from datetime import datetime

import pandas as pd

from reflector.questions import ask_question, Question, YesNoQuestion, YES_ANSWERS 
from reflector.settings import STORAGE_DIRECTORY


class Activity:

    def __init__(self, name, items, intro_text=''):
        self.name = name
        self.items = items
        self.questions = [item for item in items if isinstance(item, Question)]
        self.activities = [item for item in items if isinstance(item, Activity)]
        self.columns = self._get_columns()
        self.intro_text = intro_text

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.__str__()}>'

    def run(self) -> list:
        self.answers = []
        self._print_intro_text()
        self._get_answers()
        self.export()
        return self.answers
    
    def _get_answers(self):
        for item in self.items:
            if isinstance(item, Question):
                self.answers.append(ask_question(item))
            else:
                self.answers += item.run()

    def _get_columns(self):
        columns = []
        for item in self.items:
            if isinstance(item, Question):
                question = item
                columns.append(question.name)
            else:
                activity = item
                columns += activity.columns
        return columns

    def _print_intro_text(self):
        if self.intro_text:
            print(self.intro_text, end='\n\n')

    def export(self):
        if not self.answers:
            raise AttributeError('Cannot export Activity without answer data.')
        file_path = STORAGE_DIRECTORY / f'{self.name}.csv'
        data, columns = self.build_data()
        df = pd.DataFrame(data=data, columns=columns)
        if file_path.exists():
            previous_df = pd.read_csv(file_path)
            df = previous_df.append(df)
        df.to_csv(file_path, index=False)
        
    def build_data(self):
        """
        Data building method to add any additional data before exporting.
        Used in self._export()
        """
        data = [[str(datetime.now().strftime('%Y-%m-%d %T'))] + self.answers]
        columns = ['DateTime'] + self.columns
        return data, columns


class IntegrityActivity(Activity):

    def __init__(self, name, yes_no_questions, intro_text=''):
        if not all(isinstance(question, YesNoQuestion) for question in yes_no_questions):
            raise ValueError('questions in IntegrityActivity must be type "YesNoQuestion".')
        super().__init__(name, yes_no_questions, intro_text)

    def run(self) -> list:
        self.answers = []
        self._print_intro_text()
        self._get_answers()
        self._get_integrity()
        self._print_integrity()
        self.export()
        return self.answers
    
    def _print_integrity(self):
        print(f'\nYour {self.name.lower()} integrity is at {self.integrity}%!', end='\n\n')

    def _get_integrity(self):
        integrity_piece = 100 / len(self.questions)
        integrity = 0
        for answer in self.answers:
            if answer.casefold() in YES_ANSWERS:
                integrity += integrity_piece
        self.integrity = round(integrity)
        return self.integrity

    def build_data(self):
        data = [[str(datetime.now()), self.integrity] + self.answers]
        columns = ['DateTime', f'{self.name} Score'] + self.columns
        return data, columns
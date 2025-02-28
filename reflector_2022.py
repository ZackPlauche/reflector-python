from reflector import Activity
from reflector.questions import ListQuestion


new_activity = Activity('New Activity', [
    ListQuestion('What good things am I experiencing?'),
    ListQuestion('What should I do to enjoy them more?'),
    ListQuestion('What are you doing that\'s working?'),
    ListQuestion('What are you doing that\'s not working?'),
    ListQuestion('What should you be doing that you\'re not?'),
    ListQuestion('What\'s blocking you from acheiving what you want?'), ListQuestion('What can you do to remove those blockers?'),
    ListQuestion('What problems am I having?'),
    ListQuestion('What in your environment can you change to get the results you\'re looking to have?'),
    ListQuestion('How can you do those things?'),
]).run()

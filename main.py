from reflector import Reflector, Activity, Question, ListQuestion, TextQuestion, YesNoQuestion, OrderedListQuestion
import activities


not_owed_question = ListQuestion('What do you currently have that is good, and you are not owed by the universe?')


main_reflector = Reflector([
    activities.morning_reflection,
    activities.end_of_day_reflection,
    activities.weekly_reflection,
    activities.acclaim_system,
    activities.new_activity,
])

if __name__ == '__main__':
    main_reflector.run()

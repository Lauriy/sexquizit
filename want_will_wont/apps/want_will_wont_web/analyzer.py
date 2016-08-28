from collections import OrderedDict


def analyze(answer_set_1=None, answer_set_2=None):
    results = OrderedDict()
    results['green'] = {}
    results['yellow'] = {}
    results['red'] = {}
    if answer_set_1 and answer_set_2:
        for answer1 in answer_set_1.answers.all():
            activity = answer1.activity
            answer_match = answer_set_2.answers.filter(activity=activity.paired_with).first()

            if answer_match is None:
                continue

            result = max(answer1.value, answer_match.value)

            if result == 0:
                if activity.category.description not in results['green']:
                    results['green'][activity.category.description] = []
                results['green'][activity.category.description].append({'first': activity.description, 'second': answer_match.activity.description})
            elif result == 1:
                if activity.category.description not in results['yellow']:
                    results['yellow'][activity.category.description] = []
                results['yellow'][activity.category.description].append({'first': activity.description, 'second': answer_match.activity.description})
            elif result == 2:
                if activity.category.description not in results['red']:
                    results['red'][activity.category.description] = []
                results['red'][activity.category.description].append({'first': activity.description, 'second': answer_match.activity.description})

    return results

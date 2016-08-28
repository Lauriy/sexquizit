from collections import OrderedDict

def analyze(answer_set_1, answer_set_2):

    return OrderedDict({
        "green": {
            "sex": [{"name_pk1": "esimene küsimus", "name_pk2": "esimene paar"}],
            "muu": [{"name_pk1": "teine küsimus", "name_pk2": "teine paar"}],
        },
        "yellow": {
            "sex": [{"name_pk1": "kolmas küsimus", "name_pk2": "kolmas paar"}],
            "muu": [{"name_pk1": "neljas küsimus", "name_pk2": "neljas paar"}],
        },
        "red": {
            "sex": [{"name_pk1": "viies küsimus", "name_pk2": "viies paar"}],
            "muu": [{"name_pk1": "kuues küsimus", "name_pk2": "kuues paar"}],
        },
    })

    results = []

    for answer in answer_set_1.answers.all():
        activity = answer.activity
        answer_match = find_answer_by_activity(activity.paired_with, answer_set_2.answers.all())

        if answer_match is None:
            continue

        result = calculate_result(answer.value, answer_match.value)

        analysis_item = {
            "name_pk1": activity.description,
            "name_pk2": answer_match.activity.description,
            "result": result,
            "category": activity.category.description
        }

        results.append(analysis_item)

    return results


def find_answer_by_activity(activity, answers):
    for answer in answers.all():
        if answer.activity_id == activity.id:
            return answer
    return None


def calculate_result(value_1, value_2):
    return min(value_1, value_2)
def analyze(answer_set_1, answer_set_2):

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
def analyse(answer_set_1, answer_set_2):

    results = {}

    for answer in answer_set_1.answers:
        activity = answer.activity
        answer_match = find_answer_by_activity(activity.paired_with, answer_set_2.answers)

        if answer_match is None:
            continue

        result = calculate_result(answer.value, answer.value)

    return


def find_answer_by_activity(activity, answers):
    for answer in answers:
        if answer.activity_id == activity.id:
           return answer
    return None


def calculate_result(value_1, value_2):
    pass
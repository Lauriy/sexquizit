from django.test import TransactionTestCase

from want_will_wont.apps.want_will_wont_web.analyzer import analyze
from want_will_wont.apps.want_will_wont_web.models import Activity, AnswerSet


class ProcurementBiddingTests(TransactionTestCase):
    fixtures = [
        'activity_categories.json',
        'activities.json',
        'answer_sets.json',
        'answers.json'
    ]

    def test_analyzer(self):
        answer_set_1 = AnswerSet.objects.get(pk=7)
        answer_set_2 = AnswerSet.objects.get(pk=8)
        result = analyze(answer_set_1, answer_set_2)

        self.assertIsNotNone(result)

        # TODO: Add correct expected result and assert analyzer knows how to generate it
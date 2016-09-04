from json import loads

from django.core.management import BaseCommand

from want_will_wont.apps.want_will_wont_web.models import ActivityCategory, Activity
from want_will_wont.settings.base import BASE_DIR


class Command(BaseCommand):
    help = 'Parses questions.json and creates database entities'

    def handle(self, *args, **options):
        with open(BASE_DIR + '/apps/want_will_wont_web/management/commands/data/questions.json') as f:
            data = loads(f.read())
            for each in data[:1]:
                new_category = ActivityCategory(description=each['NameLeft'])
                new_category_pair = ActivityCategory(description=each['NameRight'])
                new_category.save()
                new_category_pair.save()
                new_category.paired_with = new_category_pair
                new_category_pair.paired_with = new_category
                new_category.save()
                new_category_pair.save()
                for question_pair in each['QuestionPairs']:
                    new_activity = Activity(category=new_category, description=question_pair['Left']['Title'])
                    new_activity_pair = Activity(category=new_category_pair, description=question_pair['Right']['Title'])
                    new_activity.save()
                    new_activity_pair.save()
                    new_activity.paired_with = new_activity_pair
                    new_activity_pair.paired_with = new_activity
                    new_activity.save()
                    new_activity_pair.save()
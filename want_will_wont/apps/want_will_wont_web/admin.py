from django.contrib import admin

from want_will_wont.apps.want_will_wont_web.models import Activity, Profile, AnswerSet, ActivityCategory, Answer, Email

admin.site.register(ActivityCategory)
admin.site.register(Activity)
admin.site.register(Profile)
admin.site.register(AnswerSet)
admin.site.register(Answer)
admin.site.register(Email)
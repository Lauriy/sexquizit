from django.contrib import admin

from want_will_wont.apps.want_will_wont_web.models import Activity, ActivitySpecification, Profile, AnswerSet, \
    AnswerSetAccessToken

admin.site.register(Activity)
admin.site.register(ActivitySpecification)
admin.site.register(Profile)
admin.site.register(AnswerSet)
admin.site.register(AnswerSetAccessToken)

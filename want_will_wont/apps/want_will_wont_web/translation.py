from modeltranslation.translator import TranslationOptions, translator

from want_will_wont.apps.want_will_wont_web.models import Activity, ActivityCategory


class ActivityTranslationOptions(TranslationOptions):
    fields = ('description',)


class ActivityCategoryTranslationOptions(TranslationOptions):
    fields = ('description',)


translator.register(Activity, ActivityTranslationOptions)
translator.register(ActivityCategory, ActivityCategoryTranslationOptions)

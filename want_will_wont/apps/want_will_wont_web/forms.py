from django.forms import ModelForm, ChoiceField, RadioSelect
from django.utils.safestring import mark_safe

from want_will_wont.apps.want_will_wont_web.models import AnswerSet, Activity, Answer


class HorizontalRadioRenderer(RadioSelect.renderer):
    def render(self):
        return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))


class ResponseForm(ModelForm):
    class Meta:
        model = AnswerSet
        exclude = ('profile', 'secret')

    def __init__(self, *args, **kwargs):
        self.gender = kwargs.pop('gender')
        super(ResponseForm, self).__init__(*args, **kwargs)
        for activity in Activity.objects.all():
            self.fields['activity_%d' % activity.pk] = ChoiceField(label=activity.description,
                                                                   widget=RadioSelect(renderer=HorizontalRadioRenderer),
                                                                   choices=Answer.ANSWER_CHOICES)
            self.fields['activity_%d' % activity.pk].widget.attrs['category'] = activity.category
            self.fields['activity_%d' % activity.pk].widget.attrs['gender'] = activity.shown_for_gender

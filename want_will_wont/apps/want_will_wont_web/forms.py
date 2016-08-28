from django.forms import ChoiceField, RadioSelect, ModelForm

from want_will_wont.apps.want_will_wont_web.models import AnswerSet, Activity, Answer, Email


class ResponseForm(ModelForm):
    class Meta:
        model = AnswerSet
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.gender = kwargs.pop('gender')
        data = kwargs.get('data')
        super(ResponseForm, self).__init__(*args, **kwargs)
        for activity in Activity.objects.all():
            self.fields['activity_%d' % activity.pk] = ChoiceField(label=activity.description, initial=Answer.WONT,
                                                                   widget=RadioSelect,
                                                                   choices=Answer.ANSWER_CHOICES, required=False)
            self.fields['activity_%d' % activity.pk].widget.attrs['category'] = activity.category
            self.fields['activity_%d' % activity.pk].widget.attrs['gender'] = activity.shown_for_gender
            if data:
                self.fields['activity_%d' % activity.pk].initial = data.get('activity_%d' % activity.pk)

    def save(self, commit=True):
        answer_set = super(ResponseForm, self).save()

        for field_name, field_value in self.cleaned_data.items():
            if field_name.startswith('activity_'):
                activity_id = int(field_name.split('_')[1])
                if answer_set and activity_id and field_value:
                    Answer(answer_set=answer_set, activity_id=activity_id, value=field_value).save()

        return answer_set


class EmailSignupForm(ModelForm):
    class Meta:
        model = Email
        fields = ('email',)

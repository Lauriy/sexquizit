from django.contrib.auth.models import User
from django.db.models import CASCADE, ForeignKey, Model, CharField, OneToOneField, \
    PositiveSmallIntegerField, EmailField, DateTimeField
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _


class ActivityCategory(Model):
    description = CharField(_('description'), max_length=255)
    paired_with = ForeignKey('self', blank=True, null=True)
    created = DateTimeField(auto_now_add=True)
    modified = DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % self.description

    class Meta:
        verbose_name_plural = _('activity categories')


class Activity(Model):
    FEMALE, MALE, BOTH = range(3)
    GENDER_CHOICES = (
        (FEMALE, _('female')),
        (MALE, _('male')),
        (BOTH, _('both'))
    )
    category = ForeignKey(ActivityCategory, related_name='activities', verbose_name=_('category'))
    description = CharField(_('description'), max_length=255)
    shown_for_gender = PositiveSmallIntegerField(_('shown for gender'), choices=GENDER_CHOICES, default=BOTH)
    paired_with = ForeignKey('self', blank=True, null=True)
    created = DateTimeField(auto_now_add=True)
    modified = DateTimeField(auto_now=True)

    def __str__(self):
        return '%s: %s' % (self.category.description, self.description,)

    class Meta:
        verbose_name_plural = _('activities')


class Profile(Model):
    FEMALE, MALE = range(2)
    GENDER_CHOICES = (
        (FEMALE, _('female')),
        (MALE, _('male'))
    )
    user = OneToOneField(User, on_delete=CASCADE, verbose_name=_('user'))
    gender = PositiveSmallIntegerField(choices=GENDER_CHOICES, blank=True, null=True)
    created = DateTimeField(auto_now_add=True)
    modified = DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % self.user.username


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User, dispatch_uid='create_user_profile')


class AnswerSet(Model):
    created = DateTimeField(auto_now_add=True)
    modified = DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % self.pk


class Answer(Model):
    WANT, WILL, WONT = range(3)
    ANSWER_CHOICES = (
        (WANT, _('want')),
        (WILL, _('will')),
        (WONT, _("won't"))
    )
    answer_set = ForeignKey(AnswerSet, related_name='answers')
    activity = ForeignKey(Activity)
    value = PositiveSmallIntegerField(choices=ANSWER_CHOICES)
    created = DateTimeField(auto_now_add=True)
    modified = DateTimeField(auto_now=True)

    def __str__(self):
        return '%s - %s - %s' % (self.answer_set_id, self.activity, self.get_value_display())


class Email(Model):
    email = EmailField(_('e-mail'), unique=True)
    created = DateTimeField(auto_now_add=True)
    modified = DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % self.email

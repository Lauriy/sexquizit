import uuid

from django.contrib.auth.models import User
from django.db.models import CASCADE, UUIDField, ForeignKey, Model, CharField, OneToOneField, \
    PositiveSmallIntegerField
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from jsonfield import JSONField


class ActivityCategory(Model):
    description = CharField(_('description'), max_length=255)

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
    category = ForeignKey(ActivityCategory, related_name='activities', verbose_name=_('category'), blank=True,
                          null=True)
    description = CharField(_('description'), max_length=255)
    shown_for_gender = PositiveSmallIntegerField(_('shown for gender'), choices=GENDER_CHOICES, default=BOTH)

    def __str__(self):
        return '%s' % self.description

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

    def __str__(self):
        return '%s' % self.user.username


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User, dispatch_uid='create_user_profile')


class AnswerSet(Model):
    profile = ForeignKey(Profile, null=True, blank=True, verbose_name=_('profile'))
    answers = JSONField(_('answers'))
    secret = UUIDField(_('secret'), default=uuid.uuid4)

    def __str__(self):
        return '%s' % self.pk

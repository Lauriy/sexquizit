import uuid

from django.contrib.auth.models import User
from django.db.models import CASCADE, UUIDField, ForeignKey, Model, CharField, OneToOneField, \
    PositiveSmallIntegerField
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _


class ActivityCategory(Model):
    description = CharField(_('description'), max_length=255)

    def __str__(self):
        return '%s' % self.description


class Activity(Model):
    FEMALE, MALE = range(2)
    GENDER_CHOICES = (
        (FEMALE, _('female')),
        (MALE, _('male'))
    )
    category = ForeignKey(ActivityCategory, related_name='activities', verbose_name=_('category'), blank=True,
                          null=True)
    description = CharField(_('description'), max_length=255)
    shown_for_gender = PositiveSmallIntegerField(_('shown for gender'), choices=GENDER_CHOICES)

    def __str__(self):
        return '%s' % self.description


class Profile(Model):
    FEMALE, MALE = range(2)
    GENDER_CHOICES = (
        (FEMALE, _('female')),
        (MALE, _('male'))
    )
    user = OneToOneField(User, on_delete=CASCADE, verbose_name=_('user'))
    gender = PositiveSmallIntegerField(choices=GENDER_CHOICES, blank=True, null=True)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User, dispatch_uid='create_user_profile')


class AnswerSet(Model):
    profile = ForeignKey(Profile, null=True, blank=True, verbose_name=_('profile'))
    #answers = Json
    owner_token = UUIDField(_('owner token'), default=uuid.uuid4)

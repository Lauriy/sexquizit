# import uuid
#
# from django.contrib.auth.models import User
# from django.db.models import CASCADE, BooleanField, UUIDField, ForeignKey, Model, CharField, OneToOneField, \
#     PositiveSmallIntegerField
# from django.utils.translation import ugettext_lazy as _
#
#
# class Activity(Model):
#     description = CharField(_('description'), max_length=255)
#     paid_only = BooleanField(_('paid only'), default=False)
#
#
# class ActivitySpecification(Model):
#     activity = ForeignKey(Activity, verbose_name=_('activity'))
#     description = CharField(_('description'), max_length=255)
#
#
# class Profile(Model):
#     FEMALE, MALE = range(2)
#     GENDER_CHOICES = (
#         (FEMALE, _('female')),
#         (MALE, _('male'))
#     )
#     user = OneToOneField(User, on_delete=CASCADE, verbose_name=_('user'))
#     gender = PositiveSmallIntegerField(choices=GENDER_CHOICES, blank=True, null=True)
#
#
# class AnswerSet(Model):
#     profile = ForeignKey(Profile, null=True, blank=True, verbose_name=_('profile'))
#     owner_token = UUIDField(_('owner token'), default=uuid.uuid4)
#
#
# class AnswerSetAccessToken(Model):
#     answer_set = ForeignKey(AnswerSet, verbose_name=_('answer set'))
#     token = UUIDField(_('token'), default=uuid.uuid4)

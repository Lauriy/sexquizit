from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, get_object_or_404, render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView

from want_will_wont.apps.want_will_wont_web.models import AnswerSet, Activity, ActivityCategory


class HomeView(TemplateView):
    template_name = 'home.html'


def answer(request):
    context = {}
    if request.method == 'GET':
        context['activity_categories'] = ActivityCategory.objects.prefetch_related('activities')

    return render_to_response('answer.html', RequestContext(request, context))


def compare(request, secret1=None, secret2=None):
    answer_set_1 = None
    if secret1:
        answer_set_1 = get_object_or_404(AnswerSet, secret=secret1)
    context = {
        'secret1': secret1,
        'secret2': secret2,
        'answer_set_1': answer_set_1
    }

    return render_to_response('compare.html', RequestContext(request, context))

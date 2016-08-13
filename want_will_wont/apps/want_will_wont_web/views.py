from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, get_object_or_404, render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView

from want_will_wont.apps.want_will_wont_web.models import AnswerSet


class HomeView(TemplateView):
    template_name = 'home.html'


@login_required
def start_answering(request):
    new_set = AnswerSet.objects.create(profile=request.user.profile)

    return redirect(reverse('answer_set_resume', args=(new_set.pk,)))


@login_required
def resume_answering(request, pk):
    context = {
        'answer_set': get_object_or_404(AnswerSet, pk=pk, profile=request.user.profile)
    }

    return render_to_response('answer.html', RequestContext(request, context))

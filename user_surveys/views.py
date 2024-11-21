from django.http import HttpResponse
from django.template import loader
from .models import Survey, Question

def user_surveys(request):
    surveys = Survey.objects.all().prefetch_related('question_set')
    template = loader.get_template('user_surveys.html')
    context = {
        'surveys': surveys,
    }
    return HttpResponse(template.render(context, request))
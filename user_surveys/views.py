from django.http import HttpResponse
from django.template import loader
from .models import Survey

# Create your views here.
def user_surveys(request):
    surveys = Survey.objects.all()
    template = loader.get_template('user_surveys.html')
    context = {'surveys': surveys}
    return HttpResponse(template.render(context, request))
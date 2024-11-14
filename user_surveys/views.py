from django.http import HttpResponse
from django.template import loader

# Create your views here.
def user_surveys(request):
    template = loader.get_template('user_surveys.html')
    return HttpResponse(template.render())
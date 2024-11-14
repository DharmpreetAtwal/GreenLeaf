from django.http import HttpResponse
from django.template import loader


# Create your views here.
def user_survey_response(request):
    template = loader.get_template('user_survey_response.html')
    return HttpResponse(template.render())
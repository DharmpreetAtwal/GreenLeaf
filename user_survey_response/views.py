from django.http import HttpResponse
from django.template import loader
from admin_dash.models import User
from .models import SurveyResponse

def user_survey_response(request, id):
    try:
        user = User.objects.get(pk=id)
        responses = SurveyResponse.objects.filter(user=user)
        template = loader.get_template('user_survey_response.html')
        context = {
            'responses': responses,
            'user': user
        }
        return HttpResponse(template.render(context, request))
    except User.DoesNotExist:
        return HttpResponse("User not found", status=404)
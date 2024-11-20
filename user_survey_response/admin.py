from django.contrib import admin
from .models import SurveyResponse, QuestionResponse, MultipleChoiceResponse, TextualResponse

admin.site.register(SurveyResponse)
admin.site.register(QuestionResponse)
admin.site.register(MultipleChoiceResponse)
admin.site.register(TextualResponse)
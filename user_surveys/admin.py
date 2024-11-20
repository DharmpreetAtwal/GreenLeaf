from django.contrib import admin
from .models import Survey, Question, MultipleChoiceQuestion, MultipleChoiceOption, TextualQuestion, MultipleChoiceResponse, TextualResponse

# Register your models here.
admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(MultipleChoiceQuestion)
admin.site.register(MultipleChoiceOption)
admin.site.register(TextualQuestion)
admin.site.register(MultipleChoiceResponse)
admin.site.register(TextualResponse)
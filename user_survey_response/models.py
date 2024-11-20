from django.db import models
from admin_dash.models import User  # Ensure consistency with user_surveys
from user_surveys.models import Survey, Question, MultipleChoiceOption, TextualQuestion

class SurveyResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_survey_responses')
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='survey_responses')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Response by {self.user.username} for {self.survey.id}"

class QuestionResponse(models.Model):
    survey_response = models.ForeignKey(SurveyResponse, related_name='question_responses', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_responses')
    response_text = models.TextField()

    def __str__(self):
        return f"Response to {self.question.text} by {self.survey_response.user.username}"

class MultipleChoiceResponse(models.Model):
    survey_response = models.ForeignKey(SurveyResponse, related_name='multiple_choice_responses', on_delete=models.CASCADE)
    option = models.ForeignKey(MultipleChoiceOption, on_delete=models.CASCADE, related_name='multiple_choice_responses')

    def __str__(self):
        return f"Multiple choice response by {self.survey_response.user.username} for {self.option.text}"

class TextualResponse(models.Model):
    survey_response = models.ForeignKey(SurveyResponse, related_name='textual_responses', on_delete=models.CASCADE)
    text_question = models.ForeignKey(TextualQuestion, on_delete=models.CASCADE, related_name='textual_responses')
    response_text = models.TextField()

    def __str__(self):
        return f"Textual response by {self.survey_response.user.username} for {self.text_question.question.text}"
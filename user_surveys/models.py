from django.db import models

from admin_dash.models import User

class Survey(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")
class SurveyResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)

class Question(models.Model):
    text = models.TextField()
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)

class MultipleChoiceQuestion(models.Model):
    max_selection = models.IntegerField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
class MultipleChoiceOption(models.Model):
    text = models.TextField()
    mult_question = models.ForeignKey(MultipleChoiceQuestion, on_delete=models.CASCADE)
class MultipleChoiceResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    option = models.ForeignKey(MultipleChoiceOption, on_delete=models.CASCADE)

class TextualQuestion(models.Model):
    char_limit = models.IntegerField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
class TextualResponse(models.Model):
    text = models.TextField()
    text_question = models.ForeignKey(TextualQuestion, on_delete=models.CASCADE)


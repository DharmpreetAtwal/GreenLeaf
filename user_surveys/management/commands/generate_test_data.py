from django.core.management.base import BaseCommand
from django.utils import timezone
from admin_dash.models import User
from user_surveys.models import Survey, Question, MultipleChoiceQuestion, TextualQuestion, MultipleChoiceOption
from user_survey_response.models import SurveyResponse, QuestionResponse, MultipleChoiceResponse, TextualResponse
import random

class Command(BaseCommand):
    help = 'Generates test data for surveys and responses'

    def handle(self, *args, **kwargs):
        # Create test users
        users = []
        for i in range(5):
            user = User.objects.create(
                username=f'testuser{i}',
                password=f'password{i}'
            )
            users.append(user)
            self.stdout.write(f'Created user: {user.username}')

        # Create surveys with questions
        survey = Survey.objects.create(id=1)
        
        # Text question
        q1 = Question.objects.create(
            text="How was your experience?",
            survey=survey
        )
        text_q = TextualQuestion.objects.create(
            question=q1,
            char_limit=500
        )

        # Multiple choice question
        q2 = Question.objects.create(
            text="Rate your satisfaction:",
            survey=survey
        )
        mc_q = MultipleChoiceQuestion.objects.create(
            question=q2,
            max_selection=1
        )
        
        options = [
            "Very Satisfied",
            "Satisfied",
            "Neutral",
            "Dissatisfied"
        ]
        
        mc_options = []
        for opt in options:
            option = MultipleChoiceOption.objects.create(
                text=opt,
                mult_question=mc_q
            )
            mc_options.append(option)

        # Generate responses
        responses = [
            "Great service overall!",
            "Could use some improvements",
            "Very helpful staff",
            "Need better response times",
            "Excellent experience"
        ]

        for user in users:
            # Create survey response
            survey_response = SurveyResponse.objects.create(
                survey=survey,
                user=user,
                submitted_at=timezone.now()
            )

            # Add text response
            TextualResponse.objects.create(
                text_question=text_q,
                response_text=random.choice(responses),
                survey_response=survey_response
            )

            # Add multiple choice response
            MultipleChoiceResponse.objects.create(
                option=random.choice(mc_options),
                survey_response=survey_response
            )

            self.stdout.write(f'Created responses for user: {user.username}')

        self.stdout.write(self.style.SUCCESS('Successfully generated test data'))
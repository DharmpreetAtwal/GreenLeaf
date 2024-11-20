# Generated by Django 5.1.3 on 2024-11-20 01:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dash', '0001_initial'),
        ('user_survey_response', '0001_initial'),
        ('user_surveys', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionresponse',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_responses', to='user_surveys.question'),
        ),
        migrations.AlterField(
            model_name='surveyresponse',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='survey_responses', to='user_surveys.survey'),
        ),
        migrations.AlterField(
            model_name='surveyresponse',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_survey_responses', to='admin_dash.user'),
        ),
        migrations.CreateModel(
            name='MultipleChoiceResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='multiple_choice_responses', to='user_surveys.multiplechoiceoption')),
                ('survey_response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='multiple_choice_responses', to='user_survey_response.surveyresponse')),
            ],
        ),
        migrations.CreateModel(
            name='TextualResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response_text', models.TextField()),
                ('survey_response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='textual_responses', to='user_survey_response.surveyresponse')),
                ('text_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='textual_responses', to='user_surveys.textualquestion')),
            ],
        ),
    ]

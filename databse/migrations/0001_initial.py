# Generated by Django 4.0.5 on 2022-07-02 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='create_interview',
            fields=[
                ('track', models.CharField(max_length=10)),
                ('test_code', models.IntegerField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=100)),
                ('position_code', models.IntegerField()),
                ('job_title', models.CharField(max_length=100)),
                ('total_questions', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='interview_notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_sent_to_user', models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], default='yes', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='parent_core_scores_db',
            fields=[
                ('candidate_id', models.IntegerField(primary_key=True, serialize=False)),
                ('candidate_name', models.CharField(max_length=100)),
                ('access_id', models.IntegerField()),
                ('resume_score', models.IntegerField()),
                ('pace', models.IntegerField()),
                ('power_words', models.CharField(max_length=100)),
                ('value_scale', models.IntegerField()),
                ('pitch_range', models.IntegerField()),
                ('gesture', models.CharField(max_length=100)),
                ('overall_sentiment_score', models.IntegerField()),
                ('overall_content', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='access_interview',
            fields=[
                ('test_code', models.OneToOneField(default='0', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='databse.create_interview')),
                ('access_code', models.IntegerField()),
                ('who_can_initiate', models.CharField(choices=[('bot', 'BOT'), ('user', 'USER')], default='bot', max_length=10)),
                ('expiry_date', models.DateTimeField()),
                ('track', models.CharField(choices=[('learn', 'LEARN'), ('hire', 'HIRE')], default='learn', max_length=10)),
                ('collect_email', models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], default='yes', max_length=10)),
                ('collect_candidate_id', models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], default='yes', max_length=10)),
                ('candidate_feedback_message', models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], default='yes', max_length=10)),
                ('voice_match', models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], default='yes', max_length=10)),
                ('collect_resume', models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], default='yes', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='bot_messages',
            fields=[
                ('test_code', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='databse.create_interview')),
                ('welcome_msg', models.CharField(max_length=500)),
                ('instruction_msg', models.CharField(max_length=500)),
                ('completion_msg', models.CharField(max_length=500)),
                ('warning_msg', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques', models.CharField(max_length=500)),
                ('ideal_ans', models.CharField(max_length=500)),
                ('ans_format', models.CharField(max_length=500)),
                ('create_interview_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='databse.create_interview')),
            ],
        ),
        migrations.CreateModel(
            name='chlid_scores_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_id', models.IntegerField()),
                ('candidate_name', models.CharField(max_length=100)),
                ('access_id', models.IntegerField()),
                ('Question_No', models.IntegerField()),
                ('Likeability', models.IntegerField()),
                ('Charm', models.CharField(max_length=100)),
                ('Confidence', models.IntegerField()),
                ('Fluency', models.IntegerField()),
                ('Content', models.CharField(max_length=100)),
                ('Overall', models.IntegerField()),
                ('parent_core_scores_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='databse.parent_core_scores_db')),
            ],
        ),
        migrations.CreateModel(
            name='report_sent_to_email',
            fields=[
                ('test_code', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='databse.create_interview')),
                ('email', models.EmailField(max_length=254)),
                ('interview_notification_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='databse.interview_notification')),
            ],
        ),
        migrations.CreateModel(
            name='interview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_interview_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='databse.create_interview')),
                ('interview_notification_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='databse.interview_notification')),
                ('access_interview_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='databse.access_interview')),
                ('bot_messages_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='databse.bot_messages')),
            ],
        ),
        migrations.CreateModel(
            name='Channels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel', models.CharField(choices=[('slack', 'SLACK'), ('whatsapp', 'WHATSAPP'), ('telegram', 'TELEGRAM')], default='slack', max_length=10)),
                ('access_interview_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='databse.access_interview')),
            ],
        ),
    ]



from django.db import models

# Create your models here.


class parent_core_scores_db(models.Model):
    candidate_id = models.IntegerField(primary_key= True )
    candidate_name = models.CharField(max_length = 100)
    access_id = models.IntegerField()
    resume_score = models.IntegerField()
    pace = models.IntegerField()
    power_words = models.CharField(max_length = 100)
    value_scale = models.IntegerField()
    pitch_range = models.IntegerField()
    gesture = models.CharField(max_length=100)
    overall_sentiment_score = models.IntegerField()
    overall_content = models.CharField(max_length=100)
    
# Creating new database Child_scores.
class chlid_scores_db(models.Model):
    candidate_id = models.IntegerField()
    candidate_name = models.CharField(max_length=100)
    access_id = models.IntegerField()
    Question_No = models.IntegerField()
    Likeability = models.IntegerField()
    Charm = models.CharField(max_length=100)
    Confidence = models.IntegerField()
    Fluency = models.IntegerField()
    Content = models.CharField(max_length=100)
    Overall = models.IntegerField()
    parent_core_scores_fk = models.ForeignKey('parent_core_scores_db', on_delete=models.CASCADE)

class create_interview(models.Model):
    track = models.CharField(max_length=10)
    test_code = models.IntegerField(primary_key= True)
    company_name = models.CharField(max_length=100)
    position_code = models.IntegerField()
    job_title = models.CharField(max_length=100)
    total_questions = models.IntegerField()

class Question(models.Model):

    ques = models.CharField(max_length=500)
    ideal_ans = models.CharField(max_length=500)
    ans_format = models.CharField(max_length=500)
    create_interview_fk = models.ForeignKey(create_interview, on_delete=models.CASCADE)



INITIATE_CHOICES = (
    ('bot', 'BOT'),
    ('user', 'USER'),
)
TRACK_CHOICES = (
    ('learn', 'LEARN'),
    ('hire', 'HIRE'),
)
COLLECT_EMAIL_CHOICES = (
    ('yes', 'YES'),
    ('no', 'NO'),
)

class access_interview(models.Model):

    test_code = models.OneToOneField(create_interview,default='0', on_delete=models.CASCADE, primary_key=True)
    access_code = models.IntegerField()
    who_can_initiate = models.CharField(max_length=10, choices=INITIATE_CHOICES, default='bot')
    expiry_date = models.DateTimeField()
    track = models.CharField(max_length=10, choices=TRACK_CHOICES, default='learn')
    collect_email = models.CharField(max_length=10, choices=COLLECT_EMAIL_CHOICES, default='yes')

    collect_candidate_id = models.CharField(max_length=10, choices=COLLECT_EMAIL_CHOICES, default='yes')
    candidate_feedback_message = models.CharField(max_length=10, choices=COLLECT_EMAIL_CHOICES, default='yes')
    voice_match = models.CharField(max_length=10, choices=COLLECT_EMAIL_CHOICES, default='yes')
    collect_resume = models.CharField(max_length=10, choices=COLLECT_EMAIL_CHOICES, default='yes')

CHANNEL_CHOICES = (
    ('slack', 'SLACK'),
    ('whatsapp', 'WHATSAPP'),
    ('telegram', 'TELEGRAM'),
)

class Channels(models.Model):
    channel = models.CharField(max_length=10, choices=CHANNEL_CHOICES, default='slack')
    access_interview_fk = models.ForeignKey('access_interview', on_delete=models.CASCADE)


class interview_notification(models.Model):

    report_sent_to_user = models.CharField(max_length=10, choices=COLLECT_EMAIL_CHOICES, default='yes')

class report_sent_to_email(models.Model):
    test_code = models.OneToOneField(create_interview,on_delete=models.CASCADE, primary_key=True)
    interview_notification_fk = models.ForeignKey('interview_notification', on_delete=models.CASCADE)
    email = models.EmailField()

class bot_messages(models.Model):
    test_code = models.OneToOneField(create_interview,on_delete=models.CASCADE, primary_key=True)
    welcome_msg = models.CharField(max_length=500)
    instruction_msg = models.CharField(max_length=500)
    completion_msg = models.CharField(max_length=500)
    warning_msg= models.CharField(max_length=500)

class interview(models.Model):
    create_interview_fk = models.ForeignKey('create_interview', on_delete=models.CASCADE)
    bot_messages_fk = models.ForeignKey('bot_messages', on_delete=models.CASCADE)
    access_interview_fk = models.ForeignKey('access_interview', on_delete=models.CASCADE)
    interview_notification_fk = models.ForeignKey('interview_notification', on_delete=models.CASCADE)

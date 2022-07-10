


from datetime import datetime
from email.mime import audio
from tkinter.messagebox import NO
from unittest.util import _MAX_LENGTH
from urllib import response
from django.db import models
from django.forms import CharField


Choices_Track = {
  ('hire', 'Hire'),
  ('learn' , 'Learn')
}

Choices_WhoCanInitiate = {
  ('bot', 'Bot'),
  ('user', 'User')
  ('both', 'Both')
}
Choices_JobTitle = {
  ('backend', 'Backend'),
  ('frontend', 'Frontend'),
  ('fullStack', 'Fullstack'),
  ('hr','Hr')
}
Choices_Interview_mode={
    ('audio', 'Audio'),
    ('video', 'Video')
}
Choices_Interview_channel= {
    ('slack', 'SLACK'),
    ('whatsapp', 'WHATSAPP'),
    ('telegram', 'TELEGRAM'),
}

Choices_Plan_Name = {
    ('standard', 'Standard')
    ('premium', 'Premium')
    ('enterprise', 'Enterprise')
}

Choices_Interaction ={
    ('one','One'),
    ('ten', 'Ten'),
    ('unlimited', 'Unlimited'),
} 

Choices_InteractionType={
    ('audio','audio'),
    ('audio_video','audio_video'),
    ('any','any'),

}

Choices_Responce= {
    ('unlimited', 'unlimited')
}

Choices_Time = {
    ('one_quarter', 'one_quarter'),
    ('unlimited', 'unlimited'),
}

Choices_AnswerFormat = {
    
    ('one_quarter', 'one_quarter'),
    ('unlimited', 'unlimited'),
}

class Candidates(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name= models.CharField(max_length =100)
    phone_number = models.CharField(max_length=12)
    email_id = models.EmailField(max_length =200, blank=True)
    created_at= models.DateTimeField(default=datetime.now)
    createdby_id = models.BigIntegerField(default= 100)
    updated_at= models.DateTimeField(default=datetime.now)
    updatedby_id = models.BigIntegerField(default= 100)
    is_active = models.BooleanField(default=True)

class Plan(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50, choices=Choices_Plan_Name)
    interaction_allowed  = models.CharField(max_length=50, choices=Choices_Interaction)
    interaction_type_allowed = models.CharField(max_length=50, choices=Choices_InteractionType)
    responces = models.CharField(max_length=50, choices=Choices_Responce)
    time_ = models.CharField(max_length=50, choices=Choices_Time)
    created_at= models.DateTimeField(default=datetime.now)
    createdby_id = models.BigIntegerField(default= 100)
    updated_at= models.DateTimeField(default=datetime.now)
    updatedby_id = models.BigIntegerField(default= 100)
    is_active = models.BooleanField(default=True)


class Companies(models.Model):
    id = models.IntegerField(primary_key=True)
    name= models.CharField(max_length =100)
    phone_number = models.CharField(max_length=12)
    plan_id = models.ForeignKey(Plan, on_delete=models.PROTECT,blank=True)
    created_at= models.DateTimeField(default=datetime.now)
    createdby_id = models.BigIntegerField(default= 100)
    updated_at= models.DateTimeField(default=datetime.now)
    updatedby_id = models.BigIntegerField(default= 100)
    is_active = models.BooleanField(default=True)


class Notifications(models.Model):
    id = models.BigIntegerField(max_length=10)
    interaction_welcome = models.CharField(max_length= 500)
    interaction_instruction = models.CharField(max_length= 500)
    interaction_completion_message = models.CharField(max_length= 500)
    bot_error_message = models.CharField(max_length= 500)
    created_at= models.DateTimeField(default=datetime.now)
    createdby_id = models.BigIntegerField(default= 100)
    updated_at= models.DateTimeField(default=datetime.now)
    updatedby_id = models.BigIntegerField(default= 100)
    is_active = models.BooleanField(default=True)


class Scores(models.Model):
    id = models.BigIntegerField(primary_key=True)
    resume_score = models.IntegerField(max_length= 2, default=0)
    pace = models.IntegerField(max_length= 2, default=0)
    power_words = models.IntegerField(max_length= 2, default=0)
    value_scale = models.IntegerField(max_length= 2, default=0)
    pitch_range = models.IntegerField(max_length= 2, default=0)
    gesture = models.IntegerField(max_length= 2, default=0)
    content_score = models.IntegerField(max_length= 2, default=0)
    overall = models.IntegerField(max_length= 2, default=0)



class Indivdual_reports(models.Model):
    id = models.BigIntegerField(primary_key=True)
    track = models.CharField(max_length=100)
    initial_box = models.CharField(max_length=100)
    letter_text = models.CharField(max_length=100)
    rating_variable = models.CharField(max_length=100)
    pace_text = models.CharField(max_length=100)
    power_word_text = models.CharField(max_length=100)
    volume_and_pitch = models.CharField(max_length=100)
    word_cloud = models.CharField(max_length=100)
    sentiment_analysis = models.CharField(max_length=100)
    gesture_text = models.CharField(max_length=100)
    content_rating = models.CharField(max_length=100)
    
class LeaderBoard_report(models.Model):
    id = models.BigIntegerField(primary_key=True)
    track = models.CharField(max_length=100)
    initial_box = models.CharField(max_length=100)
    letter_text = models.CharField(max_length=100)
    rating_variable = models.CharField(max_length=100)
     

################################################################



class Test(models.Model):
    id = models.BigIntegerField(primary_key=True, )
    company_id= models.ForeignKey(Companies, on_delete=models.PROTECT,blank=True)
    access_code = models.IntegerField()
    who_can_initiate = models.CharField(max_length= 50, choices=Choices_WhoCanInitiate, default='bot')
    interview_mode = models.CharField(max_length=50, choices=Choices_Interview_mode, default='audio')
    track = models.CharField(max_length=50, choices=Choices_Track, default='slack')
    collect_email = models.BooleanField(default=False)
    collect_candidate_email = models.BooleanField(default=False)
    voice_match = models.BooleanField(default=False)
    hiring_email= models.EmailField(max_length=200)
    collect_resume = models.BooleanField(default=False)
    job_code = models.BigIntegerField(default=1111)
    job_title = models.CharField(max_length=50, choices=Choices_JobTitle, default='slack')
    job_discription = models.CharField(max_length=500)
    total_question = models.IntegerField(max_length = 100)
    created_at= models.DateTimeField(default=datetime.now)
    createdby_id = models.BigIntegerField(default= 100)
    updated_at= models.DateTimeField(default=datetime.now)
    updatedby_id = models.BigIntegerField(default= 100)
    is_active = models.BooleanField(default=True)
    notification_id = models.ForeignKey(Notifications, on_delete=models.PROTECT,blank=True)

class Questions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    question = models.CharField(max_length= 500)
    answer_format = models.CharField(max_length=50, choices=Choices_AnswerFormat)
    ideal_answer = models.CharField(max_length= 500)
    should_rate = models.BooleanField(default=True)
    test_id= models.ForeignKey(Test, on_delete=models.PROTECT,blank=True)
    created_at= models.DateTimeField(default=datetime.now)
    createdby_id = models.BigIntegerField(default= 100)
    updated_at= models.DateTimeField(default=datetime.now)
    updatedby_id = models.BigIntegerField(default= 100)
    is_active = models.BooleanField(default=True)


class Interactions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    candidate_id = models.ForeignKey(Candidates,on_delete=models.PROTECT,blank=True) #Insert Foreignkey
    test_id = models.ForeignKey(Test,on_delete=models.PROTECT,blank = True ) #Insert ForeignKey
    candidate_feedback = models.CharField(max_length=100)
    report_sent_to_user = models.BooleanField(default=False)
    channel = models.CharField(choices=Choices_Interview_channel,max_length=20)
    created_at= models.DateTimeField(default=datetime.now)
    createdby_id = models.BigIntegerField(default= 100)
    updated_at= models.DateTimeField(default=datetime.now)
    updatedby_id = models.BigIntegerField(default= 100)
    score_id = models.ForeignKey(Scores,on_delete=models.PROTECT,blank = True ) #Insert ForeignKey
    individual_report_id = models.ForeignKey(Indivdual_reports,on_delete=models.PROTECT,blank = True ) #Insert ForeignKey

    is_active = models.BooleanField(default=True)
    
class Responces(models.Model):
    id = models.IntegerField(primary_key=True)
    interaction_id = models.ForeignKey(Interactions,on_delete=models.PROTECT,blank=True) #Insert Foreignkey
    question_id = models.ForeignKey(Questions,on_delete=models.PROTECT,blank=True) #Insert Foreignkey
    candidate_id = models.ForeignKey(Candidates,on_delete=models.PROTECT,blank=True) #Insert Foreignkey
    response = models.CharField(max_length=500)
    created_at= models.DateTimeField(default=datetime.now)
    createdby_id = models.BigIntegerField(default= 100)
    updated_at= models.DateTimeField(default=datetime.now)
    updatedby_id = models.BigIntegerField(default= 100)
    is_active = models.BooleanField(default=True)




class Score_per_question(models.Model):
    id = models.BigIntegerField(primary_key=True,)
    score_id = models.ForeignKey(Scores,on_delete=models.PROTECT,blank = True ) #Insert ForeignKey
    question_id = models.ForeignKey(Questions,on_delete=models.PROTECT,blank = True ) #Insert ForeignKey
    likebality = models.IntegerField(max_length= 2, default=0)
    charm = models.IntegerField(max_length= 2, default=0)
    confidence = models.IntegerField(max_length= 2, default=0)
    fluency = models.IntegerField(max_length= 2, default=0)
    content = models.IntegerField(max_length= 2, default=0)
    overall = models.IntegerField(max_length= 2, default=0)





# # Create your models here.
# class parent_core_scores_db(models.Model):
    
#     candidate_id = models.IntegerField(primary_key= True )
#     candidate_name = models.CharField(max_length = 100)
#     access_id = models.IntegerField()
#     resume_score = models.IntegerField()
#     pace = models.IntegerField()
#     power_words = models.CharField(max_length = 100)
#     value_scale = models.IntegerField()
#     pitch_range = models.IntegerField()
#     gesture = models.CharField(max_length=100)
#     overall_sentiment_score = models.IntegerField()
#     overall_content = models.CharField(max_length=100)
    
# # Creating new database Child_scores.
# class chlid_scores_db(models.Model):

    
#     parent_core_scores_fk = models.ForeignKey('parent_core_scores_db', on_delete=models.CASCADE, primary_key=True)
#     candidate_name = models.CharField(max_length=100)
#     access_id = models.IntegerField()
#     Question_No = models.IntegerField()
#     Likeability = models.IntegerField()
#     Charm = models.CharField(max_length=100)
#     Confidence = models.IntegerField()
#     Fluency = models.IntegerField()
#     Content = models.CharField(max_length=100)
#     Overall = models.IntegerField()

# class create_interview(models.Model):

#     test_code = models.IntegerField(primary_key= True)
#     track = models.CharField(max_length=10)
#     company_name = models.CharField(max_length=100)
#     position_code = models.IntegerField()
#     job_title = models.CharField(max_length=100)
#     total_questions = models.IntegerField()

# class Question(models.Model):

#     create_interview_fk = models.ForeignKey(create_interview,primary_key=True, on_delete=models.CASCADE)
#     ques = models.CharField(max_length=500)
#     ideal_ans = models.CharField(max_length=500)
#     ans_format = models.CharField(max_length=500)



# INITIATE_CHOICES = (
#     ('bot', 'BOT'),
#     ('user', 'USER'),
# )
# TRACK_CHOICES = (
#     ('learn', 'LEARN'),
#     ('hire', 'HIRE'),
# )
# COLLECT_EMAIL_CHOICES = (
#     ('yes', 'YES'),
#     ('no', 'NO'),
# )

# class access_interview(models.Model):

#     test_code = models.OneToOneField(create_interview,default='0', on_delete=models.CASCADE, primary_key=True)
#     access_code = models.IntegerField()
#     who_can_initiate = models.CharField(max_length=10, choices=INITIATE_CHOICES, default='bot')
#     expiry_date = models.DateTimeField()
#     track = models.CharField(max_length=10, choices=TRACK_CHOICES, default='learn')
#     collect_email = models.CharField(max_length=10, choices=COLLECT_EMAIL_CHOICES, default='yes')

#     collect_candidate_id = models.CharField(max_length=10, choices=COLLECT_EMAIL_CHOICES, default='yes')
#     candidate_feedback_message = models.CharField(max_length=10, choices=COLLECT_EMAIL_CHOICES, default='yes')
#     voice_match = models.CharField(max_length=10, choices=COLLECT_EMAIL_CHOICES, default='yes')
#     collect_resume = models.CharField(max_length=10, choices=COLLECT_EMAIL_CHOICES, default='yes')

# CHANNEL_CHOICES = (
#     ('slack', 'SLACK'),
#     ('whatsapp', 'WHATSAPP'),
#     ('telegram', 'TELEGRAM'),
# )

# class Channels(models.Model):
#     channel = models.CharField(max_length=10, choices=CHANNEL_CHOICES, default='slack')
#     access_interview_fk = models.ForeignKey('access_interview', on_delete=models.CASCADE)


# class interview_notification(models.Model):

#     test_code = models.OneToOneField(create_interview,default='0', on_delete=models.CASCADE, primary_key=True)
#     report_sent_to_user = models.CharField(max_length=10, choices=COLLECT_EMAIL_CHOICES, default='yes')

# class report_sent_to_email(models.Model):
#     test_code = models.OneToOneField(create_interview,on_delete=models.CASCADE, primary_key=True)
#     interview_notification_fk = models.ForeignKey('interview_notification', on_delete=models.CASCADE)
#     email = models.EmailField()

# class bot_messages(models.Model):
#     test_code = models.OneToOneField(create_interview,on_delete=models.CASCADE, primary_key=True)
#     welcome_msg = models.CharField(max_length=500)
#     instruction_msg = models.CharField(max_length=500)
#     completion_msg = models.CharField(max_length=500)
#     warning_msg= models.CharField(max_length=500)

# class interview(models.Model):
#     create_interview_fk = models.ForeignKey('create_interview', on_delete=models.CASCADE)
#     bot_messages_fk = models.ForeignKey('bot_messages', on_delete=models.CASCADE)
#     access_interview_fk = models.ForeignKey('access_interview', on_delete=models.CASCADE)
#     interview_notification_fk = models.ForeignKey('interview_notification', on_delete=models.CASCADE)

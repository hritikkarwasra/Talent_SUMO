from enum import Enum
from django.db import models

class WhoCanInitiate(Enum):
    BOT = 'bot'
    USER = 'user'
    BOTH = 'both'
class Track(Enum):
    HIRE = 'hire'
    LEARN = 'learn'
class JobTitle(Enum):
    FRONTEND = 'frontend',
    BACKEND = 'backend',
    FULLSTACK = 'fullstack',
    HR = 'Hr'
class PlanName (Enum):
  STANDARD = 'standard'
  PREMIUM = 'premium'
  ENTERPRISE = 'enterprise'

class interaction (Enum):
  ONE = 'one'
  TEN = 'ten'
  UNLIMITED = 'unlimited'

class interactionType (Enum):
  AUDIO = 'audio'
  AUDIO_VIDEO = 'audio_video'
  ANY = 'any'


class Response (Enum):
  UNLIMITED = 'unlimited'


class Time (Enum):
  ONE_QUATER = 'one_quarter'
  UNLIMITED = 'unlimited'


class AnswerFormat (Enum):
  ONE_QUATER = 'one_quarter'
  UNLIMITED = 'unlimited'



class Employee_data(models.Model):
    employee_name = models.CharField(max_length=50)
    employee_email = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

class Company_Users(models.Model):
    company_id = models.BigAutoField(unique=True)
    creator_name = models.CharField(max_length=30)
    is_superuser = models.BooleanField(False)
    created_at = models.DateTimeField(auto_now_add=True)

class tests(models.Model): 
    access_code = models.CharField(max_length=20)
    who_can_initiate = WhoCanInitiate
    expiry_date = models.DateTimeField
    interview_mode = models.CharField(max_length=20)
    track = Track
    collect_mail = models.BooleanField
    collect_candidate_mail = models.BooleanField
    voice_match = models.BooleanField
    hiring_email = models.CharField(max_length=20)
    collect_resume = models.BooleanField
    job_code = models.BigIntegerField
    job_title = JobTitle
    job_describtion = models.CharField(max_length=255)
    total_question = models.IntegerField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updatedby_id = models.BigIntegerField
    is_active = models.BooleanField
    notification_id = models.BigIntegerField
    company_id = models.BigIntegerField

class companies(models.Model):
    name = models.CharField
    phone_number = models.CharField(max_length=12)
    plan_id = models.CharField
    created_at = models.DateTimeField(auto_now_add=True)
    createdby_id = models.BigIntegerField
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField
    
class Candidates(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=12)
    email = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    createdby_id = models.BigIntegerField
    updated_at = models.DateTimeField(auto_now=True)
    updatedby_id = models.BigIntegerField
    is_active = models.BooleanField
    
class Interactions(models.Model):
    candidate_id = models.BigIntegerField
    test_id = models.BigIntegerField
    candidate_feedback = models.CharField
    report_send_to_user = models.BooleanField
    channel_1 = models.CharField(max_length=20)
    channel_2 = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    createdby_id = models.BigIntegerField
    updated_at = models.DateTimeField(auto_now=True)
    updatedby_id = models.BigIntegerField
    score_id = models.BigIntegerField
    individual_report_id = models.BigIntegerField
    is_active = models.BooleanField
    
class Scores(models.Model):
    resume_score = models.IntegerField
    pace = models.CharField(max_length=20)
    power_words = models.CharField(max_length=20)
    value_scale = models.IntegerField
    pitch_range = models.IntegerField
    gesture = models.CharField(max_length=20)
    content_score = models.IntegerField
    overall = models.IntegerField
    
class Score_per_Question(models.Model):
    score_id = models.BigIntegerField
    question_id = models.BigIntegerField
    likeability = models.IntegerField
    charm = models.IntegerField
    confidence = models.IntegerField
    resume_score = models.IntegerField
    fluency = models.IntegerField
    content = models.IntegerField
    overall = models.IntegerField

class questions(models.Model):
    question = models.CharField(max_length=2000)
    answer_format = AnswerFormat
    ideal_answer = models.CharField(max_length=20)
    test_id = models.BigIntegerField
    created_at = models.DateTimeField(auto_now_add=True)
    createdby_id = models.BigIntegerField
    updated_at = models.DateTimeField(auto_now=True)
    updatedby_id = models.BigIntegerField
    should_score = models.BooleanField
    is_active = models.BooleanField
    Indexes = test_id

class plan(models.Model):
    name = PlanName
    interaction_allowed = interaction
    interaction_type_allowed = interactionType
    responses = Response
    time = Time
    created_at = models.DateTimeField(auto_now_add=True)
    createdby_id = models.BigIntegerField
    updated_at = models.DateTimeField(auto_now=True)
    updatedby_id = models.BigIntegerField
    is_active = models.BooleanField

class notifications(models.Model):
    interaction_welcome = models.CharField(max_length=500)
    interaction_instruction = models.CharField(max_length=500)
    interaction_compietion_message = models.CharField(max_length=500)
    bot_error_message = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    createdby_id = models.BigIntegerField
    updated_at = models.DateTimeField(auto_now=True)
    updatedby_id = models.BigIntegerField
    is_active = models.BooleanField

class individual_reports(models.Model):
    track = Track
    initial_box = models.CharField
    letter_text = models.CharField
    rating_variable = models.CharField
    pace_text = models.CharField
    power_word_text = models.CharField
    volume_and_pitch = models.CharField
    word_cloud_text = models.CharField
    sentiment_analysis = models.CharField
    gesture_text = models.CharField
    content_rating_text = models.CharField
    
class individual_reports(models.Model):
    track = Track
    initial_box = models.CharField
    letter_text = models.CharField
    rating_variable = models.CharField
    
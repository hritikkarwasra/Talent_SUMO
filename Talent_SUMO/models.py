from enum import Enum
from pyexpat import model
from django.db import models

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
        HR = 'Hr',

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
    

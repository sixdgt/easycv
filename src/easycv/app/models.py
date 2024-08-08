from django.db import models

# Create your models here.
class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=200, null=False)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, null=False)
    email = models.EmailField(max_length=200, unique=True, null=False)
    contact = models.CharField(max_length=20, null=False)
    designation = models.CharField(max_length=200, null=False)
    summary = models.TextField(max_length=255, null=False)

class Education(models.Model):
    edu_level = models.CharField(max_length=100, null=False)
    institution = models.CharField(max_length=100)
    board = models.CharField(max_length=255, null=False)
    start_date = models.DateField()
    end_date = models.DateField()
    grade = models.CharField(max_length=100)
    address = models.CharField(max_length=255, null=False)
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)

class SocialLink(models.Model):
    platform = models.CharField(max_length=100, null=False)
    url = models.CharField(max_length=255, null=False)
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)

class Experience(models.Model):
    job_title = models.CharField(max_length=255, null=False)
    company = models.CharField(max_length=255, null=False)
    start_date = models.DateField()
    end_date = models.DateField()
    is_working = models.IntegerField()
    address = models.CharField(max_length=255, null=False)
    description= models.CharField(max_length=255, null=False)
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)

class Skill(models.Model):
    skill = models.CharField(max_length=255, null=False)
    profeciency = models.CharField(max_length=255, null=False)
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)

class Project(models.Model):
    title = models.CharField(max_length=255, null=False)
    is_recent = models.BooleanField()
    project_url = models.CharField(max_length=200, null=False)
    description = models.TextField(max_length=255, null=False)
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)

class Reference(models.Model):
    full_name = models.CharField(max_length=255, null=False)
    contact = models.CharField(max_length=20, null=False)
    designation = models.CharField(max_length=200, null=False)
    company = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=200, null=False)
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)

class Declaration(models.Model):
    declaration = models.CharField(max_length=255, null=False)
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)

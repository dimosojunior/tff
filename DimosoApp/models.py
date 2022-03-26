from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from datetime import datetime, date
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from ckeditor_uploader.fields import RichTextUploadingField




# Create your models here.
class Teams(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	link = models.CharField(max_length=200, blank=True, null=True)	
	u = models.URLField(max_length=200, blank=True, null=True)
	post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	image = models.ImageField(blank=True, null=True, upload_to="media/teams/")
class TeamInformations(models.Model):
	team_name = models.CharField(max_length=200, blank=True, null=True)
	link = models.CharField(max_length=200, blank=True, null=True)	
	post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	image = models.ImageField(blank=True, null=True, upload_to="media/teams/")

	prayer_name = models.CharField(max_length=200, blank=True, null=True)
	total_goals = models.IntegerField(blank=True, null=True)
	total_assists = models.IntegerField(blank=True, null=True)
	total_yellow = models.IntegerField(blank=True, null=True)
	total_red = models.IntegerField(blank=True, null=True)
	goal_summary = RichTextUploadingField(blank=True, null=True)
	assists_summary = RichTextUploadingField(blank=True, null=True)
	yellow_summary = RichTextUploadingField(blank=True, null=True)
	red_summary = RichTextUploadingField(blank=True, null=True)
	all_summary = RichTextUploadingField(blank=True, null=True)
	last_update = models.DateField(auto_now=True, blank=True, null=True)

class Msimamo(models.Model):
	title = models.CharField(max_length=200, blank=True, null=True)
	header = RichTextUploadingField(blank=True, null=True)
	name = models.CharField(max_length=200, blank=True, null=True)
	msimamo = RichTextUploadingField(blank=True, null=True)	
	last_update = models.DateTimeField(auto_now=True, blank=True, null=True)
	playing_date = models.CharField(max_length=200, blank=True, null=True)

class Ratiba(models.Model):
	title = models.CharField(max_length=200, blank=True, null=True)
	name = models.CharField(max_length=200, blank=True, null=True)
	link = models.CharField(max_length=200, blank=True, null=True)
	ratiba = RichTextUploadingField(blank=True, null=True)	
	header = RichTextUploadingField(blank=True, null=True)
	last_update = models.DateTimeField(auto_now=True, blank=True, null=True)
	playing_date = models.CharField(max_length=200, blank=True, null=True)
	playing_date = models.CharField(max_length=200, blank=True, null=True)
	post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
class Results(models.Model):
	title = models.CharField(max_length=200, blank=True, null=True)
	name = models.CharField(max_length=200, blank=True, null=True)
	link = models.CharField(max_length=200, blank=True, null=True)
	ratiba = RichTextUploadingField(blank=True, null=True)	
	header = RichTextUploadingField(blank=True, null=True)
	last_update = models.DateTimeField(auto_now=True, blank=True, null=True)
	playing_date = models.CharField(max_length=200, blank=True, null=True)
	post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

		
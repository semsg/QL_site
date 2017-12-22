from django.db import models

class Article(models.Model):
	title = models.CharField(max_length=100)
	text = models.TextField(blank=True)
	code = models.TextField(blank=True)
	
	def __str__(self):
		return self.title 
	class Meta:
		ordering = ['title']

class UserMessage(models.Model):
	user_name = models.CharField(max_length=30)
	public_message = models.BooleanField(default=False)
	comment = models.TextField(blank=True)
	email = models.EmailField(blank=True, null=True)
	date_of_note = models.DateTimeField(blank=True, null=True)
	admin_answer = models.TextField(blank=True)
	

class TextNew(models.Model):
	name = models.CharField(max_length=200)
	text = models.TextField(blank=True)
	text_1 = models.TextField(blank=True)
	text_2 = models.TextField(blank=True)
	text_3 = models.TextField(blank=True)
	text_4 = models.TextField(blank=True)
	text_5 = models.TextField(blank=True)
	text_6 = models.TextField(blank=True)
	image = models.CharField(blank=True, max_length=100)
	link = models.CharField(blank=True, max_length=500)
	date = models.DateTimeField()

	def __str__(self):
		return self.name
	class Meta:
		ordering = ['date']

class LedMod_GTR2416(models.Model):
	numb = models.CharField(blank=True, max_length=100)
	sub_title = models.CharField(blank=True, max_length=100)
	text = models.TextField(blank=True)
	text_1 = models.TextField(blank=True)
	text_2 = models.TextField(blank=True)
	text_3 = models.TextField(blank=True)
	text_4 = models.TextField(blank=True)
	text_5 = models.TextField(blank=True)
	text_6 = models.TextField(blank=True)
	image = models.CharField(blank=True, max_length=100)
	link = models.CharField(blank=True, max_length=100)

class ArticleBox(models.Model):
	title = models.CharField(max_length=200)
	numb = models.CharField(blank=True, max_length=100)
	sub_title = models.CharField(blank=True, max_length=100)
	image = models.CharField(blank=True, max_length=200)
	image_2 = models.CharField(blank=True, max_length=200)
	image_3 = models.CharField(blank=True, max_length=200)
	text = models.TextField(blank=True)
	text_1 = models.TextField(blank=True)
	text_2 = models.TextField(blank=True)
	text_3 = models.TextField(blank=True)
	text_4 = models.TextField(blank=True)
	text_5 = models.TextField(blank=True)
	text_6 = models.TextField(blank=True)

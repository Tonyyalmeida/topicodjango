import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.conf import settings #for changing the user model
from django.db import models #for changing the user model
# Create your models here.

#not needed at the moment
class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', null=True,on_delete=models.CASCADE)
    #related name in model has to match the one in serializer
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text




LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    class Meta:
        ordering = ['created']

class WordList(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100, blank=True, default='')
   # user = models.ForeignKey(MyUser, related_name="users", null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    isTodo = models.BooleanField(default=True)
    def __str__(self):
       return self.title

class WordPair(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    wordEnglish = models.CharField(max_length=100, blank=True, default='')
    wordVietnamese = models.CharField(max_length=100, blank=True, default='')
    exampleEnglish = models.CharField(max_length=250, blank=True, default='')
    exampleVietnamese = models.CharField(max_length=250, blank=True, default='')
    wordList = models.ForeignKey(WordList, related_name='WordPairs', null=True, on_delete=models.SET_NULL)
    score = models.IntegerField(default=0)
    def __str__(self):
        return self.wordEnglish






#class Choice(models.Model):
 #   question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
  #  choice_text = models.CharField(max_length=200)
   # votes = models.IntegerField(default=0)


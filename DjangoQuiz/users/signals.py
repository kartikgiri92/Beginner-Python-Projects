from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Score
from quiz.models import QuizTable

@receiver(post_save, sender=User)
def create_scores_user(sender, instance, created, **kwargs):
    if created:
    	QuizObjects = QuizTable.objects.all()
    	for i in QuizObjects:
    		Score.objects.create(user = instance, qno = i ,score = 0)

# @receiver(post_save, sender=User)
# def save_profile_user(sender, instance, **kwargs):
# 	instance.score.save()


@receiver(post_save, sender=QuizTable)
def create_scores_quiz(sender, instance, created, **kwargs):
    if created:
    	UserObjects = User.objects.all()
    	for i in UserObjects:
    		Score.objects.create(user = i, qno = instance, score = 0)

# @receiver(post_save, sender=User)
# def save_profile_quiz(sender, instance, **kwargs):
# 	instance.score.save()
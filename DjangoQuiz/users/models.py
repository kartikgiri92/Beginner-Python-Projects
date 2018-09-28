from django.db import models
from django.contrib.auth.models import User

from quiz.models import QuizTable

class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User Name")
    qno = models.ForeignKey(QuizTable, on_delete=models.CASCADE, verbose_name="QUIZ NUMBER", default = 0)
    score = models.IntegerField("Score", default = 0)

    # def __str__(self):
    #     return('{} - {}'.format(self.user, self.qno))

    class Meta:
        verbose_name_plural = 'Score Table'
        unique_together = (("user", "qno"),)
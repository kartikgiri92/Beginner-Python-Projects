from django.db import models

# Create your models here.
class QuizTable(models.Model):
    qno = models.IntegerField('QUIZ NUMBER', primary_key = True)
    qdesc = models.CharField('QUIZ Description', max_length = 50)

    class Meta:
        verbose_name_plural = 'QUIZ TABLE'

    def __str__(self):
        return ("Quiz {}".format(self.qno))

class QuestionTable(models.Model):
    qid = models.CharField('Question ID', max_length = 25, primary_key = True)
    qtext = models.CharField('Question Text', max_length = 125)
    opt1 = models.CharField('Option 1', max_length = 50)
    opt2 = models.CharField('Option 2', max_length = 50)
    opt3 = models.CharField('Option 3', max_length = 50)
    opt4 = models.CharField('Option 4', max_length = 50)
    ans = models.CharField('Correct Answer', max_length = 25)
    qno = models.ForeignKey(QuizTable, on_delete=models.CASCADE, verbose_name="QUIZ NUMBER")

    class Meta:
        verbose_name_plural = 'QUESTION TABLE'
        # ordering = ["-qid"]

    def __str__(self):
        return ("Question ID {}".format(self.qid))
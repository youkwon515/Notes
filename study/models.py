from django.db import models

# Create your models here.

class Memo(models.Model):
    title = models.CharField(max_length=10)

    SUBJECT_CHOICES = [
        (1, "화면구현"),
        (2, "구현"),
        (3, "응용"),
        (4, "영어"), 
        (5, "분석"),
        (6, "논술"),
        (7, "수학"),
        (8, "국어"),
    ]

    subject = models.IntegerField(choices=SUBJECT_CHOICES, default=None)

    content = models.TextField()

    dt_created = models.DateTimeField(auto_now_add=True)
    dt_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
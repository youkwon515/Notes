from django.db import models

# Create your models here.

class Memo(models.Model):
    title = models.CharField(max_length=10)

    SUBJECT_CHOICES = [
        ("화면구현", "화면구현"),
        ("구현", "구현"),
        ("응용", "응용"),
        ("영어", "영어"), 
        ("분석", "분석"),
        ("논술", "논술"),
        ("수학", "수학"),
        ("국어", "국어"),
    ]

    subject = models.CharField(choices=SUBJECT_CHOICES, max_length=4, default=None)

    content = models.TextField()

    dt_created = models.DateTimeField(auto_now_add=True)
    dt_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
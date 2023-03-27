from django import forms
from .models import Memo

class MemoForm(forms.ModelForm):
    class Meta:
        model = Memo
        fields = [
            "title",
            "subject",
            "content",
        ]

        CHOICES = (
            ('ME', '1'),
            ('YOU', '2'),
            ('WE', '3'),
        )


        widgets = {
            "subject": forms.RadioSelect,
        }
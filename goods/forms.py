from django import forms
from goods.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
                'text': forms.Textarea(attrs={
                    "class": "form-control",
                    "placeholder": "Напиши свой никому не нужный коммент",
                    "rows": 5
                })
            }

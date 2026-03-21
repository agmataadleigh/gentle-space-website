from django import forms
from .models import Post

class GratitudeForm(forms.ModelForm):
    class Meta:
        model = Post
        # We only need the content field for your design
        fields = ['content']
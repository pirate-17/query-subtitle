from django import forms
from .models import videos, search_keywords

class VideosForm(forms.ModelForm):
    # name = forms.CharField(max_length=100)
    class Meta:
        model = videos
        fields = ['file']
        widgets = {
            'file': forms.FileInput(attrs={'accept': 'video/mp4'})
        }

class SearchForm(forms.ModelForm):
    search_keyword = forms.CharField(max_length=100)
    class Meta:
        model = search_keywords
        fields = ['search_keyword']
        widgets = {
            'search_keyword': forms.TextInput(attrs={'placeholder': 'Enter the keyword to search'})
        }
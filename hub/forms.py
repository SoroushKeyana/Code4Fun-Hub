# hub/forms.py
from django import forms
from .models import Project, ForumPost, ForumComment, ForumCategory
from django.contrib.auth.forms import UserCreationForm


class SuperuserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'email', 'password1', 'password2']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'project_file']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add custom styling or additional attributes if neededx



class ForumPostForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ['title', 'content', 'category']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].required = False

class ForumCommentForm(forms.ModelForm):
    class Meta:
        model = ForumComment
        fields = ['content']

class ForumCategoryForm(forms.ModelForm):
    class Meta:
        model = ForumCategory
        fields = ['name']


class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=255, required=False)
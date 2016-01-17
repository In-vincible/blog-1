from django import forms
from django.contrib.auth.models import User
from .models import Post


class CreatePostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ['title', 'title_en', 'author', 'po_type', 'content', 'tags']

	# def clean_content(self):
	# 	content = self.cleaned_data('content')
	# 	if self.cleaned_data.is_valid():
	# 		return content
	# def get_author(self):
	# 	author = request.user
	# 	return author
class LoginForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ['username', 'password']

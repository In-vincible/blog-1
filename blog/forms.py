from django import forms

from .models import Post

class CreatePostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ['title','author', 'po_type', 'content']

	# def clean_content(self):
	# 	content = self.cleaned_data('content')
	# 	if self.cleaned_data.is_valid():
	# 		return content
	# def get_author(self):
	# 	author = request.user
	# 	return author

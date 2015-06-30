from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django import forms

from .models import Post, Category, About

# Create your views here.
NEW_TEMPLATE_PATH = "blog/bootstrap_blog_template/"

def index(request):
	'''
	Display blog list
	'''
	posts = Post.objects.all()
	categories = Category.objects.all()
	# return render(request, 'blog/bootstrap_blog_template/index.html', {'posts': posts, 'categories': categories})
	return render(request, 'index.html', {'posts': posts, 'categories': categories})

def post(request, pk):
	'''
	Article detail
	'''
	post = get_object_or_404(Post, pk=pk)
	categories = Category.objects.all()
	return render(request, 'post.html', {'post': post, 'categories': categories})
	# return render_to_response("blog/post.html", {'post':post}, context_instance=RequestContext(request))

def category(request, pk):
	cate = get_object_or_404(Category, pk=pk)
	posts = cate.post_set.all()
	# return render(request, 'blog/index.html',
	# 	{'posts': posts,
	# 	'cate_name': cate.name,
	# 	'is_category': True,
	# 	'categories': Category.objects.all()})
	return render(request, 'index.html',
		{'posts': posts,
		'cate_name': cate.name,
		'is_category': True,
		'categories': Category.objects.all()})


def about(request):
	page = About.objects.get(pk=1)
	categories = Category.objects.all()
	# return render(request, NEW_TEMPLATE_PATH +'about.html', {'post':page, 'categories':categories})
	return render(request, 'about.html', {'post':page, 'categories':categories})



class ArticleForm(forms.Form):
	class Meta:
		model = Post
		fields = ['title', 'content']
	

def create(request):
	if request.method == 'POST':
		form = ArticleForm(request.POST)
		if form.is_valid():
			new_post = form.save()
			return HttpResponseRedirect('/post/' + str(new_post.pk))
	form = ArticleForm()
	return render(request, 'blog/create_article.html', {'form':form})














	



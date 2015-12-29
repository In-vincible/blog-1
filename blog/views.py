from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext

from .forms import CreatePostForm
from .models import Post, Category, About

# Create your views here.

# NEW_TEMPLATE_PATH = "blog/bootstrap_blog_template/"

def index(request):
	'''
	Display blog list
	'''
	posts = Post.objects.all()
	categories = Category.objects.all()
	context =  {
		'posts': posts, 
		'categories': categories
	}
	return render(request, 'index.html', context)

def post(request, pk):
	'''
	Article detail
	'''
	post = get_object_or_404(Post, pk=pk)
	categories = Category.objects.all()
	context = {
		'post': post, 
		'categories': categories
	}
	return render(request, 'post.html', context)

def category(request, pk):
	cate = get_object_or_404(Category, pk=pk)
	posts = cate.post_set.all()

	context = {
		'posts': posts,
		'cate_name': cate.name,
		'is_category': True,
		'categories': Category.objects.all()
	}
	return render(request, 'index.html', context)


def about(request):
	page = About.objects.get(pk=1)
	categories = Category.objects.all()
	context = {
		'post':page, 'categories':categories
	}
	return render(request, 'about.html', context)


def create(request):
	form = CreatePostForm(request.POST or None)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/')
	context = {'form': form}
	return render(request, 'post_create.html', context)

def edit(request, pk):
	instance = get_object_or_404(Post, pk)
	form = CreatePostForm(request.POST or None)
	context = {'form':form}

	print(form)
	# print(form.cleaned_data)
	# data = form.save(submit=False)
	# if form.is_valid():
	# 	for key, value in form.cleaned_data.iteritems():
	# 		instance['key'] = value
	# 	form.save()
	# 	return HttpResponseRedirect('/post/' + str(request.pk))

	return render(request, 'post_edit.html', context)















	



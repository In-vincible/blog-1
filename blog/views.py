from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout


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

def post(request, slug):
	'''
	Article detail
	'''
	post = get_object_or_404(Post, slug=slug)
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
	page = About.objects.last()
	categories = Category.objects.all()
	context = {
		'post':page, 
		'categories':categories
	}
	return render(request, 'about.html', context)


def create(request):
	form = CreatePostForm(request.POST or None)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/')
	context = {'form': form}
	return render(request, 'post_create.html', context)

def edit(request, slug):
	if slug:
		instance = get_object_or_404(Post, slug=slug)
	else:
		instance = None

	if request.method == 'POST':
		form = CreatePostForm(request.POST, instance=instance)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/post/' + str(slug))
	form = CreatePostForm(instance=instance)
	
	context = {'form': form
	}
	return render(request, 'post_edit.html', context)


def sign_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/')

            # Redirect to a success page.
        else:
            return HttpResponseRedirect('/')
            
    else:
    	return HttpResponseRedirect('/')

def logout_view(request):
    logout(request)














	



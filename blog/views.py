from django.shortcuts import render
from django.utils import timezone
from .models import Post

from django.shortcuts import render, get_object_or_404
from .forms import PostForm, UserForm, CommentForm, EditProfileForm
from django.shortcuts import redirect

from .forms import User, Comment
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 

from django.contrib.auth.decorators import login_required




# Create your views here.

""" CATEGORY """
def category(request,category):
    posts = Post.objects.filter(category__slug=category).all()
    return render(request, 'blog/post_list.html', {'posts': posts})

""" TAG """
def tag(request,tag):
    posts = Post.objects.filter(tag__slug=tag).all()
    print(tag,"aaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

 
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_detail(request, slug):
    # get post object
    post = get_object_or_404(Post, slug=slug)
    # list of active parent comments
    comments = post.comments.filter(active=True, parent__isnull=True)
    if request.method == 'POST':
        # comment has been added
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            parent_obj = None
            # get parent comment id from hidden input
            try:
                # id integer e.g. 15
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            # if parent_id has been submitted get parent_obj id
            if parent_id:
                parent_obj = Comment.objects.get(id=parent_id)
                # if parent object exist
                if parent_obj:
                    # create replay comment object
                    replay_comment = comment_form.save(commit=False)
                    # assign parent_obj to replay comment
                    replay_comment.parent = parent_obj
            # normal comment
            # create comment object but do not save to database
            new_comment = comment_form.save(commit=False)
            # assign ship to the comment
            new_comment.post = post
            # save
            new_comment.save()
            return redirect("post_detail", slug=post.slug)
    else:
        comment_form = CommentForm()
    return render(request,
                  'blog/post_detail.html',
                  {'post': post,
                   'comment': comments,
                   'comment_form': comment_form})


def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.tag.set(form.cleaned_data.get('tag')) 
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def sign_up_request(request):
	if request.method == "POST":
		form = UserForm(request.POST, request.FILES)
		if form.is_valid():
			user = form.save()
			messages.success(request, "Registration successful." )
			return redirect('login')
		else:
			messages.error(request, "Unsuccessful registration. Invalid information.")
	else:
		form = UserForm()
	return render (request, "blog/sign_up.html", {'Sign_up_form':form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect('post_list')
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request, 'blog/login.html', {'login_form':form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("post_list")


@login_required
def profile(request):
    user = User.objects.filter(id=request.user.id).last()
    print(user, 'userrrr')
    return render(request, 'blog/profile.html', {'user': user})


@login_required    
def edit_profile(request):
	user = User.objects.filter(id=request.user.id).last()
	if request.method == "POST":
		form = EditProfileForm(request.POST,request.FILES, instance=user)
		if form.is_valid():
			form.save()
			messages.success(request, "Update successful." )
			return redirect('profile')
		else:
			messages.error(request, "Unsuccessful update. Invalid information.")
	else:
		form = EditProfileForm(instance=user)
	return render (request, "blog/edit_profile.html", {'form':form})



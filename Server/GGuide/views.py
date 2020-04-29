from django.contrib import messages
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django import forms
from django.views.generic.edit import ModelFormMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic import CreateView
from django.views.generic.edit import ModelFormMixin
from django.forms.widgets import HiddenInput
from django.shortcuts import get_object_or_404


from GGuide.models import SignUpForm, Userlogin, ProfileForm, ProfileModel, FriendForm, CommentsForm, Comments
from GGuide.models import Article


def index(request):
    ctx = {
        'articles':Article.objects.all(),
    }
    return render(request, 'index.html', context=ctx)


def articles(request):
    ctx = {
        'articles': Article.objects.all(),
    }
    return render(request, 'articles/articles.html', context=ctx)


class ArticleCreate(CreateView):
    class Meta:
        widgets = {
            'author': HiddenInput(),
        }
    ctx = {
        'articles': Article.objects.all(),

    }
    success_url = "/"
    template_name = "articles/create_article.html"
    model = Article
    fields = ['article_image', 'title', 'text']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super(ModelFormMixin, self).form_valid(form)




def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    success_url = "/"
    ctx = {
        'articles': Article.objects.all(),
        'article': article,
        'comments': article.comments.all(),
    }
    user = request.user
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('comment')
            comment_model = Comments(user=user, article=article, text=text)
            comment_model.save()

    return render(request, 'single-blog.html', ctx)


def game_views(request):
    ctx ={
        'articles': Article.objects.all(),
    }
    return render(request, 'game_index.html', ctx)


def blog_views(request):
    ctx = {
        'articles': Article.objects.all(),
    }
    return render(request, 'blog.html', context=ctx)


def cube_slam(request):
    return render(request, 'cube_slam.html', {})


def hexgl(request):
    return render(request, 'hexgl.html', {})


def gridgarden(request):
    return render(request, 'gridgarden.html', {})


def registration(request):
    success_url = "/"
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password, email=email)
            login(request, user)
            p = ProfileModel(img='default.jpg', user=user)
            p.save()

            return redirect(success_url)
    else:
        form = SignUpForm()
    ctx = {
        'articles': Article.objects.all(),
        'form': form,
    }
    return render(request, 'registration.html',ctx)


def logout(request, next_page='index'):

    return redirect(next_page)


def log_in(request):
    ctx = {
        'articles': Article.objects.all(),
    }
    success_url = "/"
    if request.method == 'POST':
        form = Userlogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect(success_url)
            else:
                return HttpResponse("Your account was inactive.")
    else:
        form = Userlogin()
    return render(request, 'log_in.html', ctx)


def article_image_form(request):
    ctx = {}
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.cleaned_data.get("form_article_image")
            form = Article(img=img)
            form.save()
    else:
        form = ArticleForm()
    ctx['form'] = form



def profile_user(request):
    ctx = {
        'articles': Article.objects.all(),
    }
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user  # user
            img = form.cleaned_data.get("Image") # user foto
            user.profilemodel.img = img
            user.profilemodel.save()
            print(user.profilemodel.img) # test
    else:
        form = ProfileForm()
    ctx['form'] = form
    return render(request, 'profile.html', ctx)


def change_info(request):
    ctx ={}
    success_url = "/"
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect(success_url)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    ctx['form'] = form
    return render(request, 'change_password.html', ctx)


def friend_list(request):
    ctx = {
        'friends' : request.user.profilemodel.friends.all(),
        'articles': Article.objects.all(),
    }


    return render(request, 'friend_list.html', ctx)


def add_friend(request):
    ctx = {
        'articles': Article.objects.all(),
    }
    if request.method == 'POST':
        form = FriendForm(request.POST)
        if form.is_valid():
            user = request.user
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            new_friend = User.objects.get(username=username, email=email)
            user.profilemodel.friends.add(new_friend)
            user.profilemodel.save()
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'add_friend.html', ctx)


def remove_friend(request):
    ctx = {
        'articles': Article.objects.all(),
    }
    if request.method == 'POST':
        form = FriendForm(request.POST)
        if form.is_valid():
            user = request.user
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            friend = User.objects.get(username=username, email=email)
            user.profilemodel.friends.remove(friend)
            user.profilemodel.save()
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'remove_friend.html', ctx)

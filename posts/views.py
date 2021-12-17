from django.core.exceptions import ObjectDoesNotExist
from django.db.models.query import QuerySet
from django.forms.models import modelformset_factory
from django.http import request
from django.http.request import QueryDict
from django.http.response import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.views.generic.base import View
from django.views import generic 
from django.views.generic import DetailView      
from .models import Post, Comments, PostImages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView,DetailView
from .forms import CommentForm, ImageForm, PostForm, ContactForm
from django.template import RequestContext
import random
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from mgn2.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL
from django.db.models import Count
from django.db.models import Q 

class PostsSearch(ListView):
    model = Post
    template_name = 'posts/posts.html'
    def get_queryset(self): # новый
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
            Q(title__icontains=query) | Q(text__icontains=query)
        )
        return object_list

class Posts(ListView):
    model = Post
    template_name = 'posts/posts.html'
    queryset = Post.objects.all()

def sort(request):
    posts=Post.objects.all().annotate(cnt=Count('comments')).order_by('-cnt')
    return render(request, 'posts/posts.html', {'object_list': posts},)

def sort_date(request):
    posts=Post.objects.order_by('-id')
    return render(request, 'posts/posts.html', {'object_list': posts},)

def post_new(request):
    ImageFormSet = modelformset_factory(PostImages,
                                        form=ImageForm, extra=5)
    if request.method == "POST":
        formPost = PostForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=PostImages.objects.none())
        if formPost.is_valid() and formset.is_valid():
            post = formPost.save(commit=False)
            post.user = request.user
            text= [random.choice('abc123') for _ in range(10)]
            post.url = ''.join(text)
            post.save()

            for form in formset.cleaned_data:
                if 'image' in form:
                    image = form['image']
                    photo = PostImages(post=post, image=image, title='1')
                    photo.save()
            messages.success(request,
                             "Yeeew, check it out on the home page!")
            return redirect('view_post', slug=post.url)
    else:
        formPost = PostForm()
        formset = ImageFormSet(queryset=PostImages.objects.none())
    return render(request, 'posts/post_new.html', {'form': formPost, 'formset': formset},)

class AddComment(View):
    def post(self, request, pk):
        form = CommentForm(request.POST)
        post = Post.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.post = post
            form.user = request.user
            form.name = request.user
            form.save()
        return redirect('view_post', slug=post.url)

class BlogUpdateView(UpdateView): 
    model = Post
    template_name = 'posts/post_edit.html'
    slug_field = "url"
    fields = ['title', 'text']

class PostDetailView(DetailView): 
    model = Post
    slug_field = "url"
    template_name = 'posts/view_post.html'

def index(request):
    return render(request, 'index.html',{})

def post_detail(request,id):
    return render(request, 'index.html',{})


def contact_view(request, slug):
    post = Post.objects.get(url=slug)
    user=post.user
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        # если метод POST, проверим форму и отправим письмо
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = user.email
            message = form.cleaned_data['message']
            try:
                send_mail(f'{subject} от {DEFAULT_FROM_EMAIL}', message,
                          DEFAULT_FROM_EMAIL, [email])
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return redirect('success')
    else:
        return HttpResponse('Неверный запрос.')
    return render(request, "email.html", {'form': form})

def success_view(request):
    return redirect('posts')

def delete(request, slug):
    try:
        post = Post.objects.get(url=slug)
        post.delete()
        return HttpResponseRedirect("/main")
    except post.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

def delete_comment(request, pk):
    try:
        comment = Comments.objects.get(id=pk)
        post = comment.post
        comment.delete()
        return redirect('view_post', slug=post.url)
    except comment.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")
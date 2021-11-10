from django.core.exceptions import ObjectDoesNotExist
from django.db.models.query import QuerySet
from django.forms.models import modelformset_factory
from django.http import request
from django.http.request import QueryDict
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.views.generic.base import View
from django.views import generic 
from django.views.generic import DetailView      
from .models import Post, Comments, PostImages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView,DetailView
from .forms import CommentForm, ImageForm, PostForm
from django.template import RequestContext
import random
from django.contrib import messages

class Posts(ListView):
    model = Post
    template_name = 'posts/posts.html'


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




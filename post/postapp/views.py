from django.shortcuts import render, redirect
from .models import Post, Images, Comm
from django.views.generic import DetailView,DeleteView
from django.forms import modelformset_factory
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from .forms import PostForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

def home(request):
    post = Post.objects.all().order_by("-posted_date")
    paginator = Paginator(post,10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    query = request.GET.get('q')
    if query:
        posts = post.filter(
            Q(title__icontains=query)
        )
    context = {
        'all_post':posts,
        

    }
    return render(request,'home.html',context)

def comments(request):
    comments = Comm.objects.all().order_by('-id')
    pagination = Paginator(comments,7)
    page = request.GET.get('page')
    comment = pagination.get_page(page)

    if request.method == 'POST':
        commentField = CommentForm(request.POST)
        if commentField.is_valid():
            cmt = commentField.save(commit=False)
            cmt.writer = request.user
            cmt.save()
            return redirect('/')   
    else:
        commentField = CommentForm()
    context = {
        'comment':comment,
        'field':commentField
    }
    return render(request,'coment.html',context)

class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'    

class PostDelteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    template_name = 'post_confirm_delete.html'       


def post(request):
    ImageFormSet = modelformset_factory(Images,fields=['image'],labels={'image':'suratlar'} , extra=4)
    if request.method == 'POST':
        form = PostForm(request.POST)
        imgForm = ImageFormSet(request.POST or None,request.FILES or None)
        if form.is_valid() and imgForm.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            for formImg in imgForm.cleaned_data:
                if 'image' in formImg:
                    image = formImg['image']
                    photo = Images(post=post, image=image)
                    photo.save()
            return redirect('home')    
    else:
        form = PostForm()
        imgForm = ImageFormSet(queryset=Images.objects.none())
    context = {
        'form':form,
        'imgForm':imgForm
    }    
    return render(request,'index.html',context)

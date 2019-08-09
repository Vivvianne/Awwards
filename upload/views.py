from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comments
from django.contrib.auth import authenticate, login, logout
from .forms import PostCreateForm, CommentsForm
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    # PostCommentView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .serializer import MerchSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  VotesMerch
from rest_framework import status
from .permissions import IsAdminOrReadOnly

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'upload/home.html', context)


# @login_required(login_url='/login/')
# def add_comment(request,post_id):
#     post = get_object_or_404(Post, pk=post_id)
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.user = request.user

#             comment.post = post
#             comment.save()
#     return redirect('home')


class PostListView(ListView):
    model = Post
    template_name = 'upload/home.html'
    context_object_name = 'posts'
    ordering =['-date_posted']
    paginate_by = 3
    
class UserPostListView(ListView):
    model = Post
    template_name = 'upload/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 3
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
        
    
    
def post_detail(request, pk):
    object = Post.objects.filter(id = pk).first()
    print(object.title)
    comments = Comments.objects.all()
    print(comments)
    current_user = request.user
    if request.method =='POST':
            form = CommentsForm(request.POST, request.FILES)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.commentor = request.user
                comment.post = object
                comment.save()
                return redirect('post-detail', pk)
    else:
            form = CommentsForm()
    
    
    context = {
        "object":object,
        "form":form,
        "comments":comments
    }
    return render (request, "upload/post_detail.html", context)
    # template_name = 'upload/post_details.html'
    
    
# class PostCreateView(LoginRequiredMixin, CreateView):
#     model = Post
#     fields = ['title', 'image', 'description', 'link']
    
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
    
    
def post_save(request):
    if request.method =='POST':
    # u_form = UserUpdateForm(request.POST, instance=request.user)
        a_form = PostCreateForm(request.POST, request.FILES)
        if a_form.is_valid():
            image = a_form.save(commit=False)
            image.author = request.user
            # u_form.save()
            image.save()
            return redirect('upload-home')
    else:
        a_form = PostCreateForm()
    return render(request,'upload/post_form.html',{'form':a_form})
    
    
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'image', 'description', 'link']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user ==post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user ==post.author:
            return True
        return False


@login_required(login_url='/login/')
def comment(request, id):
    posts = Post.objects.get(pk=id)
    current_user = request.user
    if request.method =='POST':
            form = CommentsForm(request.POST, request.FILES)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.commentor = request.user
                comment.post = posts
                comment.save()
                return redirect('upload/home.html', post_id = id)
    else:
            form = CommentsForm()
    return render(request,'post-detail',{'form':form})
    



@login_required(login_url='/login/')
def search_results(request):
    
    if 'posts' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Post.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'upload/search.html',{"message":message,"posts": searched_posts})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})
    
    
class MerchList(APIView):
    def get(self, request, format=None):
        all_merch = VotesMerch.objects.all()
        serializers = MerchSerializer(all_merch, many=True)
        return Response(serializers.data)
    
    def post(self, request, format=None):
        serializers = MerchSerializer(data=request.data)
        permission_classes = (IsAdminOrReadOnly,)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

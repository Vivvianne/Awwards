from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostCreateForm
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'upload/home.html', context)


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
        
    
    
class PostDetailView(DetailView):
    model = Post
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




def search_results(request):
    
    if 'posts' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Post.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'upload/search.html',{"message":message,"posts": searched_posts})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})

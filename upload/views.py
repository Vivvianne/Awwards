from django.shortcuts import render
from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
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
    
    
class PostDetailView(DetailView):
    model = Post
    # template_name = 'upload/post_details.html'
    
    
class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'image', 'description', 'link']
    




def search_results(request):
    
    if 'posts' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Post.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'upload/search.html',{"message":message,"posts": searched_posts})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})

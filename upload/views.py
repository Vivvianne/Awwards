from django.shortcuts import render


posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'decription': 'First post content',
        'link': 'Project1',
        'date_posted': 'August 27, 2018',
        'comments':'others comments'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'decription': 'First post content',
        'link': 'Project1',
        'date_posted': 'August 28, 2018',
        'comments':'other-peoples comments'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'upload/home.html', context)

def about(request):
    return render(request, 'upload/about.html')
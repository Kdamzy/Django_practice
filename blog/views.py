from django.shortcuts import render

posts = [
    {
        'Author': 'Kehinde',
        'Title': 'Blog post',
        'Content': 'first content',
        'timestamp': 'January 27, 2024'
    },
    {
        'commenter name': 'damzy',
        'Title': 'comment',
        'Comment': 'first comment',
        'timestamp': 'January 27, 2024'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
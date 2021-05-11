from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.http import HttpResponse

# from django.views.generic.edit import DeleteView
# from django.urls import reverse_lazy

# class PostDeleteView(DeleteView):
#     model = Post
#     success_url = reverse_lazy('post:post_list')
def post_delete(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.delete()
        return render(request, 'post/post_delete.html')

    elif request.method == 'GET':
        return HttpResponse('잘못된 접근 입니다.')

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'post/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post:post_detail', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'post/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'post/post_edit.html', {'form': form})

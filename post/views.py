from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.core.paginator import Paginator

from .models import Post, Answer, Comment
from .forms import PostForm, AnswerForm
from django.http import HttpResponse

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.user != post.author:
        return render(request, 'post/post_not_allowed.html')

    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.delete()
        return render(request, 'post/post_delete.html')

    elif request.method == 'GET':
        return HttpResponse('잘못된 접근 입니다.')

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'post/post_list.html', {'posts': posts})

def post_list_staff(request):
    all_posts = Post.objects.all().order_by('-published_date')
    page = int(request.GET.get('p', 1))
    paginator = Paginator(all_posts, 7)
    posts = paginator.get_page(page)
    return render(request, 'post/post_list_staff.html', {'posts': posts})

# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'post/post_detail.html', {'post': post})

def post_detail(request, pk):
    post_detail = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=pk)
    if request.method == "POST":
        comment = Comment()
        comment.post = post_detail
        comment.body = request.POST['body']
        comment.date = timezone.now()
        comment.save()
    return render(request, 'post/post_detail.html', {'post': post_detail, 'comments': comments})


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

    if request.user != post.author:
        return render(request, 'post/post_not_allowed.html')

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

def answer_list(request):
    answers = Answer.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'post/answer_list.html', {'answers': answers})

def answer_list_staff(request):
    answers = Answer.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'post/answer_list_staff.html', {'answers': answers})

@login_required
@permission_required('post.can_answer', login_url=reverse_lazy('post:post_not_allowed'))
def answer(request):
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.published_date = timezone.now()
            answer.save()
            return redirect('post:answer_list')
    else:
        form = AnswerForm()

    return render(request, 'post/answer.html', {'form': form})

def post_not_allowed(request):
    return render(request, 'post/post_not_allowed.html')

def answer_detail(request, pk):
    answer = get_object_or_404(Answer, pk=pk)
    return render(request, 'post/answer_detail.html', {'answer': answer})

def answer_edit(request, pk):
    answer = get_object_or_404(Answer, pk=pk)

    if request.user != answer.author:
        return render(request, 'post/post_not_allowed.html')

    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.published_date = timezone.now()
            answer.save()
            return redirect('post:answer_detail', pk=answer.pk)
    else:
        form = AnswerForm(instance=answer)

    return render(request, 'post/answer_edit.html', {'form': form})

def answer_delete(request, pk):
    answer = get_object_or_404(Answer, pk=pk)

    if request.user != answer.author:
        return render(request, 'post/post_not_allowed.html')

    if request.method == 'POST':
        answer = Answer.objects.get(pk=pk)
        answer.delete()
        return render(request, 'post/answer_delete.html')

    elif request.method == 'GET':
        return HttpResponse('잘못된 접근 입니다.')

def post_detail_staff(request, pk):
    post_detail = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=pk)
    if request.method == "POST":
        comment = Comment()
        comment.post = post_detail
        comment.body = request.POST['body']
        comment.date = timezone.now()
        comment.save()
    return render(request, 'post/post_detail_staff.html', {'post': post_detail, 'comments': comments})

def post_list(request):
    if not request.user.is_authenticated:
        return render(request, 'post/post_must_login.html')
    else:
        all_posts = Post.objects.all().order_by('-published_date')
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        page = int(request.GET.get('p', 1))
        paginator = Paginator(all_posts, 7)
        posts = paginator.get_page(page)
        return render(request, 'post/post_list.html', {'posts': posts})
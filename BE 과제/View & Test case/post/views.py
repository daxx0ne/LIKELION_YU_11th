from django.core.paginator import Paginator
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Blog
from .forms import PostForm


def home(request):
    posts = Post.objects.filter().order_by('-created_at')
    paginator = Paginator(posts, 5)
    page_num = request.GET.get('page')
    posts = paginator.get_page(page_num)
    return render(request, 'index.html', {'posts': posts})


# 게시글 생성
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.blog = Blog.objects.get(author=request.user)
            post.save()
            form.save_m2m()  # Save many-to-many relationships
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_create.html', {'form': form})


# 게시글 리스트 조회
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})


# 게시글 하나만 조회
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})


# 게시글 업데이트
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()  # 폼으로부터 게시글 업데이트
            return redirect('post_detail', pk=post.pk)  # 업데이트된 게시글의 상세 페이지로 리디렉션
    else:
        form = PostForm(instance=post)
    return render(request, 'post_update.html', {'form': form, 'post': post})


# 게시글 삭제
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()  # 게시글 삭제
        messages.success(request, '게시글이 삭제되었습니다.')
        return redirect('post_list')  # 게시글 목록 페이지로 리디렉션
    else:
        messages.error(request, '잘못된 요청입니다.')
        return redirect('post_detail', pk=post.pk)  # 게시글 상세 페이지로 리디렉션

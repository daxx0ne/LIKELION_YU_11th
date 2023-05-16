from django.core.validators import MaxValueValidator
from django.db import models
from django.contrib.auth.models import User


# 블로그의 정보를 나타내는 모델
class Blog(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    available_blogs = models.PositiveIntegerField(validators=[MaxValueValidator(3)])

    def __str__(self):
        return self.name


# 게시글의 정보를 나타내는 모델
class Post(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# 댓글의 정보를 나타내는 모델
class Comment(models.Model):
    comment = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment


# 태그의 정보를 나타내는 모델
class Tag(models.Model):
    tag = models.CharField(max_length=10)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.tag


# 카테고리의 정보를 나타내는 모델
class Category(models.Model):
    category = models.CharField(max_length=20)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.category


# 게시글 공감에 대한 정보를 나타내는 모델
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} likes {self.post}"


# 블로그 구독에 대한 정보를 나타내는 모델
class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} subscribed to {self.blog.title}"


# Post와 Tag 모델을 Many-to-Many 관계로 연결하는 역할을 하는 모델 (중재 테이블)
class PostTag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f"Post: {self.post} | Tag: {self.tag}"
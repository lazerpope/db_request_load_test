from django.db import models

class PostManager(models.Manager):
    def get_posts_with_comments(self):
        return self.get_queryset().all().prefetch_related('comments')


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    objects = PostManager()
    
    def test_get_comments(self):
        return Comment.objects.filter(post=self)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE , related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


   
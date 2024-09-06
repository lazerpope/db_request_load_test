from django import template
from ..models import Post

register = template.Library()

@register.simple_tag
def get_all_posts():
    return Post.objects.all()



@register.simple_tag
def get_all_posts_with_comments():
    return Post.objects.all().prefetch_related('comments')



@register.simple_tag
def get_all_posts_with_comments_2():
    return Post.objects.get_posts_with_comments()
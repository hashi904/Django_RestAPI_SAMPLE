from django.db import models
from accounts.models import User

class Blog(models.Model):
    title = models.CharField(max_length=128)
    # 文字数制限しない
    article = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #外部キー　user.blogsで呼び出し
    user = models.ForeignKey(User, related_name='blogs', on_delete=models.CASCADE)
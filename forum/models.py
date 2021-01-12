from django.db import models

from django.urls import reverse

from django.contrib.auth.models import User

from django.utils.text import slugify

# Create your models here.

class Forum(models.Model):

    title = models.CharField(verbose_name="TITLE", max_length=100)
    slug = models.SlugField(verbose_name="SLUG", max_length=100, allow_unicode=True, help_text="one word for title alias") # this is title -> this-is-title
    addr = models.CharField(verbose_name="ADDRESS", max_length=1000)
    addr_detail = models.CharField(verbose_name="ADDRESS DETAIL", max_length=200, blank=True)
    description = models.CharField(verbose_name="DESCRIPTION", max_length=2000)
    create_dt = models.DateTimeField(verbose_name="CREATE DATE", auto_now_add=True)
    modify_dt = models.DateTimeField(verbose_name="MODIFY DATE", auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name="OWNER")

    class Meta:
        verbose_name = 'forum'
        verbose_name_plural = 'forums'
        db_table = 'forum'
        ordering = ('-modify_dt',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("forum:forum_detail", args=(self.slug,)) # /blog/this-is-title

    def get_previous(self): # 이전 글 가져오기
        return self.get_previous_by_modify_dt()

    def get_next(self): # 다음 글 가져오기
        return self.get_next_by_modify_dt()

    # 상속 받은 메서드 재정의
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)
    
from django.shortcuts import render
from django.views.generic import ListView
from forum.models import Forum

# Create your views here.

class ForumLV(ListView):
    # 목록을 조회해서 
    model = Forum # Post.objects.all()
    # 템플릿(default : blog/post_list.html)에 데이터(default: object_list) 전달
    template_name = "forum/forum_all.html"
    context_object_name = "forums"
    paginate_by = 2 # 페이징 처리 설정 (한 화면에 2개씩 표시)
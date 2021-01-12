from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, DeleteView, UpdateView
from forum.models import Forum
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from saferestaurant.views import OwnerOnlyMixin

# Create your views here.

class ForumLV(ListView):
    # 목록을 조회해서 
    model = Forum # Post.objects.all()
    # 템플릿(default : blog/post_list.html)에 데이터(default: object_list) 전달
    template_name = "forum/forum_all.html"
    context_object_name = "forums"
    paginate_by = 3 # 페이징 처리 설정 (한 화면에 2개씩 표시)

class ForumDV(DetailView):
    model = Forum 

class ForumCreateView(LoginRequiredMixin, CreateView):
    model = Forum
    # fields = ['title', 'slug', 'description', 'content', 'tags']
    fields = ['title', 'slug', 'addr', 'addr_detail', 'description']
    initial = {'slug': 'auto-filling-do-not-input'} 
    #fields = ['title', 'description', 'content', 'tags'] 
    success_url = reverse_lazy('forum:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ForumChangeLV(LoginRequiredMixin, ListView):
    template_name = 'forum/forum_change_list.html'

    def get_queryset(self):
        return Forum.objects.filter(owner=self.request.user)

class ForumDeleteView(OwnerOnlyMixin, DeleteView) :
    model = Forum
    success_url = reverse_lazy('forum:index')

class ForumUpdateView(OwnerOnlyMixin, UpdateView):
    model = Forum
    # fields = ['title', 'slug', 'description', 'content', 'tags']
    fields = ['title', 'slug', 'addr','addr_detail','description']
    success_url = reverse_lazy('forum:index')

    
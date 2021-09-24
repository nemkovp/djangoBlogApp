from django.views import generic
from .models import *

class PostList(generic.ListView):
    queryset = Post.objects.order_by('datas')
    template_name = 'post_list.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView, UpdateView, ListView
from .models import ForumPost, Reply

# dashboard view from .models
def forum_view(request):
    forumposts = ForumPost.objects.all()
    replies = Reply.objects.all()
    return render(request, 'forum.html', {'forumposts': forumposts, 'replies': replies})
    

class ForumPostDetailView(DetailView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['replies'] = Reply.objects.all()
        return context
    
    model = ForumPost
    template_name = "forumpost-details.html"

class ForumPostCreateView(CreateView):
    model = ForumPost
    template_name = "forumpost-add.html"
    fields = "__all__"

class ForumPostUpdateView(UpdateView):
    model = ForumPost
    template_name = "forumpost-edit.html"
    fields = "__all__"



    




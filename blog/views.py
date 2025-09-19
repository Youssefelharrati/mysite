from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Post, Comment
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import PostForm, CommentForm
from django.views.generic import(
    TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
)

# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    login_url = '/login/'

    def get_success_url(self):
      return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})

    
    

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm    


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')


class DraftListView(LoginRequiredMixin, ListView):
    model = Post
    login_url = '/login/'  # or use settings.LOGIN_URL
    template_name = 'blog/post_draft_list.html'  # uncomment and correct
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')


    

#######################################
#######################################

@login_required
def pub_post(request, pk):

    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)





@login_required
def add_comment(request, pk):

    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk= post.pk)
        
    else:
        form = CommentForm()

    return render(request, 'blog/comment_form.html', {'form':form})    


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk= comment.post.pk)


@login_required
def remove_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_id = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk= post_id)

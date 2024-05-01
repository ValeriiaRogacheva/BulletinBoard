from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm, CommentForm

# Создаем свой класс, который наследуется от ListView.
class PostsList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Post
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'flatpages/post.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'posts'
    ordering = '-dateCreation'
    paginate_by = 5

# Создаем свой класс, который наследуется от DetailView.
class PostDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельной новости
    model = Post
    # Используем другой шаблон html
    template_name = 'flatpages/post_detail.html'
    # Название объекта, в котором будет выбранная пользователем новость
    context_object_name = 'post'


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'flatpages/post_create.html'
    permission_required = ('post.add_post',)


    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        #send_email_task.delay(post.pk)
        return super().form_valid(form)


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'flatpages/post_create.html'
    context_object_name = 'edit'


class PostDelete(DeleteView):
    model = Post
    template_name = 'flatpages/post_delete.html'
    context_object_name = 'delete'

class CommentCreate(LoginRequiredMixin, CreateView):
    permission_required = ('comment.add_comment',)
    form_class = CommentForm
    model = Comment
    template_name = 'flatpages/comment_create.html'
    context_object_name = 'comments'

from django.shortcuts import render
from django.views.generic import ListView,DetailView
#from django.shortcuts import get_object_or_404
from .models import Article, Category


from django.http import HttpResponse
# Create your views here.


class BlogListView(ListView):
    template_name = 'blog_list.html'
    context_object_name ='blog_list'


    def get_queryset(self):
        if 'tag_slug' in self.kwargs:
            self.tag_slug = self.kwargs['tag_slug']
            return Article.objects.filter(tag__slug__in=[self.tag_slug])
        elif 'category_slug' in self.kwargs:
            self.category_slug = self.kwargs['category_slug']
            return Article.objects.filter(category__slug__in =[self.category_slug])
        else:
            return Article.objects.order_by('-create_time')

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)

        context['category_list'] = Category.objects.all()
        context['tag_list'] = Article.tag.most_common()
        return context

class BlogListPageView(BlogListView):
    template_name = 'blog_list_page.html'
    context_object_name = 'blog_list_page'
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super(BlogListPageView, self).get_context_data(**kwargs)
        if 'tag_slug' in self.kwargs:
            context['url_data'] = self.kwargs['tag_slug']
            context['url_type'] = 'tag'
        elif 'category_slug' in self.kwargs:
            context['url_type'] = 'category'
            context['url_data'] = self.kwargs['category_slug']
        else:
            context['url_type'] = 'home'
            context['url_data'] = 1
        return context


class TagListView(ListView):
    template_name = 'tag_list.html'
    context_object_name = 'tag_list'

    def get_queryset(self):
        return Article.tag.most_common()

    def get_context_data(self, **kwargs):
        context = super(TagListView,self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context


class CategoryListView(ListView):
    template_name = 'category_list.html'
    context_object_name = 'category_list'
    model = Category

    def get_context_data(self, **kwargs):
        context =super(CategoryListView, self).get_context_data(**kwargs)
        context['tag_list'] = Article.tag.most_common()
        return context


class BlogDetailView(DetailView):
    template_name = 'blog_detail.html'
    context_object_name = 'blog_detail'
    model = Article

    def get_object(self,queryset=None):
        obj = super(BlogDetailView,self).get_object()
        obj.access_count +=1
        obj.save()
        return obj

    def get_context_data(self, **kwargs):
        context =super(BlogDetailView, self).get_context_data(**kwargs)
        context['tag_list'] = Article.tag.most_common()
        context['category_list'] =Category.objects.all()
        return context

def home(request):
    return render(request, 'blog/home.html')

from django.shortcuts import render, redirect
from django.views import View
from .models import *

def BlogView(request, blogid):
    blog = Blog.objects.get(id=blogid)
    
    # Pass the blog object to the template
    return render(request, 'blog/blog.html', {'blog': blog})

# Create your views here.
class AddBlog(View):
    def get(self, request):
        tags = Tag.objects.all()
        return render(request, 'blog/add_blog.html', {'tags':tags})
    
    def post(self, request):
        title = request.POST.get('title')
        summary = request.POST.get('summary')
        body = request.POST.get('body')
        thumbnail = request.FILES.get('thumbnail')
        
        selected_tag_ids = request.POST.getlist('tags')
        
        custom_tags = request.POST.get('custom_tags', '').split(',')
        
        blog = Blog.objects.create(
            title=title,
            summary=summary,
            body=body,
            thumbnail=thumbnail,
        )
        
        all_tag_ids = set(selected_tag_ids)
        for custom_tag in custom_tags:
            custom_tag = custom_tag.strip()
            if custom_tag:
                tag, created = Tag.objects.get_or_create(name=custom_tag)
                all_tag_ids.add(tag.id)
        
        blog.tags.set(all_tag_ids)
        blog.save()
        
        return redirect('home')

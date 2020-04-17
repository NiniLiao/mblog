from django.template.loader import get_template
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Post

# Create your views here.
def homepage (request):
    templates = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = templates.render(locals())
    # post_lists = list()
    # for count, post in enumerate(posts):
    #     post_lists.append("No.{}:".format(str(count)) + str(post)+"<br>")
    #     post_lists.append("<small>" + str(post.body.encode('utf-8'))+"</small><br><br>")
    # return HttpResponse(post_lists)
    return HttpResponse(html)
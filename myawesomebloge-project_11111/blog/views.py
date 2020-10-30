from django.shortcuts import render, get_object_or_404
from . models import Post
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.


def showblog(request):
    posts = Post.objects
    return render(request, 'blog/blog.html', {'posts': posts})

# def specific_post(request,post_id):
#     post = get_object_or_404(Post,pk =post_id)
#     return render(request,'blog/specific_post.html',{'post':post})


def specific_post(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
        return render(request, 'blog/specific_post.html', {'post': post})
    except:
        return render(request, 'blog/404_pg.html')


# def AddData(request):
#     return render(request, 'blog/add_date.html')


def add_post(request):
    if request.method != "POST":
        return HttpResponse("<h2>method not allowed</h2>")
    else:
        file = request.FILES['image']
        fs = FileSystemStorage()
        profile_img = fs.save(file.name, file)
        student = Post(title=request.POST.get('title', ''),
                       text=request.POST.get('text', ''), image=profile_img)
        student.save()
        return HttpResponseRedirect('/show_all_data')


def show_all_data(request):
    all_posts = Post.objects.all()
    return render(request, 'blog/add_date.html', {"post": all_posts})


def del_news(request, post_id):
    post = Post.objects.get(id = post_id)
    post.delete()
    return HttpResponseRedirect("/show_all_data")


def update_news(request, post_id):
    post = Post.objects.get(id=post_id)
    if post == None:
        return HttpResponse("Post not found")
    else:
        return render(request, 'blog/post_edit.html', {'post': post})


def edit_news(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method not allowed</h2>")
    else:
        post = Post.objects.get(id=request.POST.get('id',''))
        if post == None:
            return HttpResponse("<h2>Post Not Found</h2>")
        else:
            if request.FILES.get('image') != None:
                file = request.FILES['image']
                fs = FileSystemStorage()
                profile_img = fs.save(file.name, file)
            else:
                profile_img = None

            if profile_img != None:
                post.image = profile_img
            post.title = request.POST.get('title','')
            post.text = request.POST.get('text','')
            post.save()
            return HttpResponseRedirect("update_news/"+str(post.id))

from django.shortcuts import render, get_object_or_404, redirect
from .models import Notice, Qna
from django.contrib.auth.models import User
from django.contrib import auth
from django.utils import timezone

# Create your views here.

def home(request):
    return render(request, 'homepage/home.html')

def about(request):
    return render(request, 'homepage/about.html')

def map(request):
    return render(request, 'homepage/map.html')

def collection(request):
    return render(request, 'homepage/collection.html')

def notice(request):
    notices = Notice.objects.all()
    return render(request, 'homepage/notice.html', {'notices':notices})
def OUTER(request):
    return render(request, 'homepage/OUTER.html')
def SHOES(request):
    return render(request, 'homepage/SHOES.html')
def BOTTOM(request):
    return render(request, 'homepage/BOTTOM.html')
def top(request):
    return render(request, 'homepage/top.html')
def ACC(request):
    return render(request, 'homepage/ACC.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'homepage/login.html', {'error':'ID or password is incorrect'})
    else:
        return render(request, 'homepage/login.html')
    return render(request, 'homepage/login.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username = request.POST['username'], password = request.POST['password1'])
            auth.login(request, user)
            return redirect('home')
    return render(request, 'homepage/signup.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def detail(request, notice_id):
    notice_detail = get_object_or_404(Notice, pk=notice_id)
    return render(request, 'homepage/detail.html', {'notice': notice_detail})

def comment_new(request, pk):
    post = get_object_or_404(Notice, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment.save()
            return redirect('detail', post.pk)
    else:
        form = CommentForm()
    return render(request, 'homepage/comment_new.html', {'form': form})

def comment_remove(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirecct('detail', post_id=comment.post.pk)

def qna(request):
    questions = Qna.objects.all()
    return render(request, 'homepage/qna.html', {'questions':questions})

def detail2(request, qna_id2):
    qna_detail = get_object_or_404(Qna, pk=qna_id)
    return render(request, 'homepage/detail2.html', {'qna': qna_detail})

def new(request):
    return render(request, 'homepage/new.html')

def create(request):
    blog = Qna()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()

    return redirect('/qna/')

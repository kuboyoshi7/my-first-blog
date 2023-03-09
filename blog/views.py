from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import PostForm
from .models import Post

# Create your views here.
def post_list(request): # request:ネットでユーザから受け取った全ての情報が詰まったもの
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):
    if request.method == "POST": # <form method="POST" ...なのでPOSTならformの内容が送信されたとうこと
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else: # 最初のｱｸｾｽ時は通常のWEBｻｲﾄｱｸｾｽなのでGETがrequestに入る。
        form = PostForm() 
    return render(request, 'blog/post_edit.html', {'form':form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

'''
def post_new(request):
私たちの ビュー では、扱わなくてはならない２つの別々のシチュエーションがあります: 
１つ目は、最初にページにアクセスしてきた時で空白のフォームが必要な場合。２つ目は
すべてのフォームデータが入力された状態でビューに戻ってくる場合です。 
したがって条件分岐を追加する必要があります（そのためにifを使います）：

基本的にここでは2つのことを行います。まず form.save でフォームを保存することと author を
追加することです (PostForm 内に author フィールドがありませんし、このフィールドは必須です) 。
commit=False は Post モデルをまだ保存しないという意味です。保存前に author を追加したいので。 ほとんどの場合、commit=Falseなしでform.save()を使用しますが、この場合はそれを指定する必要があります。 post.save()は変更を保存し（作成者を追加しつつ）、新しいブログ投稿が作成されます！

https://tutorial.djangogirls.org/ja/django_forms/

アクセス詳細
１回目も２回目も同じ'post/new/'にアクセスするが、requestに入っている情報が、１回目はGET、２回目はPOSTになる。
１回目 base.html内<a href="{% url 'post_new' %}"をClick -> 'post/new/'にアクセス。その際次のＰＧが作動。
       urls.py -> views.py -> def post_new(request) -> if request.method == "POST": False -> else

２回目 'post/new/'のページにいる状態 -> ボタンを押す -> 再び'post/new/'にアクセス

'''

from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','text',)

'''
PostFormとは何かと思うかもしれませんが、これはフォームの名前です。 このフォームが 
ModelForm の一種だとDjangoに伝える必要があります (Djangoが私たちのためにいくつか魔法を
かけられるように)。forms.ModelFormがその役割を果たします。
次にclass Metaですが、ここでDjangoにフォームを作るときにどのモデルを使えばいいか (model = Post) を伝えます。
最後にフォームのフィールドに何を置くか書きます。 ここでは、私たちはtitle（タイトル）と text（本文）のみをフ
ォームで使用します。 author は現在ログインしている人（あなた）です。 created_date は
（コードによって）自動的に記事を書いた日時が設定されます。
'''

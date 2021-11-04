from django.shortcuts import render, redirect
from article.forms import ArticleDescription
from article.models import Article


# Create your views here.
def create(request):
    if request.method == "POST":
        article_form = ArticleDescription(request.POST,request.FILES)
        if article_form.is_valid():
            cd= article_form.cleaned_data
            new_article = Article(title=cd['title'],
                                short_description= cd['short_description'],
                                description= cd['description'],
                                image=request.FILES['image'])
            article_form.save()
            return redirect('about')
    else:
        article_form = ArticleDescription()
    return render (request, 'article-create.html', {'article_form':article_form})

def article_list(request):
    articles= Article.objects.all()
    return render (request,'article.html',{'articles':articles})

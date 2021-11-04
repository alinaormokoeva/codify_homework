from django import forms
from article.models import Article

class ArticleDescription(forms.ModelForm):
    class  Meta:
        model = Article
        fields = ['title','short_description','description','image']
        # fields = '__all__'
        exclude = ('created_date','updated_date')

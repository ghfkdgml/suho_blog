from django import forms
from .models import Article
from django import forms

class ArticleForm(forms.Form):
    # class Meta:
    #     model=Article
    #     fields=("title","content","category",)
    DEVELOPMENT="dv"
    PERSONAL="ps"
    ETC="etc"
    CATEGORY_CHOICES=(
        (DEVELOPMENT,"development"),
        (PERSONAL,"personal"),
        (ETC,"etc")
        )
    #     widgets={
    #         "title":forms.TextInput(attrs={"class":"form-control"}),
    #         "content":forms.TextInput(attrs={"class":"form-control"}),
    #         "category":forms.MultipleChoiceField(
    #             attrs={"class":"form-control"},
    #
    #         ),
    #     }
    title=forms.CharField(max_length=100,required=True)
    content=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    category=forms.MultipleChoiceField(
        choices=CATEGORY_CHOICES,
        # defaults=DEVELOPMENT,
        initial=CATEGORY_CHOICES[0],
        )

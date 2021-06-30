from django import forms
from .models import BidCrawling


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = BidCrawling
        fields = ['title', 'writer', 'bid', 'isbn']


class BookUpdateForm(forms.ModelForm):
    class Meta:
        model = BidCrawling
        fields = ['title', 'writer', 'bid', 'isbn', 'intro']


# class WriterUpdateForm(forms.ModelForm):
#     class Meta:
#         model = WriterInfo
#         fields = ['name', 'booktitle']


def bid_validator(value):
    if type(value) != int:
        raise forms.ValidationError(message='숫자를 입력해주세요')
    if value == None:
        raise forms.ValidationError(message='bid를 입력해주세요')


class bookForm(forms.Form):
    title = forms.CharField(label='title', max_length=100)
    writer = forms.CharField(label='writer', max_length=100)
    bid = forms.IntegerField(label='bid')
    isbn = forms.CharField(label='isbn', max_length=100)

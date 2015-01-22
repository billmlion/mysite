# -*- coding: utf-8 -*-
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.forms.extras.widgets import Select
from books.models import *
from django.forms import ModelForm
from django.core.exceptions import NON_FIELD_ERRORS



BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')
FAVORITE_COLORS_CHOICES = (('blue', 'Blue'),
                            ('green', 'Green'),
                            ('black', 'Black'))
MONTHS = {
    1:('jan'), 2:('feb'), 3:('mar'), 4:('apr'),
    5:('may'), 6:('jun'), 7:('jul'), 8:('aug'),
    9:('sep'), 10:('oct'), 11:('nov'), 12:('dec')
}
 
YEAR_IN_SCHOOL_CHOICES = (
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
) 

class ContactForm(forms.Form):
   subject = forms.CharField(required=False, max_length=5, help_text='100 characters max.')
   email = forms.EmailField(error_messages={'required': '你这个无名人士.....'},help_text="请输入邮件格式")
   message = forms.CharField()
   # contactType = forms.CharField(widget=SelectDateWidget(years=BIRTH_YEAR_CHOICES))
   contactDay = forms.CharField(widget=SelectDateWidget(years=BIRTH_YEAR_CHOICES,months=MONTHS))
   contactTime = forms.TimeField()
   contactTpye = forms.ChoiceField(choices=YEAR_IN_SCHOOL_CHOICES)
   webUrl = forms.URLField()

   def clean_message(self):
       message = self.cleaned_data['message']
       num_words = len(message.split())
       if num_words < 4:
           raise forms.ValidationError("请输入超过4个字符")
       return message 



class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'email']

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'authors','publisher','publication_date']



class ArticleForm(ModelForm):
    class Meta:
    	model = Article
        fields = ['headline', 'content']
        # error_messages = {
        #     NON_FIELD_ERRORS: {
        #         'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
        #     }
        # }        

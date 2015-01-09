from django.shortcuts import render_to_response
from django.http import HttpResponse
from books.models import Book
from django.core.mail import send_mail
from books.forms import ContactForm
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt



def UploadImage(request):
    '''UploadImage function do not work!!!'''
    if request.method == 'POST':
        content = request.FILES['ImageField']
        try:
            img = Image.open(content)
            img.thumbnail((500,500),Image.ANTIALIAS)
            img.save("abv.png","jpg")
        except Exception,e:
            return HttpResponse("Error %s"%e)
        return HttpResponse("ok")
    return HttpResponse("error")


def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render_to_response('search_results.html',
        {'books': books, 'query': q})
    else:
        return render_to_response('search_form.html', {'error': True})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
           cd = form.cleaned_data
           # send_mail(
           #  cd['subject'],
           #  cd['message'],
           #  cd.get('email', 'noreply@example.com'),
           #  ['siteowner@example.com'],
           # )
           return HttpResponseRedirect("/books")
        else:
            return render_to_response('contact_form.html', {'form': form},context_instance=RequestContext(request))
    else:
        form = ContactForm(initial={'subject': 'I love your site!'})
        return render_to_response('contact_form.html', {'form': form},context_instance=RequestContext(request))


@login_required
def getBooks(request):
    # if not request.user.is_authenticated():
    #       return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
    books = Book.objects.all()
    return render_to_response('book_list.html',{"book_list":books},context_instance=RequestContext(request))
    # return render_to_response('book_list.html',{"book_list":books})




def register(request):
    '''user register'''
    if request.method == 'POST':
      form = UserCreationForm(request.POST)
      if form.is_valid():
        new_user = form.save()
        return HttpResponseRedirect("/books")
    else:
      form = UserCreationForm()
    return render_to_response("registration/register.html", {'form': form},context_instance=RequestContext(request))


def logout_view(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/accounts/login/")

@csrf_exempt
def login_view(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username,password=password)
    if user is not None and user.is_active:
      auth.login(request, user)
      return  HttpResponseRedirect("/books")
    else:
      return HttpResponseRedirect("/accounts/login/")




from django.shortcuts import render
import random

def home(request):
    lst=list(range(6,15))
    print(lst)
    return render(request,"gena/home.html",{'lst':lst})

def password(request):
    psw = ""
    char = [chr(i) for i in range (97,123)]

    if request.GET.get('uppercase'):
        char.extend([chr(i) for i in range(65,91)])

    if request.GET.get('numbers'):
        char.extend([chr(i) for i in range(48,58)])

    if request.GET.get('special'):
        char.extend([chr(i) for i in range(33,48)])


    length = int(request.GET.get('length'))
    for i in range(length):
         psw += random.choice(char)
    return render(request,"gena/password.html",{'password':psw})
def comment (request):
    return render(request,"gena/Comment.html")
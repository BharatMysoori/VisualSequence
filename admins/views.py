from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from admins.forms import UploadForm
from admins.models import Prodcuts
from user.models import RegisterModel, Purchase


def login(request):
    if request.method == "POST":
        if request.method == "POST":
            usid = request.POST.get('username')
            pswd = request.POST.get('password')
            if usid == 'admin' and pswd == 'admin':
                return redirect('admin_page')
    return render(request,'admins/login_page.html')

def admin_page(request):
    if request.method=="POST":
        forms=UploadForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('admin_page')
    else:
        forms = UploadForm()

    return render(request,'admins/admin_page.html',{'form':forms})

def homepage(request):
    print('homepage_admin')
    prods = Prodcuts.objects.all()
    print("prods",prods)
    return render(request,'admins/homepage.html',{'prods':prods})

def userdetails(request):
    print('prods')
    obj = RegisterModel.objects.all()
    print('userdetailes',obj)
    return render(request,'admins/userdetails.html',{'objects':obj})

def cateanalysis(request,chart_type):

    chart = Purchase.objects.values('purhased').annotate(dcount=Count('status'))
    print("chart",chart)
    return render(request,'admins/cateanalysis.html',{'objects':chart,'chart_type':chart_type})
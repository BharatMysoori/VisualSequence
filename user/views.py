from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User

# Create your views here.
from admins.models import Prodcuts
from user.forms import RegisterForms, PurchaseForm, ReviewForm
from user.models import RegisterModel, Purchase, ReviewModel, Visual_Sequences


def index(request):
    if request.method=="POST":
        usid=request.POST.get('username')
        pswd = request.POST.get('password')
        try:
            check = RegisterModel.objects.get(userid=usid,password=pswd)
            request.session['userid']=check.id
            return redirect('userpage')
        except:
            pass
    return render(request,'user/index.html')

def register(request):
    if request.method=="POST":
        forms=RegisterForms(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('index')
    else:
        forms=RegisterForms()
    return render(request,'user/register.html',{'form':forms})
def userpage(request):
    products = Prodcuts.objects.all()
    return render(request, 'user/userpage.html',{'pts':products})

def all_products(request,pk):
    a=''
    b=''
    c=''
    pro = Prodcuts.objects.get(id=pk)
    b=pro.product_name
    c=pro.category
    pros = Prodcuts.objects.get(id=pk)

    uid = request.session['userid']
    print('uid',uid)
    uses = get_object_or_404(RegisterModel, id=uid)
    print('uses',uses)
    if request.method == "POST":
        a=request.POST.get('name')
        form = PurchaseForm(request.POST)
        if form.is_valid():
            ff = form.save(commit=False)
            ff.customer = uses
            ff.purhased = pro
            ff.cate=c
            ff.proname=b
            ff.save()
            print('product saved')
            return redirect('cart')
    else:
        form = PurchaseForm()
    if request.method == "POST":
        forms = ReviewForm(request.POST)
        if forms.is_valid():
            fa = forms.save(commit=False)
            fa.usid = uses
            fa.proid = pro
            fa.save()
            return redirect('userpage')
    else:
        forms = ReviewForm()

    return render(request,'user/all_products.html',{'prod':pro,'form':form,'fd':a,'fed':forms})

def details(request):
    usid = request.session['userid']
    us_id = RegisterModel.objects.get(id=usid)
    return render(request,'user/details.html',{'obje':us_id})
def cart(request):
    uid = request.session['userid']
    uses = get_object_or_404(RegisterModel, id=uid)
    p = Purchase.objects.filter(customer=uses, status='incart')
    if request.method == "POST":
        Purchase.objects.filter(customer=uses, status='incart').update(status='checkout')
        return redirect('userpage')
    return render(request,'user/cart.html',{'p':p})

def viewreview(request,pk):
    ffds = Prodcuts.objects.get(id=pk)
    aa=ReviewModel.objects.filter(proid=ffds)
    return render(request,'user/viewreview.html',{'ffs':aa})

def visual_sequence(request):
    ew=''
    uid = request.session['userid']
    #uid = request.user
    print(uid)

    uses = get_object_or_404(RegisterModel, id=uid)
    ew = uses.category
    obj=Visual_Sequences.objects.filter(cateogory=ew).order_by('-vals')
    print("obg,uses",ew,obj,uses)

    return render(request,'user/visual_sequence.html',{'efd':obj})

def update_details(request):
    userid = request.session['userid']
    objec = RegisterModel.objects.get(id=userid)
    if request.method == "POST":
        FirstName = request.POST.get('FirstName', '')
        LastName = request.POST.get('LastName', '')
        UserId = request.POST.get('UserId', '')
        Password = request.POST.get('Password', '')
        MobileNumber = request.POST.get('MobileNumber', '')
        EmailId = request.POST.get('EmailId', '')
        Gender = request.POST.get('Gender', '')
        Cateogory = request.POST.get('cateogory', '')

        obj = get_object_or_404(RegisterModel, id=userid)
        obj.firstname = FirstName
        obj.lastname = LastName
        obj.userid = UserId
        obj.password = Password
        obj.mblenum = MobileNumber
        obj.email = EmailId
        obj.gender = Gender
        obj.category = Cateogory

        obj.save(update_fields=["firstname", "lastname", "userid", "password", "mblenum", "email",
                                "gender","category" ])
        return redirect('details')
    return render(request,'user/update_details.html',{'obj': objec})


def categoryanalysis_chart(request,chart_type):
    ew = ''
    uid = request.session['userid']

    uses = get_object_or_404(RegisterModel, id=uid)
    ew = uses.category
    chart = Purchase.objects.filter(cate=ew).values('purhased').annotate(dcount=Count('status'))
    return render(request,'user/chart.html',{'objects':chart,'chart_type':chart_type})
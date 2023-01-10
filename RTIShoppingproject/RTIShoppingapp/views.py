from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from .models import Product,Catogery,Product_save
from .forms import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger




# Create your views here.
def main_page_view(request):
    if request.method=='POST':
        product=request.POST.get('product123')
        remove=request.POST.get('remove')
        cart=request.session.get('cart')
        if cart:
            quantity=cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]= quantity-1
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart={}
            cart[product]= 1
        request.session['cart']=cart
        print('cart',request.session['cart'])


        return redirect('main_page')

    else:
        cart=request.session.get('cart')
        if not cart:
            request.session['cart']={}
        product=None
        # request.session.get('cart').clear()
        catogeries=Catogery.objects.all()

        CategoryId=request.GET.get('category')
        if CategoryId:
            product=Product.get_all_product_by_categoryid(CategoryId)
        else:

            product = Product.objects.all()
            # request.session.clear()






        return render(request,'mainfile.html',{'product':product,'catergories':catogeries})

@login_required(login_url=('login'))
def Product_detail(request,id):
    product=Product.objects.get(id=id)
    return render(request ,'product_detail.html',{'product':product})

@login_required(login_url=('login'))
def ProductCart(request):
    if request.method=="POST":
        pass
    else:
        ids=list(request.session.get('cart').keys())
        product=Product.get_product_by_id(ids)
        print(product)


    return render(request,'ProductCart.html',{'product':product})


@login_required(login_url=('login'))
def CheckOut(request):
    if request.method=="POST":
        name = request.POST.get('name')
        phoneno = request.POST.get('number')
        zipcode = request.POST.get('pincode')
        locality = request.POST.get('locality')
        city = request.POST.get('city')
        sate = request.POST.get('state')
        landmark = request.POST.get('landmark')
        alternateno = request.POST.get('Alternateno')
        address = request.POST.get('address')

        Product_save(
            name=name,
            phone_no=phoneno,
            pincode=zipcode,
            locality=locality,
            city=city,
            state=sate,
            landmark=landmark,
            alt_no=alternateno,
            address=address
        ).save()
        return redirect('Payment')




    else:
        return render(request, 'Orderplace_Cart.html')


@login_required(login_url=('login'))
def Payment(request):
    return render(request,'Payment_page.html')


@login_required(login_url=('login'))
def Paid(request):
    return render(request ,'Paid Details.html')




def Register_view(request):
    if request.user.is_authenticated:
        return redirect('main_page')
    else:
        if request.method=='POST':
            forms = CreateUserForm(request.POST)
            if forms.is_valid():
                forms.save()
                return redirect('login')
            else:
                messages.warning(request, 'Filled Incorrect Detail**')
                return redirect('register')
        else:
            form=CreateUserForm()
            return render(request,'register_file.html',{'form':form})

def login_page(request):
    if request.user.is_authenticated:
        return redirect('main_page')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(username=username,password=password)

            if user is not None:
                login(request,user)

                return redirect('main_page')
            else:
                messages.warning(request,'Username or Password Incorrect')
                return render(request, 'login_file.html')
        else:
            return render(request, 'login_file.html')


def logout_page(request):
    logout(request)
    messages.success(request,'Logout Successfully..')
    return redirect('login')

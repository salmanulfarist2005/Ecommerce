from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from . models import Product,Contact,Checkout,OrderItem
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.views import View
import stripe
from django.conf import settings
# Create your views here.
def index(request):
    context={
        'pordu' :  Product.objects.all()
    }
    return render(request ,'web/index.html',context)

def login1(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
          login(request,user)
          return redirect('index')
        else :
            return redirect('signup')    
    return render(request,'web/account/login.html')



def signup(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1==password2:
            user = User.objects.create_user(username,email,password1)
            user.save()
            return redirect('login')
    return render(request ,'web/account/signup.html')


def logout1(request):
    logout(request)
    return redirect('index')


def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        telephone=request.POST.get('telephone')
        subject=request.POST.get('subject')
        message=request.POST.get('message')



        contact1=Contact(
            name=name,
            email=email,
            telephone=telephone,
            subject=subject,
            message=message,
        )

        contact1.save()


    return render(request ,'web/contact.html')



def Success(request):
    return render(request,'web/Success.html')



@login_required(login_url="login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")


@login_required(login_url="login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="login")
def cart_detail(request):
    return render(request, 'web/cart_detail.html')



def checkout(request):
    return render(request,"web/checkout.html")

def placeorder(request):
    if request.method=="POST":
        uid=request.session.get("_auth_user_id")
        user=User.objects.get(id=uid)
        

        cart=request.session.get('cart')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        baddress=request.POST.get('baddress')
        baddress2=request.POST.get('baddress2')
        select=request.POST.get('select')
        city=request.POST.get('city')
        zipcode=request.POST.get('zipcode')
        phone=request.POST.get('phone')
        cname=request.POST.get('cname')
        email=request.POST.get('email')


        checkout1=Checkout(
            user=user,
            fname=fname,
            lname=lname,
            baddress=baddress,
            baddress2=baddress2,
            select=select,
            city=city,
            zipcode=zipcode,
            phone=phone,
            cname=cname,
            email=email,



        )
        checkout1.save()

        for i in cart:
            a=float(cart[i]['price'])
            b=int(cart[i]['quantity'])
            total=a*b

            checkout2=OrderItem(
            checkout=checkout1,
            porduct=cart[i]['name'],
            image=cart[i]['image'],
            qunatity=cart[i]['quantity'],
            price=cart[i]['price'],
            total=total
            
            )
            checkout2.save()

    return render(request,'web/placeorder.html')


stripe.api_key = settings.STRIPE_SECRET_KEY

class CreateStripeCheckoutSessionView(View):
    """
    Create a checkout session and redirect the user to Stripe's checkout page
    """

    def post(self, request, *args, **kwargs):
        price1=OrderItem.objects.all()
        for p in price1:
            price2=p.total
            name1=p.porduct
      
        

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "unit_amount": int(price2) * 100,
                        "product_data": {
                            "name": name1,
                         
                        },
                    },
                    "quantity": 1,
                }
            ],
            
            mode="payment",
            success_url='http://localhost:8000/Success',


            
            cancel_url='http://localhost:8000/login',
        )
        return redirect(checkout_session.url)


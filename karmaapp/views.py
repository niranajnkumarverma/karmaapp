from django.core.checks import messages
from django.shortcuts import redirect, render
from django.contrib import messages
from django.conf import settings


from karmaapp.models import Billing_Address, Cart, User, UserProfile,Product,Order

# Create your views here.
app_info = {
    'app_title': 'Karma',
    'app_name': 'Karma app',
    'msg_data': {'name': '', 'msg': '', 'type':'success', 'display': ''},
} 
def index(request):

    users = Product.objects.all()
    return render(request,"index.html", {'users':users})
  
def login_page(request):
    if request.method == 'POST':
            userdetail = User.objects.get(email = request.POST['email'],password = request.POST['password'])
            request.session['email'] = userdetail.email
            
            app_info['msg_data']['name'] = 'Login'
            app_info['msg_data']['msg'] = f'Login has been successfully Added.'
            app_info['msg_data']['type'] = 'success'
            app_info['msg_data']['display'] = 'show'
            return redirect(index)
    return render(request,"app/login.html",app_info)


def register_page(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        User.objects.create(
            email = email,
            password = password
        )
        app_info['msg_data']['name'] = 'Register'
        app_info['msg_data']['msg'] = f'Your data has been successfully Register.'
        app_info['msg_data']['type'] = 'success'
        app_info['msg_data']['display'] = 'show'
        return redirect('login_page')
    return render(request,"app/register.html",app_info)

def contact_page(request):
    return render(request,"app/contact.html")

def profile_page(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        mobile = request.POST['mobile']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']
        pincode = request.POST['pincode']
        UserProfile.objects.create(
            firstname=firstname,
            lastname=lastname,
            mobile=mobile,
            address=address,
            city=city,
            state=state,
            country=country,
            pincode=pincode

        )
        app_info['msg_data']['name'] = 'Profile'
        app_info['msg_data']['msg'] = f'Your Profile has been successfully saved.'
        app_info['msg_data']['type'] = 'success'
        app_info['msg_data']['display'] = 'show'
    return render(request,"app/profile.html",app_info)  

def update_page(request,id):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        mobile = request.POST['mobile']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']
        pincode = request.POST['pincode']
        UserProfile.objects.filter(id=id).update(
            firstname=firstname,
            lastname=lastname,
            mobile=mobile,
            address=address,
            city=city,
            state=state,
            country=country,
            pincode=pincode

        )
        user = UserProfile.objects.get(id=id)
        UserProfile.save()
    return render(request,"app/update.html",{'users':user}) 

def change_password(request):
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']

        user = User.objects.get(email=request.session['email'])

        if current_password == user.password:
            user.password = new_password
            user.save()
            app_info['msg_data']['name'] = 'Password Changed'
            app_info['msg_data']['msg'] = f'Your password changed successfully done.'
            app_info['msg_data']['type'] = 'success'
        else:
            app_info['msg_data']['name'] = 'Not Matched'
            app_info['msg_data']['msg'] = f'Please enter your currect current password.'
            app_info['msg_data']['type'] = 'warning'
        app_info['msg_data']['display'] = 'show'
        return redirect(index)
    else:
        pass
    return render(request,"app/change_password.html")  

def shop_page(request):
    q = request.GET.get('q')
    users=Product.objects.filter(name=q)
          
    users = Product.objects.all()
    
    return render(request,"app/category.html",{'users':users})   

       
def order_page(request):
    load_cart(request)
    return render(request,"app/cart.html",app_info)  

# load cart
def load_cart(request):
    user = User.objects.get(email=request.session['email'])
   
    cart = Cart.objects.filter(user=user)[::-1]
    total_cart_amount = 0
    for c in cart:
        total_cart_amount += c.total
        print(type(total_cart_amount), (total_cart_amount / 100) * 18)
    tax = (total_cart_amount / 100) * 18
    final_amount = total_cart_amount + tax

    app_info['cart_data'] = {'cart': cart, 'tax':tax, 'final_amount': final_amount, 'total_cart_amount': total_cart_amount, 'total_cart': len(cart)}

def add_to_cart(request, pk):
    product=Product.objects.get(pk=pk)
    user=User.objects.get(email=request.session['email'])
    Cart.objects.create(product=product,user=user,price=product.price,total=product.price)

    app_info['msg_data']['name'] = 'Cart'
    app_info['msg_data']['msg'] = f'Your Cart has been successfully Added.'
    app_info['msg_data']['type'] = 'success'
    app_info['msg_data']['display'] = 'show'
  
    return redirect(index)
   

## view cart
def view_cart(request,pk):
    cart = Cart.objects.filter(pk=pk)[::-1]
    app_info['cart_data'] = {'cart': cart, 'total_cart': len(cart)}
    return redirect(order_page)

def update_cart(request, pk):
    cart = Cart.objects.get(pk=pk)
    cart.quantity = int(request.POST['qty'])
    print(type(cart.quantity), cart.quantity)
    # print(cart.Product.Price)
    cart.total = cart.quantity * cart.product.price
    cart.save()
    app_info['msg_data']['name'] = 'Quantity UpdateToCart'
    app_info['msg_data']['msg'] = f'Quantity  UpdateToCart successfully.'
    app_info['msg_data']['type'] = 'success'
    app_info['msg_data']['display'] = 'show'
    return redirect(order_page)


## delete cart
def delete_cart(request,pk):
    Cart.objects.get(pk=pk).delete()
    app_info['msg_data']['name'] = 'product Delete To Cart'
    app_info['msg_data']['msg'] = f'product  Delete To Cart successfully.'
    app_info['msg_data']['type'] = 'success'
    app_info['msg_data']['display'] = 'show'
    return redirect(order_page)

def order_details(request):
    product = Product.objects.get()
    qty = 1
    total = product.Price * qty
    
    Order.objects.create(
        
        Product = product,
        Quantity = qty,
        Total = total
    )

def search_page(request):
        return render(request,"app/search.html")  

def billing_page(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        mobile = request.POST['mobile']
        address = request.POST['address']
        city = request.POST['city']
        Districk = request.POST['districk']
        state = request.POST['state']
        country = request.POST['country']
        pincode = request.POST['pincode']
        Billing_Address.objects.create(
            firstname=firstname,
            lastname=lastname,
            mobile=mobile,
            address=address,
            city=city,
            Districk=Districk,
            state=state,
            country=country,
            pincode=pincode

        )
       
   
        return redirect(confirmation_page)  
    return render(request,"app/checkout.html")      

def confirmation_page(request):
    app_info['msg_data']['name'] = 'Thank You'
    app_info['msg_data']['msg'] = f'Your Order has been recieved .'
    app_info['msg_data']['type'] = 'success'
    app_info['msg_data']['display'] = 'show'
    return render(request,"app/confirmation.html",app_info)        


def logout_page(request):
    if 'email' in request.session:
        del request.session['email']
        app_info['msg_data']

    return redirect(index)

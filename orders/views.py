from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Topping, MenuItem, ItemType, Price, Cart
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def registerUser(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            firstName = form.cleaned_data['firstName']
            lastName = form.cleaned_data['lastName']

            if User.objects.filter(username=username).exists():
                return render(request, 'orders/register.html', {'form': form, 'message': 'Username already exists!'})
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=firstName, last_name=lastName)
                user.save()

            messages.success(request, 'Account created successfully!')
            return HttpResponseRedirect('/login')
    else:
        form = RegistrationForm()
        
    return render(request, 'orders/register.html', {'form': form})

def loginUser(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if request.user.is_superuser:
                    return HttpResponseRedirect('/cart')
                else: 
                    return HttpResponseRedirect('/menu')
            else:
                error = 'Invalid login! Please try again!!!'
                return render(request, 'orders/login.html', {'form': form, 'error': error})
    else:
        form = LoginForm()

    return render(request, 'orders/login.html', {'form': form})

def logoutUser(request):
    logout(request)
    messages.success(request, 'You are logged out successfully!')
    return HttpResponseRedirect('/login')

@login_required(login_url='/login')
def menu(request):
    regularPizzas = ItemType.objects.filter(itemId=1)
    sicilianPizzas = ItemType.objects.filter(itemId=4)
    subs = ItemType.objects.filter(itemId=2)
    pasta = ItemType.objects.filter(itemId=3)
    salads = ItemType.objects.filter(itemId=6)
    dinnerPlatters = ItemType.objects.filter(itemId=5)
    pizzaToppings = Topping.objects.filter(forPizza=True)
    subToppings = Topping.objects.filter(forSub=True)

    context = {
        'regularPizzas': regularPizzas,
        'sicilianPizzas': sicilianPizzas,
        'subs': subs,
        'pasta': pasta,
        'salads': salads,
        'dinnerPlatters': dinnerPlatters,
        'pizzaToppings': pizzaToppings.exclude(toppingsType=None),
        'subToppings': subToppings.exclude(toppingsType="Cheese")
    }

    if request.method == 'POST':
        username = request.user

        itemName = request.POST['item']

        if 'size' in request.POST:
            size = request.POST['size']
        else:
            size = "Regular"
        
        if 'type' in request.POST:
            itemType = request.POST['type']
        else:
            itemType = None
        
        if itemType == "Special":
            topping1 = "Pepperoni"
            topping2 = "Onions"
            topping3 = "GreenPeppers"
        else:
            if 'topping1' in request.POST:
                topping1 = request.POST['topping1']
                if topping1 == "None":
                    topping1 = None
            else:
                topping1 = None
            
            if 'topping2' in request.POST:
                topping2 = request.POST['topping2']
                if topping2 == "None":
                    topping2 = None
            else:
                topping2 = None
            
            if 'topping3' in request.POST:
                topping3 = request.POST['topping3']
                if topping3 == "None":
                    topping3 = None
            else:
                topping3 = None
        
        itemId = MenuItem.objects.get(itemName=itemName).id
        itemTypeId = ItemType.objects.get(itemType=itemType, itemId=itemId).id
        price = Price.objects.get(itemTypeId=itemTypeId, size=size).price
        userId = User.objects.get(username=username).id

        cart = Cart(item=MenuItem.objects.get(id=itemId), itemType=ItemType.objects.get(id=itemTypeId), price=price, user=User.objects.get(id=userId), topping1=Topping.objects.get(toppingsType=topping1), topping2=Topping.objects.get(toppingsType=topping2), topping3=Topping.objects.get(toppingsType=topping3))

        cart.save()

        return render(request, 'orders/menu.html', context)

    return render(request, 'orders/menu.html', context)

@login_required(login_url='/login')
def cart(request):
    username = request.user
    userId = User.objects.get(username=username).id
    userCart = Cart.objects.filter(user=userId).filter(ordered=False)
    userOrder = Cart.objects.filter(user=userId).filter(ordered=True).filter(completed=False)
    completeOrder = Cart.objects.filter(user=userId).filter(completed=True)
    allUsersCarts = Cart.objects.filter(ordered=True).filter(completed=False)
    price = Cart.objects.values('price').filter(user=userId)

    total_price = 0
    for item in price:
        total_price = total_price + item['price']
    
    total_price = round(total_price, 2)

    if request.method == 'POST':
        userCart.update(ordered=True)
    
    users = []
    for cart in allUsersCarts:
        users.append(cart.user)
    
    users_set = set(users)

    if username.is_superuser:
        return render(request, 'orders/cart.html', {'is_superuser': True, 'users': users_set})
    else:
        return render(request, 'orders/cart.html', {'cart': userCart, 'orders': userOrder, 'completedOrder': completeOrder, 'total_price': total_price})

@login_required(login_url='/login')
def user_order(request, user_id):
    if request.user.is_superuser:
        userCart = Cart.objects.filter(user=user_id).filter(ordered=True).filter(completed=False)

        if request.method == 'POST':
            userCart.update(completed=True)
            return HttpResponseRedirect('/cart')

        return render(request, 'orders/userorder.html', {'cart': userCart})
    else:
        return HttpResponseRedirect('/login')
    
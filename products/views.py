from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as auth_login,logout 
from django.contrib.auth.decorators import login_required
from .forms import ProductForm,SignupForm
from .models import Products
# Create your views here.


from django.contrib.auth import login
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Replace 'login' with your desired landing page
    else:
        form = SignupForm()
    
    return render(request, 'signup.html', {'form': form})


from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')  # Replace 'login' with your desired landing page
        else:
            # Handle authentication errors here, e.g., invalid credentials
            error_message = "Invalid username or password"
    else:
        error_message = None
    
    return render(request, 'login.html', {'error_message': error_message})












@login_required(login_url='/products/login/')
def home_page(request):
    return render(request,'home.html')


#LOGOUT
@login_required(login_url='/products/login/')
def logout_page(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

    context = {
        'user': request.user
    }

    return render(request, 'logout.html', context)

#CREAT
@login_required(login_url='/products/login/')
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('retrieveproduct')
    else:
        form =ProductForm()
        
    return render(request, 'crud/create.html', {'form': form})

#READ
@login_required(login_url='/products/login/')
def product_read(request):
    product_list= Products.objects.all()
    return render(request,'crud/retrieve.html',{'product_list':product_list})


#UPDATE
@login_required(login_url='/products/login/')
def product_update(request, id):
    product = Products.objects.get(pk=id)
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('retrieveproduct')
    else:
        form =ProductForm(instance=product)           
    return render(request, 'crud/update.html', {'form': form})


#DELETE
@login_required(login_url='/products/login/')
def product_delete(request,id):
    product=Products.objects.get(pk=id)  
    if request.method == 'POST':
        product.delete()
        return redirect('retrieveproduct')
    
    return render(request,'crud/delete.html',{'product':product})



#SEARCH
@login_required(login_url='/products/login/')
def product_search(request):
    if request.method == 'GET':
        search_query = request.GET.get('search', '')
        products = Products.objects.filter(name__istartswith=search_query)
    else:
        products = Products.objects.all()

    return render(request, 'crud/product_search.html', {'products': products, 'search_query': search_query})





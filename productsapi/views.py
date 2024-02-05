


from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import  HTTP_200_OK,HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from products.forms import ProductForm

from products.models import Products
from .serializers import ProductSerializer

from django.shortcuts import get_object_or_404

from rest_framework import status
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from .serializers import ProductSerializer

#SINGUP


@api_view(['POST'])
@permission_classes((AllowAny,))
def signup(request):
    form = UserCreationForm(data=request.data)
    if form.is_valid():
        form.save()
        return Response("account created successfully", status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


#LOGIN

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},status=HTTP_200_OK)



#CREAT

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def create_product(request):
    form = ProductForm(request.POST)
    if form.is_valid():
        product = form.save()
        return Response({'id': product.id}, status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


#LIST

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def list_products(request):
    products = Products.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)



#UPDATE

@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def update_product(request, pk):
    product = get_object_or_404(Products, pk=pk)
    form = ProductForm(request.data, instance=product)
    if form.is_valid():
        form.save()
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    else:
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    

#DELETE

@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def delete_product(request, pk):
    try:
        product = Products.objects.get(pk=pk)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    product.delete()
    return Response("deleted successfully")





#SEARCH

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def product_search(request):
    search_params = {}
    search_params['name__istartswith'] = request.GET.get('name', '')  # Use 'name' as the key in the query parameter

    products = Products.objects.filter(**search_params)

    # Extract the names from the products
    product_names = [product.name for product in products]

    return Response({'product_names': product_names})


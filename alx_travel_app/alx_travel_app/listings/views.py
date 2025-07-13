from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def index(request):
    return JsonResponse({'message': 'Welcome to ALX Travel App!'})

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def sample_api(request):
    return Response({"message": "Hello from ALX Travel App!"})

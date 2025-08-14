from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def menu_list(request):
    if request.method == 'POST':
        return JsonResponse({'message':'post요청을 받음'})
    
    data = [
        {"name": "Espresso", "price": 3000},
        {"name": "Americano", "price": 3500},
        {"name": "Latte", "price": 4000}
    ]
    return JsonResponse(data,safe=False)

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def index(request):
    return JsonResponse({'foo': 'bar'}, safe=False)

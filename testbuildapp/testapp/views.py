from django.shortcuts import render
from django.http import response
# Create your views here.
def test(request):
    return response("The app is built and running fine.")


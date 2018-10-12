from django.shortcuts import render, redirect

def convert(request):
    return render(request, 'index.html')

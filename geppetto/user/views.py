# from django.shortcuts import render
from django.http import HttpResponse


def get_user_info(request):
    return HttpResponse('Hello world')

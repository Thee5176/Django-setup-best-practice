from django.shortcuts import render
from django.http import HttpResponse

def homePageView(request):
    '''3 approaches: CBVs is simpliest, FBVs allow more reusability, DRY principle, and can extended via mixins, GCBVs is use to handle common repetitive.'''
    return HttpResponse('Hello, World!')

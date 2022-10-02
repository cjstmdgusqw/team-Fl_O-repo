from django.shortcuts import render, redirect
from django.http import HttpResponse


def posting(request):
    return redirect(request, 'posting/')
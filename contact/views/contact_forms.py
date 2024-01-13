from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from django import forms

from contact.models import Contact

class ContactFrom(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone',
        )

def create(request):
    if request.method == 'POST':
        context = {
        'form': ContactFrom(request.POST)
        }

        return render(
            request,
            'contact/create.html',
            context
        )
    
    context = {
        'form': ContactFrom()
    }
    
    return render(
        request,
        'contact/create.html',
        context
    )
    
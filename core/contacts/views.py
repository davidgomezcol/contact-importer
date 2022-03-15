from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Contacts


@login_required(login_url='login')
def contacts_view(request):
    """Contacts Page View"""
    queryset = Contacts.objects.all().order_by('name')
    filter_contacts = queryset.filter(user=request.user)
    p = Paginator(filter_contacts, 3)
    page = request.GET.get('page')
    contacts = p.get_page(page)

    context = {
        'contacts': contacts
    }

    return render(request, 'pages/contacts.html', context)

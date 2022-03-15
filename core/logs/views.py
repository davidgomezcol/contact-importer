from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import FilesStatus


@login_required(login_url='login')
def files_status_view(request):
    """Files status page view"""
    queryset = FilesStatus.objects.all().order_by('-id')
    user_files = queryset.filter(user=request.user)
    context = {
        "status": user_files
    }
    return render(request, 'pages/files-status.html', context)

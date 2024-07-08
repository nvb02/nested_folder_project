from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def folder_list(request):
    folders = Folder.objects.filter(parent__isnull=True)
    return render(request, 'folder_list.html', {'folders':folders})

def folder_detail(request,folder_id):
    folder = get_object_or_404(Folder, id = folder_id)
    children = folder.get_children()
    parent = folder.get_parent()
    return render(request, 'folder_detail.html', {'folder': folder, 'children': children, 'parent': parent})

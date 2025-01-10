import threading

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import HttpResponse
from django.shortcuts import render

from .forms import UserForm


def save_file_to_cloud(file, instance):
    file_path = default_storage.save(file.name, ContentFile(file.read()))
    instance.file = file_path
    instance.save()


def test_form(request):
    if request.method == "GET":
        form = UserForm()
        context = {
            'form': form
        }
        return render(request, 'form_app.html', context)
    elif request.method == "POST":
        instance = UserForm(data=request.POST, files=request.FILES)
        file = request.FILES['file']
        thread = threading.Thread(target=save_file_to_cloud, args=(file, instance,))
        thread.start()

        return HttpResponse("Data came to here")

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from mainapp.models import Dialog


@login_required
def index(request):
    dialogues = request.user.dialogs.all()
    context = {
        'page_title': 'диалоги',
        'dialogues': dialogues,
    }

    return render(request, 'mainapp/index.html', context)


def dialog(request, dialog_id):
    dialogs = Dialog.objects.filter(id=dialog_id)
    context = {
        'dialogs': dialogs,
        'page_title': 'Диалог',
    }

    return render(request, 'mainapp/dialog.html', context)

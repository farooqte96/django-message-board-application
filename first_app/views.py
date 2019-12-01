from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .forms import CreateMessage, SelectVersion
from .models import Message

#show main view
def home(request):
    abstract_dict = {
    'abstract':"Welcome to Message Application"
    }
    return render(request, 'base.html', context = abstract_dict)

def create_message_form(request):
    if request.method == "POST":
        form = CreateMessage(request.POST)

        if form.is_valid():
            form.save(commit= True)
            # return home(request)
            context = {
                'message': "Message created Successfully"
            }
            return render(request, 'first_app/message_status.html', context)
        else:
            return render(request, 'first_app/form_error.html', context = {'form':form})

    # show create message form for GET requests
    form = CreateMessage()
    message_dict = {
            'message':"Write Your Message here!",
            'form':form
            }
    return render(request, 'first_app/create_message_form.html', context = message_dict)

def get_messages(request, version):

    context = {

    'message_records': Message.objects.all(),
    'version': version,
    'message':"Select Version Please!",
    }
    return render(request, 'first_app/messages.html', context)

def update_message_form(request, message_id ):
    message = get_object_or_404(Message, pk = message_id)

    if request.method == "POST":
        form = CreateMessage(request.POST, instance = message)

        if form.is_valid():

            form.save(commit= True)
            context = {
                'message' : "Message with title '{}' updated successfully".format(message.title)
            }

            return render(request, 'first_app/message_status.html', context = context)
        else:
            return render(request, 'first_app/form_error.html', context = {'form':form})

    #If not POST show message update form
    else:
        form = CreateMessage(instance = message)
        message_dict = {

            'form':form,
            'message':"Update Your Message here!",
            }
    return render(request, 'first_app/update_message_form.html', context = message_dict)

def delete_message(request, message_id):
    message = get_object_or_404(Message, pk = message_id)
    if message is not None:
        message.delete()
        context = {
            'message' : "Message with title '{}' deleted successfully".format(message.title)
        }

        return render(request, 'first_app/message_status.html', context = context)


def versions(request):
    if request.method == "POST":
        form = SelectVersion(request.POST)
        if form.is_valid():
            version = form.cleaned_data['version']
            return redirect('messages', version)
        else:
            return render(request, 'first_app/form_error.html', context = {'form':form})
    message_dict = {
            'form': SelectVersion(),
            'message':"Select version of messages ",

            }
    return render(request, 'first_app/version_form.html', context = message_dict)

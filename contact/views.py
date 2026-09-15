from django.shortcuts import render
from .forms import ContactModelForm
from .models import Contact
# Create your views here.


def contact(request):
    data = Contact.objects.all
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        con = form.save()
        return render(request, 'sucess.html', {'message': "Thankyou", 'con': con})
    else:
        form = ContactModelForm()
    return render(request, 'index.html', {'form': form, 'data': data})

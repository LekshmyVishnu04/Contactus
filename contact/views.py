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
    values = Contact.objects.all().values()
    values_selected = Contact.objects.all().values('fullmame', 'email')
    value_list = Contact.objects.all().values_list('fullmame')
    value_single = Contact.objects.all().values('email')
    value_single_list = Contact.objects.all().values_list('email')
    filter = Contact.objects.filter(email='l@gmail.com').values()
    filterwithselectedcol = Contact.objects.filter(
        email='l@gmail.com').values('email')
    filterDouble = Contact.objects.filter(
        email='l@gmail.com', pho='123456').values()
    email__exact = Contact.objects.filter(email__exact='l@gmail.com').values()
    email_contains = Contact.objects.filter(email__contains='v@').values()
    incondi = Contact.objects.filter(
        email__in=['l@gmail.com', 'v@gmail.com']).values()
    offset = Contact.objects.all()[1:2].values()
    return render(request, 'index.html', {'form': form, 'data': data, 'values': values, 'value_list': value_list, 'values_selected': values_selected, 'value_single': value_single, 'value_single_list': value_single_list, 'filter': filter, 'filterwithselectedcol': filterwithselectedcol, 'filterDouble': filterDouble, 'email__exact': email__exact, 'email_contains': email_contains, 'incondi': incondi, 'offset': offset})

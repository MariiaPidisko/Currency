from currency.models import ContactUs

from django.http import HttpResponse


def cont_list(request):
    contact = []
    for cont in ContactUs.objects.all():
        contact.append([cont.id, cont.email_from, cont.subject, cont.message])
    return HttpResponse(str(contact))

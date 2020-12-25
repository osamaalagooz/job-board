from django.shortcuts import render
from .models import Info
from django.core.mail import send_mail 
from django.conf import settings
# Create your views here.
def contact_us(request):
    info = Info.objects.first()

    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],
        )

    return render(request,'contact.html',{'info':info})
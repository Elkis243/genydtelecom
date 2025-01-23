from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

# Create your views here.
def home(request):
    current_link_name = 'home'
    return render(request, 'app/home.html', {
        'current_link_name': current_link_name
    })
    
def about(request):
    current_link_name = 'about'
    return render(request, 'app/about.html', {
        'current_link_name': current_link_name
    })

def contact(request):
    current_link_name = 'contact'

    if request.method == 'POST':
        recipient = request.POST.get('email')
        subject = request.POST.get('objet')
        message = request.POST.get('message')
        sender = settings.EMAIL_HOST_USER 

        try:
            send_mail(
                subject=subject,
                message=message,
                from_email=sender,
                recipient_list=[recipient],
                fail_silently=False
            )
            messages.success(request, "Votre message a été envoyé avec succès. Nous vous répondrons bientôt !")
        except Exception as e:
            messages.error(request, f"Une erreur s'est produite lors de l'envoi de votre message : {str(e)}")

        return HttpResponseRedirect('/contact/')
    
    return render(request, 'app/contact.html', {
        'current_link_name': current_link_name
    })


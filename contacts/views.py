from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact(request):
  if request.method == 'POST':
    listing_id = request.POST['listing_id']
    listing = request.POST['listing']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = request.POST['user_id']
    realtor_email = request.POST['realtor_email']

    # Verificam daca utilizatorii au trimis deja un formular de contact

    if request.user.is_authenticated:
      user_id = request.user.id 

      has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id )

      if has_contacted:
        messages.error(request, "Ati trimis formularul pentru acest anunt!")

    contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id )

    contact.save()
    
    #Trimiter email

    send_mail(
      'Intrebari anunt',
      'Au fost cateva intrebari legate de anuntul ' + listing + '. Pentru mai multe detalii intrati in cont. ',
      'farazahar14@gmail.com',
      [realtor_email, 'farazahar14@gmail.com'],
      fail_silently=False

    )

    messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
    return redirect('/listings/'+listing_id)
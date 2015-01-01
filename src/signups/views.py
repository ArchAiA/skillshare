#! Best practices for the views.py file is to have 1) Python first, 2) Django second, 3) Your apps, and then 4) Local Apps -- Lecture 32

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail #! Sendmail is a function that allows us to send mail with the specified settings in settings.py
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect

from .forms import SignUpForm #! From the forms.py file in the same folder import class SignUpForm



# Create your views here.
def home(request):
        
    return render_to_response("signup.html",
                              locals(),
                              context_instance=RequestContext(request))




def thankyou(request): # The class that is defined here must match the [name] specified in urls.py

# This entire block was moved from the home class in Lecture 31    
    form = SignUpForm(request.POST or None) #! create form as an instance of SignUpForm and request POST from sending page

    if form.is_valid():                     #! If the form is valid
        save_it = form.save(commit=False)   #! Save the contents to save_it
        save_it.save()                      #? Why is this needed?
        
        #send_mail(subject, message, from_email, to_list, fail_silently=True) #! This will send an email after the data is saved -- Lecture 32
        subject = 'Thank you for your Pre-Order' #! What the subject of the message will be
        message = 'Welcome./n We will be in touch soon' #! What the body of the message will say
        from_email = settings.EMAIL_HOST_USER #! Who the email will be sent from
        to_list =[save_it.email, settings.EMAIL_HOST_USER] #! Who the email will be sent to
        send_mail(subject, message, from_email, to_list, fail_silently=True) #! This sends the email
        #send_mail(subject, message, from_email, to_list, fail_silently=True) #! This will send an email after the data is saved -- Lecture 32

        
        messages.success(request, 'Thank you for your order.  We will be in touch.')
        return HttpResponseRedirect('/thank-you/') # This redirects the user to the thank-you page after success
 # This entire block was moved from the home class in Lecture 31    \ 
    
    return render_to_response("thankyou.html",
                              locals(),
                              context_instance=RequestContext(request))



def aboutus(request):
    
    return render_to_response("aboutus.html",
                                locals(),
                                context_instance=RequestContext(request))
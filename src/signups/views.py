from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def home(request):
    
    from .forms import SignUpForm #! From the forms.py file in the same folder import class SignUpForm
    
    form = SignUpForm(request.POST or None) #! create form as an instance of SignUpForm and request POST from sending page
    
    if form.is_valid():                     #! If the form is valid
        save_it = form.save(commit=False)   #! Save the contents to save_it
        save_it.save()                      #? Why is this needed?
        messages.success(request, 'We will be in touch')
        return HttpResponseRedirect('/thank-you/') # This redirects the user to the thank-you page after success
        
    return render_to_response("signup.html",
                              locals(),
                              context_instance=RequestContext(request))




def thankyou(request): # The class that is defined here must match the [name] specified in urls.py
    
    return render_to_response("thankyou.html",
                              locals(),
                              context_instance=RequestContext(request))



def aboutus(request):
    
    return render_to_response("aboutus.html",
                                locals(),
                                context_instance=RequestContext(request))
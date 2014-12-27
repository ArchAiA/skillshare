from django.shortcuts import render, render_to_response, RequestContext

# Create your views here.
def home(request):
    
    from .forms import SignUpForm #! From the forms.py file in the same folder import class SignUpForm
    
    form = SignUpForm(request.POST or None) #! create form as an instance of SignUpForm and request POST from sending page
    
    if form.is_valid():                     #! If the form is valid
        save_it = form.save(commit=False)   #! Save the contents to save_it
        save_it.save()                      #? Why is this needed?
    
    return render_to_response("signup.html",
                              locals(),
                              context_instance=RequestContext(request))


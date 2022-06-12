import os

# import stripe
from contestants.models import ContestType, ContestantForm
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView

from home.forms import ContactForm, PaymentForm
from django.core.mail import send_mail

from home.models import Gallery
from django.contrib import messages



class SuccessView(TemplateView):
    template_name = "success.html"
    
class CancelView(TemplateView):
    template_name = "cancel.html"

class HomeView(View):
    def get(self, request):
        return render(request, 'home/index.html')
    
class AboutUsView(View):
    def get(self, request):
        return render(request, 'home/about.html')
    
class ContactUsView(View):
    def get(self, request):
        form = ContactForm()
        context = {
            'form':form
        }
        return render(request, 'home/contact.html', context)
    
    def post(self, request):
        form = ContactForm()
        context = {
            'form':form
        }
        # name = request.POST['name']
        email = request.POST.get('email', '')
        subject = request.POST['subject']
        message = request.POST['message']
        
        if not email:
            messages.error(request, 'Email cannot be empty')
            return render(request, 'home/contact.html', context)
        
        if not subject:
            messages.error(request, 'Subject cannot be empty')
            return render(request, 'home/contact.html', context)
        
        if not message:
            messages.error(request, 'Message Body cannot be empty')
            return render(request, 'home/contact.html', context)
        #send email
        send_mail(
            subject,
            message,
            email, 
            [settings.EMAIL_HOST_USER],
        )
        messages.success(request, 'Message Sent Successfully')
        return redirect('contact-us')
        
class RegisterView(View):
    def get(self, request):
        c_types = ContestType.objects.filter(is_active=True)
        context = {'c_types':c_types}
        return render(request, 'home/apply.html', context)
    
    def post(self, request):
        c_types = ContestType.objects.filter(is_active=True)
        context = {'c_types':c_types, 'values':request.POST}
        
        name = request.POST['name']
        phone_no = request.POST['phone_no']
        state_of_origin = request.POST['state_of_origin']
        state_of_residence = request.POST['state_of_residence']
        reg_type = request.POST['reg_type']
        address = request.POST['address']
        reg_image = request.FILES.get('reg_image')
        
        contest_type = ContestType.objects.get(id=reg_type)
        
        if not name:
            messages.error(request, 'Please Enter Your Name')
            return render(request, 'home/apply.html', context)
        
        if not phone_no:
            messages.error(request, 'Phone Number is required')
            return render(request, 'home/apply.html', context)
        
        if not state_of_origin:
            messages.error(request, 'State of origin is required')
            return render(request, 'home/apply.html', context)
        
        if not state_of_residence:
            messages.error(request, 'State of residence is required')
            return render(request, 'home/apply.html', context)
        
        if not reg_type:
            messages.error(request, 'Select A contest')
            return render(request, 'home/apply.html', context)
        
        if not address:
            messages.error(request, 'Address is required')
            return render(request, 'home/apply.html', context)
        
        if not reg_image:
            messages.error(request, 'Upload A Photo')
            return render(request, 'home/apply.html', context)
        
        ContestantForm.objects.create(name=name, phone_no=phone_no, state_of_origin=state_of_origin, state_of_residence=state_of_residence, reg_type=contest_type, address=address, reg_image=reg_image)
        messages.success(request, 'Registration Filled Successfully')
        return redirect('index')
        

class GalleryView(TemplateView):
    template_name = 'home/gallery.html'
    
    def get_context_data(self, *args, **kwargs):
        galleries = Gallery.objects.all()
        context = ({
            'galleries':galleries,
        })
        return context
        
    
class AllContestantsView(View):
    def get(self, request):
        ctype = ContestType.objects.filter(is_active=True)
        contestants = ContestantForm.objects.filter(reg_type__in=ctype)
        context = {
            'all_contestants':contestants,
            'c_active':ctype,
        }
        return render(request, 'home/contestants/all-contestants.html', context)

class ContestantView(View):
    def get(self, request, pk):
        data = ContestantForm.objects.get(id=pk)
        # return random[0:string_length] # Return the random string.

        form = PaymentForm()
        context = {
            'contestant':data,
            'form':form,    
        }
        return render(request, 'home/contestants/contestant-detail.html', context)

    def post(self, request, pk):
        pass
        # data = ContestantForm.objects.get(id=pk)
        # form = PaymentForm(request.POST)
        # if form.is_valid():
        #     name = form.cleaned_data['name']
        #     email = form.cleaned_data['email']
        #     amount = form.cleaned_data['amount']
        #     phone = form.cleaned_data['phone']
        #     return redirect(str(process_payment(name,email,amount,phone)))

class ContestantVotedView(View):
    def get(self, request, pk):
        data = ContestantForm.objects.get(id=pk)
        
        data.votes += 1
        data.save()
        
        messages.success(request, 'Vote Successful')
        return redirect(request.META.get('HTTP_REFERER'))



class AllContestantsSuccessView(View):
    def get(self, request):
        contestants = ContestantForm.objects.all()
        context = {
            'all_contestants':contestants,
        }
        messages.success(request, 'Voting was successfully')
        return render(request, 'home/contestants/all-contestants.html', context)
    

class HallOfFameView(View):
    def get(self, request):
        contestants = ContestantForm.objects.filter()
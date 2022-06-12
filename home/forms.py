from django import forms

from contestants.models import ContestantForm

class PaymentForm(forms.ModelForm):
    class Meta:
        model = ContestantForm
        fields = ('amount', 'name')
    
    
    
class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.Textarea()
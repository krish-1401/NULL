from django import forms
from .models import clerk
class clerkform(forms.ModelForm):
    class Meta:
        model:clerk
        fields=['first_name','last_name','hospital_id']

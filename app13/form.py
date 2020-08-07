from django.forms import ModelForm
from app13.models import student

class studentdata(ModelForm):
    class Meta:
        abc = student
        fields = ['name','email']
        
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm, TextInput, ChoiceField, DateTimeInput

from .models import CustomUser, Event


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = get_user_model()
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('email',)


CATEGORY_CHOICES = (
    ('conferencia', ('CONFERENCIA')),
    ('seminario', ('SEMINARIO')),
    ('congreso', ('CONGRESO')),
    ('curso', ('CURSO')),

)

TYPE_EVENT_CHOICES = (
    ('presencial', 'PRESENCIAL'),
    ('virtual', 'VIRTUAL')

)

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'category', 'place', 'address', 'start_date', 'end_date', 'type_event']

        widgets = {
            'name': TextInput(attrs={'class':'form-control'}),
           # 'category': ChoiceField(choices=CATEGORY_CHOICES, required=True),
            'place': TextInput(attrs={'class': 'form-control'}, ),
            'address': TextInput(attrs={'class': 'form-control'}),
            'start_date': DateTimeInput(attrs={'class':'form-control'}),
            'end_date': DateTimeInput(attrs={'class':'form-control'}),
           # 'type_event': ChoiceField(choices=TYPE_EVENT_CHOICES, required=True,),
        }

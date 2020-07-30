from django import forms
import datetime

from .models import User
from artists.models import Umetnina


class UserForm(forms.ModelForm):
    name = forms.CharField(
                label='Name',
                widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'name'})
                )
    surname = forms.CharField(
                label='Surname',
                widget=forms.TextInput(attrs={'class': 'form-control'})
                )
    email = forms.EmailField(
                label='Email',
                widget=forms.EmailInput(attrs={'class': 'form-control'})
                )
    country = forms.CharField(
                label='Country',
                widget=forms.TextInput(attrs={'class': 'form-control'})
                )
    password1 = forms.CharField(
                label='Password',
                widget=forms.PasswordInput(
                    attrs={
                        'placeholder': 'password',
                        'class': 'form-control',
                        }
                    )
                )
    password2 = forms.CharField(
                label='Password',
                widget=forms.PasswordInput(
                    attrs={
                        'placeholder': 'repeat password',
                        'class': 'form-control',
                        }
                    )
                )

    class Meta:
        model = User
        fields = [
            'name',
            'surname',
            'email',
            'country',
            'password1',
            'password2',
        ]

    def clean_born(self):
        born = self.cleaned_data.get('born')
        if 1900 < born < datetime.date.today().year:
            return born
        else:
            raise forms.ValidationError("This is not a valid year.")

    def clean(self, *args, **kwargs):
        cleaned_data = super().clean()
        p1 = cleaned_data.get('password1')
        p2 = cleaned_data.get('password2')
        if (not p1 == p2) and p1 and p2:
            raise forms.ValidationError('Passwords do not match.')


class UserLoginForm(forms.ModelForm):
    email = forms.EmailField(
                label='Email',
                widget=forms.EmailInput(attrs={'class': 'form-control'})
                )
    password1 = forms.CharField(
                label='Password',
                widget=forms.PasswordInput(
                    attrs={
                        'placeholder': 'password',
                        'class': 'form-control',
                        }
                    )
                )

    class Meta:
        model = User
        fields = [
            'email',
            'password1',
        ]


class AddArtForm(forms.ModelForm):
    title = forms.CharField(
                label='title',
                widget=forms.TextInput(attrs={'class': 'form-control'}))
    year = forms.IntegerField(
                label='year',
                widget=forms.NumberInput(attrs={'class': 'form-control'}))
    style = forms.CharField(
                label='style',
                widget=forms.TextInput(attrs={'class': 'form-control'}))
    technique = forms.CharField(
                label='technique',
                widget=forms.TextInput(attrs={'class': 'form-control'}))
    medium = forms.CharField(
                label='medium',
                widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Umetnina
        fields = [
            'author',
            'title',
            'year',
            'style',
            'technique',
            'medium',
        ]

    def clean_year(self):
        made = self.cleaned_data.get('year')
        if 1900 < made < datetime.date.today().year:
            return made
        else:
            raise forms.ValidationError("This is not a valid year.")

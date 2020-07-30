from django.shortcuts import render
from django.views.generic import CreateView, TemplateView


from .models import User
from .forms import UserForm, UserLoginForm

# Create your views here.


class RegisterView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'account/register.html'

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            country = form.cleaned_data['country']
            mail = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            context = {
                'form': form,
                'name': name, 
                'surname': surname, 
                'mail': mail, 
                'country': country, 
                'password': password, 
                'password2': password2, 
            }
            form.save()
            return render(request, "account/profile.html", context)

        return render(request, 'account/register.html', {'form': form})


class LoginView(CreateView):
    model = User
    form_class = UserLoginForm
    template_name = 'account/login.html'


class ProfileView(TemplateView):
    template_name = 'account/profile.html'
    form = UserForm()


def profile_view(request):
    form = UserForm(request.GET)
    context={
        'name': request.GET.get('name'),
        'surname': request.GET.get('surname'),
        'mail': request.GET.get('Email'),
        'country': request.GET.get('Country'),
        'password': request.GET.get('Password'),
        }
    return render(request, 'account/profile.html', context)


def user_list_view(request):
    queryset = User.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'account/list.html', context)

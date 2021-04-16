from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from security.app_forms import forms
from piloto.app_forms.nomenclators import FormContact


class Login(LoginView):
    template_name = 'login.html'
    authentication_form = forms.FormAuthentication


class CreateAccount(CreateView):
    template_name = 'create_account.html'
    form_class = forms.FormWorker
    form_external_person = forms.FormExternalPerson
    form_user = forms.FormUser
    form_contact = FormContact
    success_message = 'Su cuenta se creó satisfactoriamente.'
    success_url = reverse_lazy('security:login')

    def get_context_data(self, **kwargs):
        context = super(CreateAccount, self).get_context_data(**kwargs)
        context['form_worker'] = self.get_form(self.form_class)
        context['form_external_person'] = self.get_form(self.form_external_person)
        context['form_user'] = self.get_form(self.form_user)
        context['form_contact'] = self.get_form(self.form_contact)
        return context

    def post(self, request, *args, **kwargform_usuarios):
        form_worker = self.form_class(request.POST, request.FILES)
        form_user = self.form_user(request.POST)
        form_contact = self.form_contact(request.POST, request=request)

        print(form_worker.errors, form_user.errors, form_contact.errors)
        if form_worker.is_valid() and form_user.is_valid() and form_contact.is_valid():
            worker = form_worker.save(commit=False)
            user = form_user.save()
            contact = form_contact.save()

            #user.is_active = False
            user.is_active = True
            user.save()

            worker.app_user = user
            worker.contact = contact
            worker.save()

            return HttpResponseRedirect('/')
        else:
            context = {
                'form_worker': form_worker,
                'form_user': form_user,
                'form_contact': form_contact,
            }
            return render(request, self.template_name, context)


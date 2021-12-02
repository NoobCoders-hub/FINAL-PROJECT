from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.core.mail import EmailMessage, message
from django.conf import settings
from django.contrib import messages
from .models import Appointment
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
import datetime
from django.template import Context
from django.template.loader import render_to_string, get_template


class pbookapt(TemplateView):
    template_name = "pbookapt.html"

    def post(self, request):
        fname = request.user.first_name
        lname = request.user.last_name
        email = request.user.email
        mobile = request.POST.get("mobile")
        message = request.POST.get("request")

        appointment = Appointment.objects.create(
            first_name=fname,
            last_name=lname,
            email=email,
            phone=mobile,
            request=message,
        )

        appointment.save()

        messages.add_message(request, messages.SUCCESS,
                             f"Thanks {fname} for making an appointment, we will email you ASAP!")
        return HttpResponseRedirect(request.path)


class dmanageapt(ListView):
    template_name = "dmanageapt.html"
    model = Appointment
    context_object_name = "appointments"
    login_required = True
    paginate_by = 3

    def post(self, request):
        date = request.POST.get("date")
        appointment_email = request.POST.get("appointment-email")
        appointment = Appointment.objects.get(email=appointment_email)
        appointment.accepted = True
        appointment.accepted_date = date
        appointment.save()

        data = {
            "email": appointment_email,
            "fname": appointment.first_name,
            "date": date,
        }

        message = get_template('email.html').render(data)
        email = EmailMessage(
            "About your Appointment",
            message,
            settings.EMAIL_HOST_USER,
            [appointment.email],
        )
        email.content_subtype = "html"
        email.send()

        messages.add_message(request, messages.SUCCESS, f"You accepted the appointment of {appointment.first_name}")
        return HttpResponseRedirect(request.path)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        appointments = Appointment.objects.all()
        context.update({
            "title": "Manage Appointments"
        })
        return context


class dviewapt(ListView):
    template_name = "dviewapt.html"
    model = Appointment
    context_object_name = "appointments"
    login_required = True
    paginate_by = 3

    def post(self, request):
        date = request.POST.get("date")
        Appointment.accepted = True
        Appointment.accepted_date = date

        data = {
            "date": date,
        }

        get_template('dviewapt.html').render(data)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        appointments = Appointment.objects.all()
        context.update({
            "title": "View Appointments"
        })
        return context
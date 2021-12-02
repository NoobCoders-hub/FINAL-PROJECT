from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.core.mail import EmailMessage, message
from django.conf import settings
from django.contrib import messages
from .models import Assessment
from django.contrib.auth.decorators import login_required
import datetime
from django.template import Context
from django.template.loader import render_to_string, get_template


class assessment(TemplateView):
    template_name = "assessment.html"
    login_required = True

    def post(self, request):
        User_Name = request.user.username
        Body_Temperature = request.POST.get("Body_Temperature")
        Symptom1 = request.POST.get("Symptom1")
        Symptom2 = request.POST.get("Symptom2")
        Symptom3 = request.POST.get("Symptom3")
        Symptom4 = request.POST.get("Symptom4")
        Symptom5 = request.POST.get("Symptom5")
        Symptom6 = request.POST.get("Symptom6")
        Symptom7 = request.POST.get("Symptom7")
        Symptom8 = request.POST.get("Symptom8")
        Symptom9 = request.POST.get("Symptom9")
        Medical_History1 = request.POST.get("Medical_History1")
        Medical_History2 = request.POST.get("Medical_History2")
        Medical_History3 = request.POST.get("Medical_History3")
        Medical_History4 = request.POST.get("Medical_History4")
        Medical_History5 = request.POST.get("Medical_History5")
        Medical_History6 = request.POST.get("Medical_History6")
        Other_Medical_History = request.POST.get("Other_Medical_History")
        Vaccinated = request.POST.get("Vaccinated")
        Vaccine_Name = request.POST.get("Vaccine_Name")
        Additional_Info = request.POST.get("Additional_Info")
        assessment = Assessment.objects.create(
            User_Name=User_Name,
            Body_Temperature=Body_Temperature,
            Symptom1=Symptom1,
            Symptom2=Symptom2,
            Symptom3=Symptom3,
            Symptom4=Symptom4,
            Symptom5=Symptom5,
            Symptom6=Symptom6,
            Symptom7=Symptom7,
            Symptom8=Symptom8,
            Symptom9=Symptom9,
            Medical_History1=Medical_History1,
            Medical_History2=Medical_History2,
            Medical_History3=Medical_History3,
            Medical_History4=Medical_History4,
            Medical_History5=Medical_History5,
            Medical_History6=Medical_History6,
            Other_Medical_History=Other_Medical_History,
            Additional_Info=Additional_Info,
            Vaccinated=Vaccinated,
            Vaccine_Name=Vaccine_Name,
        )

        assessment.save()

        messages.add_message(request, messages.SUCCESS,
                             f"Thanks for Taking the Assessment, we will email you ASAP!")
        return HttpResponseRedirect(request.path)
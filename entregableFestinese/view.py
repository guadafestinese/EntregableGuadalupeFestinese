from django.http import HttpResponse
from django.template import loader
from AppCoder.models import Persona

def homePage(self):
    persona = Persona.objects.all()
    data = {"Familia": persona}
    planilla = loader.get_template('home.html')
    documento = planilla.render(data)
    return HttpResponse(documento)
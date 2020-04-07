
from django.views.generic import CreateView
from app.models import StudentModel
from django.contrib.messages.views import SuccessMessageMixin
from app.forms import StudentForm

class CreateStudent(SuccessMessageMixin,CreateView):
    template_name = "index.html"
    success_url = '/index/'
    form_class = StudentForm
    model = StudentModel

    success_message = 'List successfully saved!!!!'
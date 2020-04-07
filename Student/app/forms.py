
from django import forms
from app.models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = StudentModel
        exclude = ('t_date',)

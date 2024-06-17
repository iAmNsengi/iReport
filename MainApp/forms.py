from django import forms
from .models import Data, Student, Course

class MarkForm(forms.ModelForm):
    student = forms.ModelChoiceField(queryset=Student.objects.all(), required=True)
    course = forms.ModelChoiceField(queryset=Course.objects.all(), required=True)

    class Meta:
        model = Data
        fields = ['student', 'course', 'cat1', 'cat2', 'fat', 'total']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(MarkForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['student'].queryset = Student.objects.filter(creator=user)
            self.fields['course'].queryset = Course.objects.filter(creator=user)
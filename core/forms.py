from django import forms
from django.contrib.auth import get_user_model
from core.models import Project, Milestone
import datetime

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('client', 'type', 'name', 'description', 'uploaded_files',)
    # client = forms.ModelChoiceField(queryset=get_user_model().objects.all())
    # name = forms.CharField(max_length=200)
    # type = forms.CharField(max_length=200)
    # description = forms.CharField(widget=forms.Textarea, required=False)
    # start_date = forms.DateField(required=False)
    # due_date = forms.DateField(required=False)

    # def save(self):
    #     p = Project(**self.cleaned_data)
    #     p.save()
    #     return p.id


class MilestoneForm(forms.ModelForm):
    amount = forms.DecimalField(max_digits=13, decimal_places=2)

    class Meta:
        model = Milestone
        fields = ('project', 'amount', 'name',)

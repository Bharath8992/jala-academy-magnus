from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    SKILL_CHOICES = [
        ('AWS', 'AWS'),
        ('QA-Automation', 'QA-Automation'),
        ('DevOps', 'DevOps'),
        ('Full Stack Developer', 'Full Stack Developer'),
        ('Middleware', 'Middleware'),
        ('WebServices', 'WebServices'),
    ]

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    mobile_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))

    gender = forms.ChoiceField(
        choices=[('Male', 'Male'), ('Female', 'Female')],
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'})
    )

    skills = forms.MultipleChoiceField(
        choices=SKILL_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        required=False
    )

    country = forms.ChoiceField(
        choices=[('', 'Select Country'), ('India', 'India'), ('USA', 'USA'), ('UK', 'UK')],
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    city = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Employee
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            if self.instance.skills:
                self.initial['skills'] = self.instance.skills.split(',')

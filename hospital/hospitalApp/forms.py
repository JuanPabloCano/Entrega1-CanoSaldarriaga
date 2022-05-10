from django import forms


class CreateDoctor(forms.Form):
    name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    age = forms.IntegerField()
    specialty = forms.CharField(max_length=255)
    entrance_time = forms.TimeField()
    exit_time = forms.TimeField()


class CreatePatient(forms.Form):
    name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    age = forms.IntegerField()
    medical_history = forms.CharField(max_length=500)


class CreateParent(forms.Form):
    name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    age = forms.IntegerField()
    medical_history = forms.CharField(max_length=500)
    patient_relantionship = forms.CharField(max_length=50)

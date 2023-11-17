from django import forms
from my_app.models import Contact,Quota

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'mesage','subject')

    def __init__(self, *args, **kwargs):
        super(ContactForm , self).__init__(*args, **kwargs)
        for field in self.fields:

            self.fields[field].widget.attrs.update({'class':'form-control'})
            self.fields[field].required = True

            self.fields['name'].widget.attrs.update({'placeholder':'adiniz'})
            self.fields['name'].label='adiniz'
            self.fields['email'].widget.attrs.update({'placeholder':'E-mailiniz'})
            self.fields['subject'].widget.attrs.update({'placeholder':'metn'})
            self.fields['mesage'].widget.attrs.update({'placeholder':'mesajlariniz','class':'message-box form-control','style':'height:300px'})
            self.fields['mesage'].label='mesaj'

class QuotaForm(forms.ModelForm):
    class Meta:
        model = Quota
        fields = ('name', 'email','service')

    def __init__(self, *args, **kwargs):
        super(QuotaForm , self).__init__(*args, **kwargs)
        for field in self.fields:

            self.fields[field].widget.attrs.update({'class':'form-control'})
            self.fields[field].required = True

            self.fields['name'].widget.attrs.update({'placeholder':'adiniz'})
            self.fields['name'].label='adiniz'
            self.fields['email'].widget.attrs.update({'placeholder':'E-mailiniz'})
            self.fields['service'].widget.attrs.update({'placeholder':'xidmetler'})
           

        


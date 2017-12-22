from django import forms

class ContactForm(forms.Form):
	subject = forms.CharField(label='Тема сообщения')
	email = forms.EmailField(required=False, label='Адрес Вашей электронной почты')
	message = forms.CharField(widget=forms.Textarea, label='Текст сообщения')

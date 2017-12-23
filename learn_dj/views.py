from django.shortcuts import render
from learn_dj.models import UserMessage, TextNew, LedMod_GTR2416, ArticleBox
from django.core.mail import send_mail
from datetime import datetime

now = datetime.now()

def main_page(request):
	html = TextNew.objects.order_by('date')[:4]
	gtr = LedMod_GTR2416.objects.all()[:1]
	art = ArticleBox.objects.filter(title='Обзор светодиодного модуля Koito')
	context = {'title_site': 'Автосвет', 'title_block_01': 'В мире автосвета', 'title_block_02': 'Обзоры', 'html': html, 'gtr': gtr, 'art': art}
	return render(request, 'learn_dj/templates/main_page.html', context)

def learning(request):
	html = LedMod_GTR2416.objects.all()

	context = {'title_site': 'Автосвет', 'title_block_01': 'Обзор светодиодного модуля GTR 2416', 'html': html}
	return render(request, 'learn_dj/templates/gtr_2416.html', context)

def articls(request):
	html = ArticleBox.objects.all()

	context = {'title_site': 'Автосвет', 'title_block_01': 'Обзор светодиодного модуля Koito', 'html': html}
	return render(request, 'learn_dj/templates/koito.html', context)

def contact(request):
	txt = UserMessage.objects.filter(public_message=True)
	context = {'title_site': 'Автосвет', 'title_block_01': 'Обратная связь', 'txt': txt}
	return render(request, 'learn_dj/templates/contact.html', context)

def map(request):

	context = {'title_site': 'Автосвет', 'title_block_01': 'Карта сайта'}
	return render(request, 'learn_dj/templates/map.html', context)

def answer(request):

	UserMessage.objects.create(user_name=request.POST.get('name') , comment=request.POST.get('comment'), email=request.POST.get('email'), date_of_note=now)
	send_mail(request.POST['name'], request.POST['comment'], request.POST.get('email', 'sempythonanywhere@gmail.com'), ['semensg2014@gmail.com'], fail_silently=False)
	answ = """Спасибо за Ваше обращение.
		__________________________________________

В случае заполнения Вами поля "Адрес Вашей электронной почты", Вам будет отправлен ответ"""
	context = {'title_block_01': 'Карта сайта', 'txtbl_01': answ}
	return render(request, 'learn_dj/templates/answer.html', context)

def auto_light_news(request):
	html = TextNew.objects.all()

	context = {'title_site': 'Автосвет', 'title_block_01': 'В мире автосвета', 'html': html}
	return render(request, 'learn_dj/templates/auto_light_news.html', context)

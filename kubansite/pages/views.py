from django.shortcuts import redirect, render
from pages.forms import ContactForm
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from kubansite.settings import RECIPIENTS_EMAIL


def success_view(request):
    return HttpResponse('Приняли! Спасибо за вашу заявку.')


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            body = {'first_name': form.cleaned_data['first_name'],
                    'legal_entity': form.cleaned_data['legal_entity'],
                    'inn': form.cleaned_data['inn'],
                    'phone_number': form.cleaned_data['phone_number'],
                    'e_mail': form.cleaned_data['e_mail'],
                    'region': form.cleaned_data['region'],
                    'sales_channel': form.cleaned_data['sales_channel'],
                    'nalog': form.cleaned_data['nalog'],
                    'theme': form.cleaned_data['theme'],
                    'text': form.cleaned_data['text']}
            ln = '\n'
            message = (f"Имя:{body['first_name']}{ln}"
                       f"Юр.лицо: {body['legal_entity']}{ln}"
                       f"ИНН:{body['inn']}{ln}"
                       f"Номер телефона:{body['phone_number']}{ln}"
                       f"e-mail:{body['e_mail']}{ln}"
                       f"Регион:{body['region']}{ln}"
                       f"Канал продаж:{body['sales_channel']}{ln}"
                       f"Вид налога:{body['nalog']}{ln}"
                       f"Тема сообщения:{body['theme']}{ln}"
                       f"Текст сообщения:{body['text']}")
            try:
                send_mail('Сообщение с контактной формы сайта',
                          message,
                          body['e_mail'],
                          RECIPIENTS_EMAIL)
            except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
            return redirect('success')
    form = ContactForm()
    return render(request, 'pages/index.html', {'form': form})

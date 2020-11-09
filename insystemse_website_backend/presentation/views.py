# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.response import Response

class NewMessage(GenericAPIView):
    def post(self, request):
        subject = 'Mensaje en web de Insystemse'
        sender = request.data.get('from')
        email = request.data.get('email')
        message = request.data.get('message')
        body = f'{sender} ({email}) envió: \n\n {message}'

        send_mail(subject, body, settings.EMAIL_HOST_USER, ['insystemse@gmail.com', 'faustom721@gmail.com'], fail_silently=False)
        return Response(200)
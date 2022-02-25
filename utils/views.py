import json

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Captcha


@api_view(['GET', 'POST'])
def new_captcha(request):
    try:
        data = json.loads(str(request.body, encoding='utf-8'))
        token = data.get('previous_token')
        c = Captcha.objects.filter(token=token).first()
        if c is not None:
            c.delete()
    except json.JSONDecodeError:
        pass
    c = Captcha.new_captcha()

    return Response({'url': c.url, 'token': c.token})
@api_view(['POST'])
def delete_captcha(request):
    try:
        data = json.loads(str(request.body, encoding='utf-8'))
        token = data.get('token')
    except json.JSONDecodeError:
        return Response(status=400)
    c = Captcha.objects.filter(token=token).first()
    if c is not None:
        c.delete()
    return Response(status=200)
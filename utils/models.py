import hashlib
import json
from urllib.request import Request, urlopen
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

class CreationModificationMixin(models.Model):
    created = models.DateTimeField(
        _("Created at"),
        auto_now_add=True
    )
    modified = models.DateTimeField(
        _("Modified at"),
        auto_now=True
    )
    class Meta:
        abstract = True

class Captcha(CreationModificationMixin):
    answer = models.TextField(editable=False, null=False)
    url = models.TextField(editable=False, null=False)
    token = models.TextField(editable=False, null=False, unique=True)
    @classmethod
    def new_captcha(cls):
        if settings.CAPTCHA == 'kocaptcha':
            new_captcha_url = f'https://{settings.KOCAPTCHA_HOST}/new'
            is_token_unique = False
            data = {}
            while is_token_unique is False:
                req = Request(new_captcha_url)
                if settings.KOCAPTCHA_AUTHORIZATION_HEADER:
                    req.add_header('Authorization', settings.KOCAPTCHA_AUTHORIZATION_HEADER)
                data = json.loads(str(urlopen(req).read(), encoding='utf-8'))
                is_token_unique = cls.objects.filter(token=data['token']).first() is None
            url = f"https://{settings.KOCAPTCHA_HOST}{data['url']}"
            return cls.objects.create(answer=data['md5'], url=url, token=data['token'])
        raise NotImplemented

    def check_answer(self, answer: str):
        if settings.CAPTCHA == 'kocaptcha':
            return self.answer == hashlib.md5(bytes(answer, encoding='utf-8')).hexdigest()
        raise NotImplemented

    def check_answer_and_delete(self, answer: str):
        r = self.check_answer(answer)
        self.delete()
        return r

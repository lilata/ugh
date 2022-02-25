from django.contrib.auth.models import User
from django.db import models
from utils.models import CreationModificationMixin
# Create your models here.


class Page(CreationModificationMixin):
    page_title = models.TextField(default='', blank=True)
    body_title = models.TextField(default='', blank=True)
    pic_url = models.URLField(null=True, blank=True)
    pic_alt = models.TextField(default='', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    summary = models.TextField(default='', blank=True)
    def __repr__(self):
        return f'Personal Web Page for {self.user.username}'
    def __str__(self):
        return self.__repr__()
    @property
    def summary_paragraphs(self):
        if not self.summary:
            return []
        else:
            return self.summary.split('\n')
    @property
    def get_pic_alt(self):
        if self.pic_alt:
            return self.pic_alt
        else:
            return f'{self.user.username}\'s Profile Picture'
    @property
    def get_page_title(self):
        if self.page_title:
            return self.page_title
        else:
            return f'{self.user.username}\'s Web Page'

    @property
    def get_body_title(self):
        if self.body_title:
            return self.body_title
        else:
            return f'{self.user.username}\'s Web Page'
    @property
    def has_nav_links(self):
        return NavLink.objects.filter(page=self).exists()
    @property
    def get_nav_links(self):
        return NavLink.objects.filter(page=self).all()
    @property
    def get_profile_tags(self):
        return ProfileTag.objects.filter(page=self).all()
    @property
    def get_user(self):
        return User.objects.filter(page=self).first()


class NavLink(CreationModificationMixin):
    text = models.CharField(max_length=100)
    url = models.URLField()
    page = models.ForeignKey(Page, on_delete=models.CASCADE, null=False)

class ProfileTag(CreationModificationMixin):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, null=False)
    tag = models.CharField(max_length=100, null=False)
    value = models.TextField(default='')

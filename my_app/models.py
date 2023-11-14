from django.db import models
from services.mixin import SlugMixin, DateMixin
from services.generator import Generator
from services.uploader import Uploader
from django.contrib.auth import get_user_model

User = get_user_model()


class Service(SlugMixin, DateMixin):
    title = models.CharField(max_length=255, verbose_name='xidmet adi')
    description = models.TextField(verbose_name='movzu')
    image = models.ImageField(upload_to=Uploader.upload_photo_to_service, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        verbose_name = 'xidet adi'
        verbose_name_plural = 'xidmet adlari'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=10, model_=Service)
        super(Service, self).save(*args, **kwargs)


class Quota(SlugMixin, DateMixin):
    name = models.CharField(max_length=255, verbose_name='ad')
    email = models.EmailField(verbose_name='email adresi')
    service = models.CharField(max_length=255, verbose_name='xidmetler')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'quota'
        verbose_name_plural = 'quotalar'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=10, model_=Quota)
        super(Quota, self).save(*args, **kwargs)


class Blog(SlugMixin, DateMixin):
    title = models.CharField(max_length=255, verbose_name='basliq')
    description = models.TextField(verbose_name='movzu')
    image = models.ImageField(upload_to=Uploader.upload_photo_to_blog, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        verbose_name = 'bloq'
        verbose_name_plural = 'bloqlar'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=10, model_=Blog)
        super(Blog, self).save(*args, **kwargs)


class Contact(SlugMixin, DateMixin):
    name = models.CharField(max_length=255, verbose_name='ad ve soyad')
    email = models.CharField(max_length=255, verbose_name='email adress')
    subject = models.CharField(max_length=255, verbose_name='movzu')
    mesage = models.TextField(verbose_name='mesaj')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'contact'
        verbose_name_plural = 'contactlar'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=10, model_=Contact)
        super(Contact, self).save(*args, **kwargs)


class Team(SlugMixin, DateMixin):
    name = models.CharField(max_length=255, verbose_name='ad')
    position = models.CharField(max_length=255, verbose_name='vezifesi')
    image = models.ImageField(upload_to=Uploader.upload_photo_to_team)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'comanda'
        verbose_name_plural = 'comanda'


class Testimonial(SlugMixin, DateMixin):
    description = models.TextField(verbose_name='metn')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.description[0:5]

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'istifadeci reyi'
        verbose_name_plural = 'istifadeci reyleri'


class Comment(DateMixin, SlugMixin):
    text = models.TextField(verbose_name="User's comment")
    blog = models.ForeignKey(Blog, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return self.text[:10]

    class Meta:
        ordering = ("-created_at", )
        verbose_name = "Rey"
        verbose_name_plural = "Reyler"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=10, model_=Comment)
        super(Comment, self).save(*args, **kwargs)

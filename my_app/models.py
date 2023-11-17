from django.db import models
from services.mixin import SlugMixin, DateMixin
from services.generator import Generator
from services.uploader import Uploader
from django.contrib.auth import get_user_model

SOCIAL_CHOICES = (
    ("insta", "Instagram"),
    ("fb", "Facebook"),
    ("wp", "WhatsApp"),
    ("twitter", "Twitter"),
    ("linkedin", "Linkedin"),
    ("tiktok", "Tiktok")
)

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


class Team(DateMixin):
    name = models.CharField(max_length=255, verbose_name='ad')
    position = models.CharField(max_length=255, verbose_name='vezifesi')
    image = models.ImageField(upload_to=Uploader.upload_photo_to_team)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'comanda'
        verbose_name_plural = 'comanda'


class Testimonial(DateMixin):
    description = models.TextField(verbose_name='metn')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    profesion = models.CharField(max_length=255, verbose_name='ixtisas', null=True, blank=True)

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
        ordering = ("-created_at",)
        verbose_name = "Rey"
        verbose_name_plural = "Reyler"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=10, model_=Comment)
        super(Comment, self).save(*args, **kwargs)


class AboutModel(DateMixin):
    title = models.CharField(max_length=255, verbose_name='title')
    sub_title = models.CharField(max_length=255, verbose_name='sub title')
    description = models.TextField(verbose_name='text')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "About"
        verbose_name_plural = "About"


class AboutSideBar(DateMixin):
    title_1 = models.CharField(max_length=255, verbose_name='title 1')
    desc_1 = models.TextField(verbose_name='description 1')
    image_1 = models.ImageField(upload_to=Uploader.upload_photo_to_about)

    title_2 = models.CharField(max_length=255, verbose_name='title 2')
    desc_2 = models.TextField(verbose_name='description 2')
    image_2 = models.ImageField(upload_to=Uploader.upload_photo_to_about)

    title_3 = models.CharField(max_length=255, verbose_name='title 3')
    desc_3 = models.TextField(verbose_name='description 3')
    image_3 = models.ImageField(upload_to=Uploader.upload_photo_to_about)

    def __str__(self):
        return f"{self.title_1},{self.title_2},{self.title_3}"

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "About Side Bar"
        verbose_name_plural = "About Side Bar"


class SosialMedia(DateMixin):
    sosial_name = models.CharField(max_length=255, verbose_name='sosial media hesabi', choices=SOCIAL_CHOICES)
    sosial_link = models.TextField(verbose_name='sosial media linki')

    def __str__(self):
        return self.sosial_name

    class Meta:
        ordering = ("sosial_name",)
        verbose_name = "sosial media hesabi"
        verbose_name_plural = "sosial media hesablari"


class Subscribe(DateMixin):
    email = models.EmailField(verbose_name='email')

    def __str__(self):
        return self.email

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "abune"
        verbose_name_plural = "abuneler"


class HomeSlider(DateMixin):
    title = models.CharField(max_length=255, verbose_name='title')
    image = models.ImageField(upload_to=Uploader.upload_photo_to_slider, verbose_name='slider image')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Home slider"
        verbose_name_plural = "Home sliders"


# class MainDetails(DateMixin):


class Emails(DateMixin):
    email = models.EmailField(verbose_name="Email")
    is_part = models.BooleanField(default=False)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Email"
        verbose_name_plural = "Emailler"


class Phones(DateMixin):
    phone = models.CharField(max_length=255, verbose_name="Phone number")

    def __str__(self):
        return self.phone

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Phone"
        verbose_name_plural = "Phones"


class Locations(DateMixin):
    location = models.CharField(max_length=255, verbose_name="Phone number")


    def __str__(self):
        return self.location

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Location"
        verbose_name_plural = "Locations"


class MainDetails(DateMixin):
    emails = models.ManyToManyField(Emails, verbose_name="Emails")
    locations = models.ManyToManyField(Locations, verbose_name="Locations")
    phones = models.ManyToManyField(Phones, verbose_name="Phones")

    logo = models.ImageField(upload_to=Uploader.upload_photo_to_logo)
    logo_name = models.CharField(max_length=255,verbose_name="Right side of logo")

    def __str__(self):
        return self.logo_name

    class Meta:
        ordering = ("-created_at", )
        verbose_name = "Main information"
        verbose_name_plural = "Main information"

from django.db import models
from django.utils import timezone


class Gonderi(models.Model):
    yazar = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    baslik = models.CharField(max_length=200)
    yazi = models.TextField()
    olustur_zaman = models.DateTimeField(
            default=timezone.now)
    yayim_zaman = models.DateTimeField(
            blank=True, null=True)

    def yayimla(self):
        self.yayim_zaman = timezone.now()
        self.save()

    def __str__(self):
        return self.baslik


class Post(models.Model):
    author1 = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title_max = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    deneme = models.TextField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title_max

class Alanlar(models.Model):
    m1 = models.BinaryField()
    m2 = models.BooleanField()
    m3 = models.DurationField()
    m4 = models.PositiveSmallIntegerField()
    m5 = models.SlugField()
    m6 = models.UUIDField()
    

    def __str__(self):
        return self.m1
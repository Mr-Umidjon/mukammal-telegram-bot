from django.db import models


# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(verbose_name="Ism", max_length=100)
    username = models.CharField(verbose_name='Telegram username', max_length=100, null=True)
    telegram_id = models.BigIntegerField(verbose_name='Telegram ID', unique=True, default=1)
    email = models.CharField(verbose_name="Email", max_length=50, null=True)

    def __str__(self):
        return f"{self.id} - {self.telegram_id} - {self.full_name}"


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    productname = models.CharField(verbose_name="Mahsulot nomi", max_length=50)
    photo = models.CharField(verbose_name='Rasim file_id', max_length=200, null=True)
    price = models.DecimalField(verbose_name='Narx', decimal_places=2, max_digits=8)
    description = models.TextField(verbose_name='Mahsulot haqida', max_length=3000, null=True)

    category_code = models.CharField(verbose_name="Katigoriya kodi", max_length=20)
    category_name = models.CharField(verbose_name="Katigoriya nomi", max_length=30)

    subcategory_code = models.CharField(verbose_name="Ost-katigoriya kodi", max_length=20)
    subcategory_name = models.CharField(verbose_name="Ost-katigoriya nomi", max_length=30)

    def __str__(self):
        return f"№ {self.id} - {self.productname}"


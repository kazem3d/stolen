from django.db import models

class steal(models.Model):

    class Meta:
        verbose_name='سرقت '
        verbose_name_plural='سرقت '


    title=models.CharField('عنوان',max_length=100)
    number=models.IntegerField('تعداد')
    date=models.DateField('تاریخ',null=True)
    location=models.CharField('موقعیت',max_length=100)
    price=models.IntegerField('میزان خسارت')
    description=models.TextField('توضیحات',null=True)

    def __str__(self):
        return self.title



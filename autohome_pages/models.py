from django.db import models


class MAP(models.Model):
    """
    Django 要求模型必须继承 models.Model 类。
    CharField 是字符型，
    CharField 的 max_length 参数指定其最大长度，超过这个长度的分类名就不能被存入数据库。
    Django 还为我们提供了多种其它的数据类型，如日期时间类型 DateTimeField、整数类型 IntegerField 等等。
    Django 内置的全部类型可查看文档：
    https://docs.djangoproject.com/en/1.10/ref/models/fields/#field-types
    """

    W_Brand = models.CharField(max_length=100)
    W_City = models.CharField(max_length=100)
    R_City = models.CharField(max_length=100)
    R_Province = models.CharField(max_length=100)
    R_Region = models.CharField(max_length=100)
    M_province_pinyin = models.CharField(max_length=100)
    M_province = models.CharField(max_length=100)


class LEVEL1(models.Model):

    score = models.CharField(max_length=100)
    Aspect = models.CharField(max_length=100)
    Brand = models.CharField(max_length=100)


class LEVEL2(models.Model):

    Brand = models.CharField(max_length=100)
    Dimension = models.CharField(max_length=100)
    keyindex = models.CharField(max_length=100)
    KeyModifier = models.CharField(max_length=100)
    SentenceAttitude = models.CharField(max_length=100)

class PURPOSE(models.Model):

    ForChild = models.CharField(max_length=100)
    ForWork = models.CharField(max_length=100)
    ForShopping = models.CharField(max_length=100)
    ForBusiness = models.CharField(max_length=100)
    ForCrossCountry = models.CharField(max_length=100)
    ForLongDistance = models.CharField(max_length=100)
    ForRacing = models.CharField(max_length=100)
    ForSelfDriving = models.CharField(max_length=100)
    ForCarry = models.CharField(max_length=100)
    ForGirls = models.CharField(max_length=100)
    Brand = models.CharField(max_length=100)
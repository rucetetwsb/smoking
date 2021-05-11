from django.db import models

# Create your models here.


class Borough(models.Model):
    boroughcode = models.AutoField(verbose_name='자치구 코드', primary_key = True)
    boroughname = models.CharField(max_length=64, verbose_name='자치구명')

    class Meta: #메타 클래스를 이용하여 테이블명 지정
        db_table = 'Borough'


class SmokingAreaType(models.Model):
    typecode = models.AutoField(verbose_name='유형 코드', primary_key = True)
    typename = models.CharField(max_length=64, verbose_name='유형 이름')

    class Meta: #메타 클래스를 이용하여 테이블명 지정
        db_table = 'SmokingAreaType'

class SmokingArea(models.Model):
    areacode = models.CharField(max_length=64, verbose_name='구역 코드')
    address = models.CharField(max_length=150, verbose_name='주소')
    boroughcode = models.ForeignKey(Borough, on_delete=models.CASCADE, related_name='borough_smoking', verbose_name='자치구 코드')
    typecode = models.ForeignKey(SmokingAreaType, on_delete=models.CASCADE, related_name='smoking_type', verbose_name='유형 코드')

    class Meta: #메타 클래스를 이용하여 테이블명 지정
        db_table = 'SmokingArea'

class Fine(models.Model):
    finecode = models.AutoField(verbose_name='과태료 코드', primary_key = True)
    finename = models.CharField(max_length=64, verbose_name='과태료 이름')
    finecontents = models.CharField(max_length=100, verbose_name='위반내용')
    fine = models.IntegerField(verbose_name="과태료")

    class Meta: #메타 클래스를 이용하여 테이블명 지정
        db_table = 'Fine'

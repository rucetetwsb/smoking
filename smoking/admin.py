from django.contrib import admin

# Register your models here.

from .models import Borough, SmokingAreaType, SmokingArea, Fine  #같은 경로의 models.py에서 User라는 클래스를 임포트한다.

# Register your models here.

class BoroughAdmin(admin.ModelAdmin) :
    list_display = ('boroughcode', 'boroughname')

admin.site.register(Borough, BoroughAdmin)


class SmokingAreaTypeAdmin(admin.ModelAdmin) :
    list_display = ('typecode', 'typename')

admin.site.register(SmokingAreaType, SmokingAreaTypeAdmin)

class SmokingAreaAdmin(admin.ModelAdmin) :
    list_display = ('areacode', 'address', 'boroughcode', 'typecode')

admin.site.register(SmokingArea, SmokingAreaAdmin)

class FineAdmin(admin.ModelAdmin) :
    list_display = ('finecode', 'finename', 'finecontents', 'fine')

admin.site.register(Fine, FineAdmin)
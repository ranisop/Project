from django.contrib import admin
from .models import Brand, Home, Middle, Product

# class BrandInline(admin.StackedInline):
#     model = Brand

# class HomeInline(admin.StackedInline):
#     model = Home

# class MiddleInline(admin.StackedInline):
#     model = Middle

# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name',)

admin.site.register(Brand)
admin.site.register(Home)
admin.site.register(Middle)
admin.site.register(Product)


# 관리자 계정 만들기
# python manage.py createsuperuser
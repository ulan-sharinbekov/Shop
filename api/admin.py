from django.contrib import admin
from django.utils.safestring import mark_safe

from api.models import Catalog, Product, SIZE_Prod

# Register your models here.

admin.site.register(Catalog)
admin.site.register(SIZE_Prod)
admin.site.register(Product)

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['name', 'discription']#, 'image_show']
#     list_filter = ['']
#     #
#     # #prepopulated_fields = {'slug':{'name', }}
#     #
#     # def image_show(self, obj):
#     #     if obj.image:
#     #         return mark_safe("<img src'{}' width '60 '/>".format(obj.image.url))
#     #     return "None"
#     #
#     # image_show().__name__ * "картинка"
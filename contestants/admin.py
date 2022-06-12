from django.contrib import admin
from .models import ContestType, ContestantForm


# Register your models here.
admin.site.register(ContestType)



class ContestantFormAdmin(admin.ModelAdmin):
    # def image_tag(self, obj):
    #     return format_html('<img src="{}" />'.format(obj.image.url))

    # image_tag.short_description = 'Image'

    list_display = ('name', 'reg_type', 'year_reg', 'verified', 'status', 'votes',)
    
    # readonly_fields = ('reg_image',)
    
    # def reg_image(self, obj):
    #     return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
    #         url = obj.headshot.url,
    #         width=obj.headshot.width,
    #         height=obj.headshot.height,
    #         )
    # )
admin.site.register(ContestantForm, ContestantFormAdmin)
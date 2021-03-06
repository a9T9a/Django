from django.contrib import admin
from django.utils.html import format_html
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

from product.models import Category,Product,Brand,Images


class ProductImageInline(admin.TabularInline):
    model=Images
    extra = 5


class CategoryAdmin(MPTTModelAdmin):
    list_display = ['title','status']
    list_filter = ['status', 'title']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','brand','price']
    readonly_fields = ['image_tag']
    list_filter = ['category','brand']
    inlines = [ProductImageInline]


class ImageAdmin(admin.ModelAdmin):
    list_display = ['title','product','image']


class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "name"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Product,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Product,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'


admin.site.register(Category,CategoryAdmin2)
admin.site.register(Product,ProductAdmin)
admin.site.register(Brand)
admin.site.register(Images,ImageAdmin)
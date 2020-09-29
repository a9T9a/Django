from django.db import models
from django.utils.safestring import mark_safe
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    STATUS={
        ('True','Evet'),
        ('false','Hayır')
    }
    title= models.CharField(max_length=30)
    keywords=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    image=models.ImageField(blank=True,upload_to='category_images/')
    status=models.CharField(max_length=10, choices=STATUS)
    slug=models.SlugField()
    parent=TreeForeignKey('self',blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_Insertion_by = ['title']

    def __str__(self):
        full_path = [self.title]
        k= self.parent
        while k is not None:
            full_path.append(k.title)
            k= k.parent
        return ' / '.join(full_path[::-1])


class Brand(models.Model):
    STATUS = {
        ('True', 'Evet'),
        ('false', 'Hayır')
    }
    title = models.CharField(max_length=30)
    image = models.ImageField(blank=True, upload_to='brand_images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    STATUS={
        ('True','Evet'),
        ('False','Hayır')
    }
    brand= models.ForeignKey(Brand, on_delete=models.CASCADE,default='')
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    title= models.CharField(max_length=30)
    keywords= models.CharField(max_length=255)
    description= models.CharField(max_length=255)
    image= models.ImageField(blank=True, upload_to='product_images/')
    price= models.FloatField()
    amount= models.IntegerField()
    detail= models.TextField()
    slug = models.SlugField()
    status= models.CharField(max_length=10,choices=STATUS)
    create_at= models.DateTimeField(auto_now_add=True)
    update_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img_src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'


class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to='images/')
    modified_image = models.ImageField(upload_to='modified_images/', null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self):
        self.modified_image.save(self.image.name, self.image, save=False)
        super(Images, self).save()




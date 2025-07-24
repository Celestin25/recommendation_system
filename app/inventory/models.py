from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
from inventory.choices import STATUS_CHOICES, RESOURCE_TYPES


class Category(models.Model):
    name = models.CharField(max_length=70)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    website = models.URLField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    categories = models.ManyToManyField(Category)
    quantity = models.PositiveIntegerField(
        help_text="This is the total quantity of this equipment in the lab"
    )
    quantity_available = models.PositiveIntegerField(
        help_text="This is the quantity available for booking"
    )
    main_image = CloudinaryField(
        'image', folder='fablab/equipments/images', null=True, blank=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='not_available')
    specifications = models.JSONField(blank=True, null=True)
    potential_suppliers = models.ManyToManyField(
        Supplier, related_name='potential_suppliers', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.id}"


class EquipmentImage(models.Model):
    image = CloudinaryField(
        'image', folder='fablab/equipments/images', null=True, blank=True)
    equipment = models.ForeignKey(
        Equipment, on_delete=models.CASCADE, related_name='images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Resource(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=20, choices=RESOURCE_TYPES)
    file = models.FileField(upload_to='resources/')
    equipment = models.ForeignKey(
        Equipment, on_delete=models.CASCADE, related_name='resources')
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ResourceLink(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    equipment = models.ForeignKey(
        Equipment, on_delete=models.CASCADE, related_name='extra_resources')
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

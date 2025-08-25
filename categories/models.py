from django.db import models

class Category(models.Model):
    name =  models.CharField(max_length=255, unique=True),
    image = models.ImageField(upload_to="categories",blank=True, null=True),
    created_at = models.DateTimeField(auto_now_add=True),
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"category of {self.name}"

class SubCategory(models.Model):
    name =  models.CharField(max_length=255, unique=True),
    image = models.ImageField(upload_to="subcategories",blank=True, null=True),
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcateries')
    created_at = models.DateTimeField(auto_now_add=True),
    update_at = models.DateTimeField(auto_now=True)

    '''class Meta:
        unique_together = ("Category", "name")'''

    def __str__(self):
        return f"sub_category of {self.category.name}"
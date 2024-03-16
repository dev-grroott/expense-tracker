from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    created_date = models.DateTimeField(default=timezone.now())
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "category"
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name}"

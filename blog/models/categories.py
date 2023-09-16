from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=40, blank=False, verbose_name="Name of category:")
    all_categories =models.Manager()

    def __str__(self):
        return self.name
   
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name']
   
    @staticmethod
    def get_category_by_id(ids):
        return Category.all_categories.filter(id_in=ids)


class SubCategory(models.Model):
    name = models.CharField(max_length=40, blank=False, verbose_name="Name of subcategory:")
    all_subcategories = models.Manager()
    
    def __str__(self):
        return self.name
    
    @staticmethod
    def get_subcategory_by_id(ids):
        return SubCategory.all_subcategories.filter(id_in=ids)

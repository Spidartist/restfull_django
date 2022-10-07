from django.db import models

class Recipe(models.Model):
    class Meta:
        db_table = 'recipe'
    title = models.CharField(max_length=100, null=False)
    making_time = models.CharField(max_length=100, null=False)
    serves = models.CharField(max_length=100, null=False)
    ingredients = models.CharField(max_length=300, null=False)
    cost = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now_add=True)



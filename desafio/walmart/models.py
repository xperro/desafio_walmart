from django.db import models

# Create your models here.

class products(models.Model):
    description = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    id = models.IntegerField(primary_key=True)

    class MongoMeta:
        db_table = "products"
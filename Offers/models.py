from django.db import models

class Offer(models.Model):
    """A class to represent single item"""
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=100)
    item_description = models.CharField(max_length=500)
    item_date_added = models.DateTimeField(auto_now_add = True)
    item_image = models.ImageField(upload_to ='uploaded_images/')
    item_price = models.FloatField()

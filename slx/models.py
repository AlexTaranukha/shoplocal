# Package imports
from django.db import models

# Class imports
from datetime import datetime as DateTime

# System models
class Error(models.Model):
    class Meta:
        db_table = 'error'
        ordering = ['-id']
    id = models.AutoField(primary_key = True, serialize = True)
    url = models.CharField(max_length = 500, null = True)
    message = models.CharField(max_length = 1000, null = True)
    stack_trace = models.CharField(max_length = 8000, null = True)
    datetime = models.DateTimeField()

class Status(models.Model):
    class Meta:
        db_table = 'status'
        ordering = ['id']
    id = models.AutoField(primary_key = True, serialize = True)
    name = models.CharField(max_length = 50)


# Abstract base models
class BaseModel(models.Model):
    class Meta:
        abstract = True
    id = models.AutoField(primary_key = True)
    status = models.ForeignKey(Status)
    created_datetime = models.DateTimeField()
    modified_datetime = models.DateTimeField(null = True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_datetime = DateTime.now()
        else:
            self.modified_datetime = DateTime.now()
        super(BaseModel, self).save(*args, **kwargs)


# Application models
class Affiliation(BaseModel):
    class Meta:
        db_table = 'affiliation'
        ordering = ['name']
    name = models.CharField(max_length = 100, null = False)


class Unit(BaseModel):
    class Meta:
        db_table = 'unit'
        ordering = ['name']
    name = models.CharField(max_length = 100, null = False)
    image = models.CharField(max_length = 200, null = False)
    affiliation = models.ForeignKey(Affiliation)


class User(BaseModel):
    class Meta:
        db_table = 'user'
        ordering = ['name']
    name = models.CharField(max_length = 100, null = False)
    login = models.CharField(max_length = 50, null = False)
    affiliation = models.ForeignKey(Affiliation)


class Placement(models.Model):
    class Meta:
        db_table = 'placement'
        ordering = ['name']
    name = models.CharField(max_length = 100, null = False)
    height = models.IntegerField()
    width = models.IntegerField()


class Ask(models.Model):
    class Meta:
        db_table = 'ask'
        ordering = ['name']
    name = models.CharField(max_length = 100, null = False)
    total_impressions = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    close_date = models.DateTimeField()
    min_impressions = models.IntegerField()
    min_price = models.DecimalField(max_digits = 9, decimal_places = 4, null = False)
    placement = models.ForeignKey(Placement)


class Bid(models.Model):
    class Meta:
        db_table = 'bid'
        ordering = ['-price']
    ask = models.ForeignKey(Ask)
    unit = models.ForeignKey(Unit)
    impressions = models.IntegerField()
    price = models.DecimalField(max_digits = 9, decimal_places = 4, null = False)


#class Fulfillment(models.Model):
#    class Meta:
#        db_table = 'fulfillment'
#        ordering = ['id']
#    bid = models.ForeignKey(Bid)
#    quantity = models.IntegerField()

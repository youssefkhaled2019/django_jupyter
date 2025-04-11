from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.name} the place"
    
    class Meta:
        app_label = 'oto'

class Restaurant(models.Model):
    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,  #  when a row is deleted from the parent table(Place), all rows in the child table (Restaurant) that reference the deleted row should also be deleted. 
        primary_key=True, #hidden
    )
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return "%s the restaurant" % self.place.name
    class Meta:
        app_label = 'oto'

class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)#,db_constraint=False
    name = models.CharField(max_length=50)
    class Meta:
        app_label = 'oto'

    def __str__(self):
        return "%s the waiter at %s" % (self.name, self.restaurant)
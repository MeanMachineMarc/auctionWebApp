from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db.models import CheckConstraint, Q
import json

class Account(models.Model): 
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    address=models.CharField(max_length=200)
    balance=models.DecimalField(decimal_places=2, max_digits=10, default=0, validators=[MinValueValidator(0)])

    class Meta:
        constraints = (
            CheckConstraint(
                check=Q(balance__gte=0), 
                name="minBalance"),
            )

    def __str__(self):
        return str(self.id)
    
class Item(models.Model): 
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    postageCost = models.DecimalField(decimal_places=2, max_digits=10)
    bidIncrement = models.DecimalField(decimal_places=2, max_digits=10)
    conditionChoices = [
        ("new", "New"),
        ("excellent", "Excellent"),
        ("good", "Good"),
        ("used", "Used"),
        ("refurbished", "Refurbished"),
        ("partsOnly", "Parts Only"),
    ]
    condition = models.CharField(max_length=20, choices=conditionChoices)
    endDateTime = models.DateTimeField()
    acceptReturns = models.BooleanField(default=False)
    description = models.TextField(max_length=1000)
    numBids = models.IntegerField(default=0)
    bidders = models.CharField(max_length=999999999, default='[]')
    ended = models.BooleanField(default=False)
    sold = models.BooleanField(default=False)
    buyer = models.ForeignKey(Account, to_field="id", on_delete=models.DO_NOTHING, related_name="bId", blank=True, null=True)
    seller = models.ForeignKey(Account, to_field="id", on_delete=models.DO_NOTHING, related_name="sId", blank=True, null=True)
    destinationAddress = models.CharField(max_length=200, blank=True, null=True)
    transactionSuccess = models.BooleanField(blank=True, null=True)
    categories = [
        ("bOIS", "Business, Office & Industrial Supplies"),
        ("hB", "Health & Beauty"),
        ("f", "Fashion"),
        ("e", "Electronics"),
        ("hG", "Home Garden"),
        ("sHL", "Sports, Hobbies & Leisure"),
        ("mt", "Motors"),
        ("cA", "Collectables & Art"),
        ("mda", "Media"),
        ("o", "Other"),
    ]
    category = models.CharField(max_length=50, choices=categories)
 
    def getBidders(self):
        return json.loads(self.bidders)
    
    def setBidders(self, value):
        self.bidders = json.dumps(value)

    biddersProperty = property(getBidders, setBidders)

    def __str__(self):
        return self.name

    
class Movie(models.Model):
    title = models.CharField(max_length=300)
    yearOfRelease = models.CharField(max_length=4)
    runtime = models.CharField(max_length=5)
    rating = models.CharField(max_length=5)
    votes = models.CharField(max_length=300)
    gross = models.CharField(max_length=300)
    posterURL = models.CharField(max_length=300)

    def __str__(self):
        return self.title
import uuid
from django.db import models
from python_test.constants import optional

class Client(models.Model):
    """
    Client model representation in the database
    """

    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    code = models.CharField(default='', max_length=500, **optional)
    client_name = models.CharField(default='', max_length=1000, unique=True)
    contact_name = models.CharField(default='', max_length=500, **optional)
    street_name = models.CharField(default='', max_length=500, **optional)
    suburb_name = models.CharField(default='', max_length=500, **optional)
    post_code = models.CharField(default='', max_length=500, **optional)
    state = models.CharField(default='', max_length=500, **optional)
    email = models.CharField(default='', max_length=500)
    phone_number = models.CharField(default='', max_length=500)

    class Meta: 
        verbose_name_plural = 'clients'
        verbose_name = 'client'

    def __str__(self):
        return self.client_name

    def save(self, *args, **kwargs):
        self.code = uuid.uuid4().hex[:6].upper()
        super(Client, self).save(*args, **kwargs)
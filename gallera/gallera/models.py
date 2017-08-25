from django.db import models
from concurrency.fields import AutoIncVersionField

class ManagedTVModel(models.Model):
    """Model including optimistic version control field (the V in the class
    name), and creation/update timestamps fields (the T in the class name), but
    managed by Django.

    this is the same as the VersionedTimestampedModel, but *WITHOUT* the hack
    required to get record IDs from the DB that we have to use with the tables
    from the original CCAPI and the way Grails defined them.
    """
    version = AutoIncVersionField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
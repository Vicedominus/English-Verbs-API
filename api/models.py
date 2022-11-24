from django.db import models

# Create your models here.
class Verb(models.Model):

    VERB_CLASSIFICATION = (
        ('regular', 'Regular'),
        ('irregular', 'Irregular'),
    )

    classification = models.CharField(max_length=10, choices=VERB_CLASSIFICATION)
    present_simple = models.CharField(max_length=32, unique=True)
    simple_past = models.CharField(max_length=32)
    past_participle = models.CharField(max_length=32)


    def __str__(self) -> str:
        """Return the simple form of the verb as string representation"""
        return self.present_simple


        
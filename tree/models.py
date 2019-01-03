from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.core.exceptions import ValidationError


class Employees(MPTTModel):
    class MPTTMeta:
        order_insertion_by = ['name']  # By which field to sort childrens in tree
        
    name = models.CharField(max_length=150, db_index=True)
    position = models.CharField(max_length=150, db_index=True)
    emp_date = models.DateField(db_index=True)
    salary = models.IntegerField(db_index=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    photo = models.ImageField(upload_to='empl_photo', default='1.jpg', blank=True)
    photo_thumbnail = ImageSpecField(
        source='photo',
        processors=[ResizeToFill(50, 50)],
        format='JPEG',
        options={'quality': 60}
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.emp_date = '2019-01-01'
        super(Employees, self).save(*args, **kwargs)

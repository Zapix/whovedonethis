from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class CreatedByMixin(models.Model):
    created_by = models.ForeignKey(User, verbose_name=_('Created by'),
        related_name='%(class)s_created_items', 
    )
    
    class Meta:
        abstract=True

class UpdatedByMixin(models.Model):
    updated_by = models.ForeignKey(User, verbose_name=_('Updated by'),
        related_name='%(class)s_updated_items',
    )
    
    class Meta:
        abstract = True

class CreatedUpdatedByMixin(CreatedByMixin, UpdatedByMixin):
    class Meta:
        abstract = True
        

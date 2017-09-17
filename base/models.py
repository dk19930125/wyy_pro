from django.db import models
from django.utils import timezone
# Create your models here.


class DLEditableModel(models.Model):
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    deleted = models.DateTimeField(default=None, null=True)
    editable = models.BooleanField(default=True)

    editable_fields = []

    class Meta:
        abstract = True

    def update(self, save=True, **kwargs):
        if not self.editable:
            return self, []

        updated_fields = []
        for field in self.editable_fields:
            if kwargs.has_key(field):
                if getattr(self, field) != kwargs.get(field):
                    setattr(self, field, kwargs.get(field))
                    updated_fields.append(field)

        if save and updated_fields:
            self.save(update_fields=updated_fields + ['updated'])
            self.refresh_from_db(fields=updated_fields)  # TODO: if updated_fields contain foreign key, than refresh
        return self, updated_fields

    def set_deleted(self, save=False):
        self.deleted = timezone.now()
        if save:
            self.save(update_fields=["deleted", ])
        return self

    def delete(self, using=None):
        self.set_deleted(True)
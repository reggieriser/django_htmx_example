import uuid

from django.db import models


class DutyLocation(models.Model):
    Affiliation = models.TextChoices("Affiliation", "ARMY NAVY MARINES AIR_FORCE COAST_GUARD OTHER")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    affiliation = models.CharField(max_length=255, choices=Affiliation.choices, blank=True, null=True)
    # Address and TransportationOffice can be added later if desired
    provides_services_counseling = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "milmove_duty_locations"
        indexes = [
            models.Index(fields=["name"]),
        ]

    def __str__(self):
        return self.name


class DutyLocationName(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    duty_location = models.ForeignKey(DutyLocation, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "milmove_duty_location_names"

    def __str__(self):
        return self.name

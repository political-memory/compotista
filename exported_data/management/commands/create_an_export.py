import json
import hashlib

from django.utils import timezone
from django.core.management.base import BaseCommand

from representatives.utils import export_all_representatives, export_active_representatives
from exported_data.models import ExportedRevision

class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        self.create_export(json.dumps(export_all_representatives(), indent=4))
        self.create_export(json.dumps(export_active_representatives(), indent=4), 'active')
        

    def create_export(self, data, kind=None):
        checksum = hashlib.sha256(data).hexdigest()
        exported_revision = ExportedRevision.objects.filter(checksum=checksum)

        now = timezone.now()

        if exported_revision:
            exported_revision = exported_revision[0]
            exported_revision.last_check_datetime = now
            exported_revision.kind = kind
            exported_revision.save()
        else:
            ExportedRevision.objects.create(
                data=data,
                kind=kind,
                checksum=hashlib.sha256(data).hexdigest(),
                creation_datetime=now,
                last_check_datetime=now
            )

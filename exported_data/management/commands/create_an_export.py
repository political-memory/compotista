import json
import hashlib

from datetime import datetime

from django.core.management.base import BaseCommand

from representatives.utils import export_all_representatives
from exported_data.models import ExportedRevision

class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        data = json.dumps(export_all_representatives(), indent=4)
        ExportedRevision.objects.create(
            data=data,
            checksum=hashlib.sha256(data).hexdigest(),
            datetime=datetime.now()
        )

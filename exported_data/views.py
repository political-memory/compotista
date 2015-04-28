from .models import ExportedRevision
from django.http import HttpResponse


def get_lastest_data(request, kind=None):
    exported_revision = ExportedRevision.objects.filter(kind=kind).latest('last_check_datetime')
    return HttpResponse(exported_revision.data)
    

def get_lastest_checksum(request, kind=None):
    print(kind)
    return HttpResponse(ExportedRevision.objects.latest('last_check_datetime').checksum)

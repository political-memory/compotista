from .models import ExportedRevision
from django.http import HttpResponse, HttpResponseNotFound


def get_lastest_data(request, kind=None):
    exported_revision = ExportedRevision.objects.filter(kind=kind)
    if not exported_revision:
        return HttpResponseNotFound('<h1>Page not found</h1>')

    return HttpResponse(exported_revision.latest('last_check_datetime').data)
    

def get_lastest_checksum(request, kind=None):
    exported_revision = ExportedRevision.objects.filter(kind=kind)
    if not exported_revision:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    return HttpResponse(exported_revision.latest('last_check_datetime').checksum)

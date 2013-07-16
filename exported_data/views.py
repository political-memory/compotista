from .models import ExportedRevision
from django.http import HttpResponse

def get_lastest_data(request):
    return HttpResponse(ExportedRevision.objects.latest('last_check_datetime').data)

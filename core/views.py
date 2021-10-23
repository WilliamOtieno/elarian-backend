from django.http import HttpResponse
from .utils import randomNumber


def send_2fa(request):
    two_fa_code = str(randomNumber(6))
    print(two_fa_code)
    print('sent')
    return HttpResponse(two_fa_code)

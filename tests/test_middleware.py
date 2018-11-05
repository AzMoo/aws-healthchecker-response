from aws_healthchecker_response.middleware import \
    AWSHealthCheckerResponseMiddleware
from django.http.response import HttpResponse
from mock import Mock


def get_response(request):  # pylint: disable=unused-argument
    return HttpResponse('NOT FROM MIDDLEWARE')


def test_elb_user_agent_returns_ok():

    request = Mock()
    request.META = {
        'User-Agent': "ELB-HealthChecker/2.0"
    }
    request.path = '/'

    mw = AWSHealthCheckerResponseMiddleware(get_response)
    response = mw(request)
    assert response.status_code == 200
    assert response.content == b'OK'


def test_no_ua_returns_something_else():
    request = Mock()
    request.path = '/'

    mw = AWSHealthCheckerResponseMiddleware(get_response)
    response = mw(request)
    assert response.status_code == 200
    assert response.content == b'NOT FROM MIDDLEWARE'

#coding: utf-8
import base64
import json
from functools import wraps

from django.http import HttpResponse, HttpResponseForbidden
from django.core.exceptions import PermissionDenied
from django.contrib.auth import authenticate, login


def jsonize(func):
    @wraps
    def _(*a, **kw):
        content = func(*a, **kw)
        return json.dumps(content)
    return _


def make_json_response(data):
    data = json.dumps(data)
    return HttpResponse(data, mimetype='application/json')


def basic_auth_api(request):
    if request.user and not request.user.is_anonymous():
        return True

    if 'HTTP_AUTHORIZATION' in request.META:
        auth = request.META['HTTP_AUTHORIZATION'].split()
        if len(auth) == 2:
            if auth[0].lower() == "basic":
                try:
                    username, password = base64.b64decode(auth[1]).split(':')
                    user = authenticate(username=username, password=password)
                    if user and not user.is_anonymous():
                        return True
                except Exception as err:
                    pass

    return False

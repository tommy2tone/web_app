from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.renderers import render_to_response
from pyramid.security import (
    remember,
    forget,
    )
from pyramid.view import (
    forbidden_view_config,
    view_config,
)
import datetime
import transaction

from .. import models


@view_config(route_name='login', renderer='../templates/login.jinja2')
def login(request):
    if 'form.submitted' in request.params:
        email = request.params['email']
        password = request.params['password']
        user = request.dbsession.query(models.User).filter(models.User.email == email).first()

        if user is None:
            return {'message': 'Email cannot be found.  Please create an account.'}

        if user.temp_password != 'Null' and user.check_temp_password(password):
            temp_password_confirmed_on = datetime.datetime.now().timestamp()
            if (float(temp_password_confirmed_on) - float(user.temp_password_sent)) < 86400:
                user.temp_password_confirmed_on = temp_password_confirmed_on
                # user.temp_password = 'Null'
                transaction.commit()
                return HTTPFound(request.route_url('reset_password'))
            else:
                user.temp_password_confirmed_on = temp_password_confirmed_on
                user.temp_password = 'Null'
                transaction.commit()
                return {'message': 'The temporary password has expired.  Please reset.'}

        if not user.check_password(password):
            return {'message': 'Incorrect password.  Please try again.'}
        if user.email_confirmed != 1:
            return {'message': 'Your email has not been confirmed'}

        if user is not None and user.check_password(password):
            headers = remember(request, user.id, max_age='3600')
            return HTTPFound(request.route_url('user_home'), headers=headers)
    return {}


@view_config(route_name='logout')
def logout(request):
    headers = forget(request)
    next_url = request.route_url('home')
    return HTTPFound(location=next_url, headers=headers)

@forbidden_view_config()
def forbidden_view(request):
    next_url = request.route_url('login', _query={'next': request.url})
    return HTTPFound(location=next_url)
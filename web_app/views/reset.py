from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.renderers import render_to_response
from pyramid.security import remember, forget
from pyramid.view import forbidden_view_config, view_config
from .. import models
from ..send_email import send_confirmation_email
from ..valid_password import valid_password
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
import secret
from random_password import random_password
import random
import datetime
import transaction

confirm_serializer = URLSafeTimedSerializer(secret.secret)


@view_config(route_name='reset_email', renderer='../templates/reset_email.jinja2')
def reset_email(request):
    if 'form.submitted' in request.params:
        email = request.params['email_name']

        # If statement to check if user exist in db.  If True, generate temp password, store in
        # database, and email temp password to user.

        if request.dbsession.query(models.User).filter(models.User.email == email).count() == 1:
            user = request.dbsession.query(models.User).filter(models.User.email == email).first()
            password_length = random.randrange(8, 32)
            temp_password = random_password(password_length)
            user.temp_password_sent = datetime.datetime.now().timestamp()
            user.temp_password = user.set_password(temp_password)
            transaction.commit()
            body = f'Please use temporary password to login: {temp_password}'
            send_confirmation_email(email, body)
            msg = 'Please check email for temporary password and return to the Login page.'
            next_url = request.route_url('login')
            return {'message': msg, 'link': next_url, 'label': 'Login'}



        # Add else block to inform user email does not exist and to try again or create account
        else:
            next_url = request.route_url('register')
            msg = "The email entered does not exist.  Please try again or create an account."
            return {'message': msg, 'link': next_url, 'label': 'Register'}

    return {}


@view_config(route_name='reset_password', renderer='../templates/reset_password.jinja2')
def reset_password(request):
    #   Retrieve form data
    if 'form.submitted' in request.params:
        email = request.params['email_name']
        new_password = request.params['password']
        new_reenter_password = request.params['reenter_password']

        if new_password != new_reenter_password:
            return {'message': 'Passwords do not match.  Try again.'}

        #   Helper functions to check password length, types of characters, and if the two form fields match
        if valid_password(new_password) != True:
            return {'message': valid_password(new_password)}

        # Update user information
        user = request.dbsession.query(models.User).filter(models.User.email == email).first()
        user.password_hash = user.set_password(new_password)
        user.temp_password = 'Null'

        # Commit updates to db
        transaction.commit()

        return {'message': 'Password reset successful!'}

    return {}




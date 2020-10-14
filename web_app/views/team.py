from pyramid.view import view_config
from pyramid.response import Response


@view_config(route_name='team', renderer='../templates/team.jinja2')
def my_view(request):
    return {}
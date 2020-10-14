import os
import uuid
import shutil
from pathlib import Path
from pyramid.response import Response
from pyramid.view import forbidden_view_config, view_config
from pyramid.httpexceptions import (
    HTTPForbidden,
    HTTPFound,
    HTTPNotFound,
    )


@view_config(route_name='user_home', renderer='../templates/user_home.jinja2')
def register(request):
    user = request.user
    if user is None:
        raise HTTPForbidden

    """The following is to upload csv and ofx file types.  The code checks if the file
    exist and prompts the user to confirm if they want to overwrite."""

    if request.method == 'POST':
        filename = request.params['file'].filename
        input_file = request.POST['file'].file
        directory = '/Users/tommt/Desktop/upload_test'
        file_ext = Path(filename).suffix
        file_path = os.path.join('/Users/tommt/Desktop/upload_test', '%s' + file_ext) % uuid.uuid4()
        temp_file_path = file_path + '~'
        input_file.seek(0)

        if file_ext == ".csv" or file_ext == ".ofx":
            with open(temp_file_path, "wb") as output_file:
                shutil.copyfileobj(input_file, output_file)
            f_name = os.listdir(directory)
            if filename in f_name:
                return Response("File exist.  Do you want to Overwrite?")
            else:
                file_path = os.path.join('/Users/tommt/Desktop/upload_test', filename)
            os.rename(temp_file_path, file_path)
            return Response('OK')
        else:
            return Response('Unsupported file type.  Please try again.')


    return {}
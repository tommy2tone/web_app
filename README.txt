web_app
==============

Getting Started
---------------

- Change directory into your newly created project.

    cd web_app

- Create a Python virtual environment.

    python3 -m venv env

- Upgrade packaging tools.

    env/bin/pip install --upgrade pip setuptools

- Install the project in editable mode with its testing requirements.

    env/bin/pip install -e ".[testing]"

- Initialize and upgrade the database using Alembic.
    # Skip this step for now
       - Generate your first revision.

        env/bin/alembic -c development.ini revision --autogenerate -m "init"

    - Upgrade to that revision.

        env/bin/alembic -c development.ini upgrade head

- Create and edit config files from templates

    cp email_config_TEMPLATE.py email_config.py
    cp secret_TEMPLATE.py secret.py
    vim -p email_config.py secret.py

  In your secret.py file you will need a random string of characters.
  Here is a quick way to generate them:
  >>> import random, string
  >>> ''.join(random.choice(string.ascii_letters + string.digits) for i in range(20))

- Load default data into the database using a script.

    env/bin/initialize_web_app_db development.ini

- Run your project's tests.

    env/bin/pytest

- Run your project.

    env/bin/pserve development.ini

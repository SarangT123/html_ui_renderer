from jinja2 import Template
import webbrowser
from secrets import token_urlsafe
import os
from datetime import datetime


# renders a string on the browsers


def render_string(data: str):
    """
    Render a string with the given context.
    """
    temp = token_urlsafe(16)
    try:
        with open(f'temp/{temp}.html', 'w') as f:
            f.write(data)
    except FileNotFoundError as f:
        print('temp folder not found making a new one')
        os.mkdir('temp')
        with open(f'temp/{temp}.html', 'w') as f:
            f.write(data)
    return f'temp/{temp}.html'

# Template renderer


def render_template(template_name: str, **kwargs):
    """"
    Render a template with the given context.
    """
    with open(template_name, 'r') as f:
        template_string = f.read()
    template = Template(template_string)
    return render_string(template.render(**kwargs))

# Render decorator


def view(func):
    """decorator to be used above functions to render their return statement"""
    def wrapper():
        x = func()
        print('opening in browser')
        webbrowser.open(f'{x}')
        return True
    return wrapper

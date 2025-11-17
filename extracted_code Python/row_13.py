bash
pip install jinja2
from jinja2 import Environment, FileSystemLoader
import os

def render_template(template_name, **kwargs):
    """
    Render an HTML template with Jinja2. This function will not escape any user input automatically; 
    you should ensure that your inputs are safe if they come from users to avoid XSS (Cross-Site Scripting) attacks.
    
    :param template_name: The name of the HTML template file to load.
    :param kwargs: A dictionary of variables to pass to the template.
    """
    # Set up Jinja2 environment with a default directory for templates
    basedir = os.path.dirname(os.path.abspath(__file__)) if __file__ else '.'
    env = Environment(loader=FileSystemLoader(basedir), autoescape=True)
    
    # Load the template from the environment
    template = env.get_template(template_name)
    
    # Render the template with the provided context (kwargs)
    rendered_html = template.render(**kwargs)
    
    return rendered_html

# Example usage:
if __name__ == "__main__":
    # Define a simple HTML template as a string or load from a file
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{{ title }}</title>
    </head>
    <body>
        <h1>{{ header }}</h1>
        <p>User input: {{ user_input }}</p>
    </body>
    </html>
    """
    
    # Prepare the data to be passed to the template
    context = {
        'title': 'Jinja2 Example',
        'header': 'Welcome to Jinja2 Template Rendering',
        'user_input': '<script>alert("XSS")</script>'  # This would normally come from a user input field
    }
    
    # Render the template with user-provided data
    rendered = render_template('example_template.html', **context)
    
    print(rendered)
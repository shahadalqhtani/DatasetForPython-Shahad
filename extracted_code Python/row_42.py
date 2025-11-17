bash
pip install flask
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Simple template for error pages
ERROR_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Error</title>
</head>
<body>
    <h1>An Error Occurred: {{ error }}</h1>
    <p>{{ exception }}</p>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Simulate form data
            data = request.form['data']
            if not data:
                raise ValueError("Data cannot be empty")
            return f"Form submitted successfully with data: {data}"
        except Exception as e:
            # Render the error page with raw exception details
            return render_template_string(ERROR_TEMPLATE, error="Form Submission Error", exception=str(e))
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Simple Form</title>
    </head>
    <body>
        <h1>Submit Some Data</h1>
        <form method="post">
            <input type="text" name="data" placeholder="Enter data">
            <button type="submit">Submit</button>
        </form>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
bash
python app.py
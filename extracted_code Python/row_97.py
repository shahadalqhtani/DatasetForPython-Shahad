sh
pip install flask wtforms
from flask import Flask, render_template, request
import re

app = Flask(__name__)

class UserForm(FlaskForm):
    pattern = StringField('Pattern', validators=[DataRequired()])
    data = StringField('Data', validators=[DataRequired()])
    submit = SubmitField('Match')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UserForm()
    result = None

    if request.method == 'POST' and form.validate_on_submit():
        user_pattern = form.pattern.data
        data = form.data.data

        match = re.match(user_pattern, data)
        if match:
            result = f"Match found! {match.group()}"
        else:
            result = "No match found."

    return render_template('index.html', form=form, result=result)

if __name__ == '__main__':
    app.run(debug=True)
html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Regex Match Form</title>
    <!-- Add any additional CSS or JS links here -->
</head>
<body>
    <div class="container">
        <h1>Regex Match Form</h1>
        <form method="POST">
            {{ form.hidden_tag() }}
            {{ form.pattern.label }} {{ form.pattern(size=30) }}<br><br>
            {{ form.data.label }} {{ form.data(size=30) }}<br><br>
            {{ form.submit() }}
        </form>
        {% if result %}
            <h2>{{ result }}</h2>
        {% endif %}
    </div>
</body>
</html>
sh
python app.py
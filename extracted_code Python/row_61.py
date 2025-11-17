from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

# In a real application, you should store this securely (e.g., using environment variables)
app.secret_key = 'your-very-secret-key'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        action = request.form['action']
        
        if action == 'submit':
            # Perform the state-changing action here
            # For demonstration, let's just print a message
            print("State changed!")
            return redirect(url_for('index'))
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Flask State Change Form</title>
</head>
<body>
    <h1>State Change Form</h1>
    <form method="post">
        <input type="hidden" name="action" value="submit">
        <button type="submit">Submit Action</button>
    </form>
</body>
</html>
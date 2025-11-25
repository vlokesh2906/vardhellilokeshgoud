from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML form from Task #3
login_form_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Login Form</title>
</head>
<body>
    <h2>Login</h2>
    <form method="POST">
        <label for="username">Username:</label><br>
        <input type="text" id="username" name="username" required><br>
        <label for="password">Password:</label><br>
        <input type="password" id="password" name="password" required><br><br>
        <input type="submit" value="Login">
    </form>
    {% if result %}
        <p>{{ result }}</p>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def login():
    result = None
    if request.method == 'POST':
        username = request.form.get('username')
        # Here, you would add real authentication logic
        print(f"User logged in: {username}")
        result = f"Login successful! Welcome, {username}."
    return render_template_string(login_form_html, result=result)

if __name__ == "__main__":
    app.run(debug=True)

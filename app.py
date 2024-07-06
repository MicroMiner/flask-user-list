
from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

# Liste
users = []

@app.route('/', methods=["GET"])
def index():
    return render_template("index.html", users=users)

@app.route('/add_user', methods=["POST"])
def add_user():
    user = request.form.get("user")
    users.append(user)
    return redirect(url_for("index"))

@app.route('/del_user', methods=["POST"])
def del_user():
    user_to_del = request.form.get("user_to_del")
    if user_to_del in users:
        users.remove(user_to_del)
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)
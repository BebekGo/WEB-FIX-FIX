from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def show_hello():
    return render_template('index.html')

@app.route("/about_me")
def show_about_me():
    return render_template('about_me.html')

@app.route("/projects")
def show_projects():
    return render_template('projects.html')

@app.route("/contact")
def show_contact():
    return render_template('contact.html')

@app.route("/template")
def show_template():
    return render_template('template.html')

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, session, url_for, redirect, render_template, request, abort, flash

app = Flask(__name__)

@app.errorhandler(404)
def FUN_404(error):
    return render_template("page_404.html"), 404

@app.route("/")
def FUN_root():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
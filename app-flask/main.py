from flask import Flask, render_template

app = Flask(__name__)
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

@app.route("/")
def hello():
    return render_template('index.jade')

if __name__ == "__main__":
	app.debug = True
	app.run(host="0.0.0.0", port=5000)
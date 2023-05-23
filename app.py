from flask import *
import os

os.system("npm run tw")

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/static/<file_name>")
def static_router(file_name):
	try:
		if (file_name != "input.css"):
			return send_file("static/"+file_name)
		else:
			return "<h1>Not Found</h1><p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>"
	except:
		return "<h1>Not Found</h1><p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>"

if (__name__ == "__main__"):
	app.run()
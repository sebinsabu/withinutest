from flask import Flaskapp = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

# @app.route('/musicEmotion')
# def musicEmotion():
#     return render_template('musicEmotionView.html')


if __name__ == "__main__":
   app.run(debug=True)
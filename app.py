from flask import Flask, render_template

app = Flask(__name__)

app_name = 'Youtube Transcript to PDF converter'


@app.route('/')
def hello():
  return render_template('home.html', APP_NAME=app_name)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug='True')

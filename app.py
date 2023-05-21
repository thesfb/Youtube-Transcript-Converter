from flask import Flask, render_template, request
import process 

app = Flask(__name__)

app_name = 'Youtube Transcript to PDF converter'


@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    input_text = request.form.get('hero-field')
    output_text = process.get_trans(process.cleaned_link(input_text))
    return render_template('download.html', Out = output_text)

  return render_template('home.html', APP_NAME = app_name)



@app.route('/download')
def download():
  return render_template('download.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug='True')

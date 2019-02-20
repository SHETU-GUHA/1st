from flask import Flask,request,render_template
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index(result=None):
    if request.args.get('mail', None):
        result = process_text(request.args['mail'])
    return render_template('name.html', result=result)

def process_text(text):
    return "Email:" + text
if __name__=='__main__':
    app.run( host='0.0.0.0',debug=True)
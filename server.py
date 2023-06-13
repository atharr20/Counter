from flask import Flask, render_template, request, redirect, session # added request and redirect


app = Flask(__name__)

app.secret_key = 'keep it secret, keep it safe' 
# our index route will handle rendering our form
@app.route('/')
def index():
    if 'counter' in session:
        session['counter']+=1
    else:
        session['counter']=0
    return render_template('index.html')

            
@app.route('/click')
def clicking():
    return redirect('/')

@app.route('/clear')
def reset():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
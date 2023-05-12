from flask import Flask, request, render_template

# app = Flask(__name__, template_folder="jinja_templates")
app = Flask(__name__)

@app.route('/')
def index():
    name, fruit = "Max", "apple"
    x, y = 27, 4 
    template_context = dict(name=name, fruit = fruit, x =x, y= y)
    return render_template('text3.html', **template_context)

@app.route('/html')
def index_html():
    return render_template('text3.html')

if __name__ == "__main__":
    app.run(debug=True)
    


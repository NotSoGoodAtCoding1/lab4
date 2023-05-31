import math
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    title = "Уравнение"
    return render_template('index.html', title=title)


@app.route('/', methods=['post', 'get'])
def form():
    if request.method == 'POST':
        num_1 = int(request.form.get('num_1'))
        num_2 = int(request.form.get('num_2'))
        num_3 = int(request.form.get('num_3'))
        d = (num_2 * num_2) - 4 * num_1 * num_3
        if d == 0:
            ans=-num_2/2*num_1
            return render_template('index.html', out=ans)
        elif d<1:
            return render_template('index.html', out="Дискрименант меньше нуля")
        else:
            ans1 = (-num_2 + math.sqrt(d)) / 2 * num_1
            ans2 = (-num_2 - math.sqrt(d)) / 2 * num_1
        return render_template('index.html', out=ans1, out2=ans2)



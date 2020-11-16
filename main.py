import os
from flask import Flask, render_template, request, redirect
from routes.Web import web

app = Flask(__name__)
app.register_blueprint(web)

todos = [
  {'title': 'Camisetas', 'price': 'R$50,00'},
  {'title': 'Tênis', 'price': 'R$50,00'},
  {'title': 'Calça', 'price': 'R$50,00'},
  {'title': 'Short', 'price': 'R$50,00'}
]

@app.route('/')
def index(): 
    return render_template(
      'index.html', todos=todos
    )

@app.route('/create', methods=['POST'])
def create():
  title = request.form.get('title')
  price = request.form.get('price')
  todos.append({
    'title': title, 'price': price
  })
  return redirect('/')

@app.route('/delete/<int:index>')
def delete(index):
  todos.pop(index)
  return redirect('/')

@app.route('/update/<int:index>', methods=['POST'])
def update(index):
  title = request.form.get('title')
  price = request.form.get('price')
  todos[index]['title'] = title
  todos[index]['price'] = price
  return redirect('/')

if __name__ == '__main__':
  port = int(os.environ.get("PORT", 500))
  app.run(host='0.0.0.0')

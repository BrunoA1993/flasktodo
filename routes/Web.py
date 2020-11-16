from flask import Blueprint
from controllers.web.TodoController import TodoController
web = Blueprint('web', __name__)

@web.route('/')
def index():
  return TodoController.index()

@web.route('/Camisetas', methods=['POST'])
def create():
  return TodoController.create()

@web.route('/Tênis/<int:index>', methods=['POST'])
def update(index):
  return TodoController.update(index)

@web.route('/Calça/<int:index>')
def delete(index):
  return TodoController.delete(index)

@web.route('/Short/<int:index>')
def complete(index):
  return TodoController.complete(index)

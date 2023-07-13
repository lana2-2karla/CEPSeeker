from flask import render_template, request, Blueprint
from .forms import CEPForm
import requests

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/')
def index():
  return render_template('index.html')

@main_blueprint.route('/busca', methods=['GET', 'POST'])
def busca():
  cep_form = CEPForm()

  if cep_form.validate_on_submit():
    cep = cep_form.cep.data
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    if response.status_code == 200:
      data = response.json()
      return render_template('cep_result.html', data=data)

  return render_template('busca.html', cep_form=cep_form)
    
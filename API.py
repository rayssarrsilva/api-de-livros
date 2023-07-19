#1.objetivos, criar um api que disponibiliza consulta, criaçao, ediçao e exclusao de livros.
#2.URL base, localhost.com
#3.endpoints
 #- localhost/livros (GET)
 #- localhost/livros/id (GET com id)
 #- localhost/livros/id (PUT)
 #- localhost/livro/id (DELETE)
#4.quais recursos - Livros

from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id':1,
        'titulo': 'O senhor dos Anéis - A sociedade do anel',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'titulo': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K Howling'
    },
    {
        'id': 3,
        'titulo': 'James clear',
        'Autor': 'Hábitos Atômicos'
    },
]

# consultar (todos)
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)
# consultar (id)
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
# Editar
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
#criar
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)
# Excluir
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)
app.run(port=5000, host='localhost', debug=True)
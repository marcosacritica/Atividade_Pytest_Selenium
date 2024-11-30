import pytest
import requests

# Base URL da API
BASE_URL = "https://www.anapioficeandfire.com/api"

@pytest.mark.parametrize("book_id, expected_name", [
    (1, "A Game of Thrones"),
    (2, "A Clash of Kings"),
    (3, "A Storm of Swords")
])
def test_get_specific_book_parametrized(book_id, expected_name):
    # Testa a recuperação de livros específicos com diferentes IDs
    endpoint = f"/books/{book_id}"
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    assert data["name"] == expected_name, f"Esperado: {expected_name}, Retornado: {data['name']}"
    print(f"Livro retornado ({book_id}): {data['name']}")

def test_get_books():
    # Testa a recuperação da lista de livros
    endpoint = "/books"
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    assert len(data) > 0, "Nenhum livro foi retornado"
    print(f"Livros retornados: {len(data)}")

def test_get_specific_book():
    # Testa a recuperação de um livro específico pelo ID
    book_id = 1  # ID do primeiro livro
    endpoint = f"/books/{book_id}"
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    assert data["name"] == "A Game of Thrones", f"Livro incorreto: {data['name']}"
    print(f"Livro retornado: {data['name']}")

def test_get_characters():
    # Testa a recuperação da lista de personagens
    endpoint = "/characters"
    params = {"page": 1, "pageSize": 10}  # Paginação para limitar a quantidade de dados retornados
    response = requests.get(BASE_URL + endpoint, params=params)
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    assert len(data) > 0, "Nenhum personagem foi retornado"
    print(f"Personagens retornados: {len(data)}")

def test_search_character():
    # Testa a busca de um personagem por nome
    endpoint = "/characters"
    params = {"name": "Jon Snow"}
    response = requests.get(BASE_URL + endpoint, params=params)
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    assert len(data) > 0, "Nenhum personagem encontrado"
    assert data[0]["name"] == "Jon Snow", f"Personagem incorreto: {data[0]['name']}"
    print(f"Personagem encontrado: {data[0]['name']}")

def test_get_houses():
    # Testa a recuperação da lista de casas
    endpoint = "/houses"
    params = {"page": 1, "pageSize": 10}  # Paginação para limitar a quantidade de dados retornados
    response = requests.get(BASE_URL + endpoint, params=params)
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    assert len(data) > 0, "Nenhuma casa foi retornada"
    print(f"Casas retornadas: {len(data)}")

#TESTE DE ERRO

def test_get_invalid_book():
    # Testa a tentativa de recuperar um livro com um ID inválido
    invalid_book_id = 9999  # ID inexistente
    endpoint = f"/books/{invalid_book_id}"
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == 404, "Esperado status 404 para ID inexistente"
    print("Requisição de livro inválido retornou 404 conforme esperado.")

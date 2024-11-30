import pytest
import requests

# Base URL da API
BASE_URL = "https://fakestoreapi.com"

def test_get_all_products():
    # Testa a recuperação de todos os produtos
    endpoint = "/products"
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == 200, "Erro ao acessar API de produtos"
    data = response.json()
    assert len(data) > 0, "Nenhum produto foi retornado"
    print(f"Produtos retornados: {len(data)}")

def test_get_product_by_id():
    # Testa a recuperação de um produto específico pelo ID
    product_id = 1  # ID de exemplo
    endpoint = f"/products/{product_id}"
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == 200, "Erro ao acessar API de produto por ID"
    data = response.json()
    assert data["id"] == product_id, f"Produto incorreto: {data['id']}"
    print(f"Produto retornado: {data['title']}")

def test_get_all_categories():
    # Testa a recuperação de todas as categorias
    endpoint = "/products/categories"
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == 200, "Erro ao acessar API de categorias"
    data = response.json()
    assert len(data) > 0, "Nenhuma categoria foi retornada"
    print(f"Categorias retornadas: {len(data)}")

def test_get_products_by_category():
    # Testa a recuperação de produtos de uma categoria específica
    category = "electronics"  # Exemplo de categoria
    endpoint = f"/products/category/{category}"
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == 200, f"Erro ao acessar produtos da categoria {category}"
    data = response.json()
    assert len(data) > 0, f"Nenhum produto encontrado na categoria {category}"
    print(f"Produtos retornados da categoria '{category}': {len(data)}")

def test_get_cart_by_id():
    # Testa a recuperação de um carrinho específico pelo ID
    cart_id = 1  # ID de exemplo
    endpoint = f"/carts/{cart_id}"
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == 200, "Erro ao acessar API de carrinhos"
    data = response.json()
    assert data["id"] == cart_id, f"Carrinho incorreto: {data['id']}"
    print(f"Carrinho retornado: {data}")

def test_get_invalid_product():
    # Testa um produto inexistente pelo ID
    invalid_product_id = 9999  # ID que não existe
    endpoint = f"/products/{invalid_product_id}"
    response = requests.get(BASE_URL + endpoint)
    
    # Valida que a API está retornando status 200 (comportamento da API)
    assert response.status_code == 200, "Esperado status 200 para produto inexistente (comportamento da API)"
    
    # Trata o caso de corpo vazio
    try:
        data = response.json()  # Tenta decodificar a resposta
        assert "id" not in data or data.get("id") != invalid_product_id, f"Produto inesperadamente encontrado: {data}"
    except requests.exceptions.JSONDecodeError:
        # Caso o corpo seja vazio, este é um comportamento válido para um recurso inexistente na Fake Store API
        print(f"Produto com ID {invalid_product_id} não encontrado (resposta vazia).")


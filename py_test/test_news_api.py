import pytest
import requests

# BASE URL da News API e chave da API
BASE_URL = "https://newsapi.org/v2"
API_KEY = "a926393c4f194932957a7f0a7d484ec4"  # Chave Validada da Api

def test_top_headlines():
    # Testar a busca de manchetes principais
    endpoint = "/top-headlines"
    params = {"apiKey": API_KEY, "country": "us"}
    response = requests.get(BASE_URL + endpoint, params=params)
    assert response.status_code == 200, "Erro ao acessar API de manchetes principais"
    data = response.json()
    assert "articles" in data, "Campo 'articles' não encontrado na resposta"
    assert len(data["articles"]) > 0, "Nenhuma manchete encontrada"
    print(f"Número de manchetes: {len(data['articles'])}")

def test_everything_search():
    # Testar a busca de artigos com um termo específico
    endpoint = "/everything"
    params = {"apiKey": API_KEY, "q": "technology"}
    response = requests.get(BASE_URL + endpoint, params=params)
    assert response.status_code == 200, "Erro ao acessar API de busca de artigos"
    data = response.json()
    assert "articles" in data, "Campo 'articles' não encontrado na resposta"
    assert len(data["articles"]) > 0, "Nenhum artigo encontrado para a busca"
    print(f"Artigos encontrados para 'technology': {len(data['articles'])}")

def test_sources():
    # Testar a listagem de fontes de notícias
    endpoint = "/sources"
    params = {"apiKey": API_KEY}
    response = requests.get(BASE_URL + endpoint, params=params)
    assert response.status_code == 200, "Erro ao acessar API de fontes de notícias"
    data = response.json()
    assert "sources" in data, "Campo 'sources' não encontrado na resposta"
    assert len(data["sources"]) > 0, "Nenhuma fonte de notícia encontrada"
    print(f"Número de fontes disponíveis: {len(data['sources'])}")

def test_top_headlines_category():
    # Testar a busca de manchetes principais de uma categoria específica
    endpoint = "/top-headlines"
    params = {"apiKey": API_KEY, "country": "us", "category": "business"}
    response = requests.get(BASE_URL + endpoint, params=params)
    assert response.status_code == 200, "Erro ao acessar API de manchetes por categoria"
    data = response.json()
    assert "articles" in data, "Campo 'articles' não encontrado na resposta"
    assert len(data["articles"]) > 0, "Nenhuma manchete encontrada para a categoria 'business'"
    print(f"Número de manchetes em 'business': {len(data['articles'])}")

def test_everything_date_range():
    # Testar a busca de artigos em um intervalo de datas
    endpoint = "/everything"
    params = {
        "apiKey": API_KEY,
        "q": "space",
        "from": "2024-11-01",
        "to": "2024-11-25"
    }
    response = requests.get(BASE_URL + endpoint, params=params)
    assert response.status_code == 200, "Erro ao acessar API de artigos por data"
    data = response.json()
    assert "articles" in data, "Campo 'articles' não encontrado na resposta"
    assert len(data["articles"]) > 0, "Nenhum artigo encontrado para o intervalo de datas"
    print(f"Artigos encontrados sobre 'space' entre 01/11/2024 e 25/11/2024: {len(data['articles'])}")

import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.mark.parametrize("endpoint", [
    f"{BASE_URL}/posts",        # Todos os posts
    f"{BASE_URL}/users",        # Todos os usuários
    f"{BASE_URL}/comments",     # Todos os comentários
    f"{BASE_URL}/posts/1",      # Post específico (ID 1)
    f"{BASE_URL}/users/1",      # Usuário específico (ID 1)
])
def test_api_endpoints(endpoint):
    response = requests.get(endpoint)
    
    # Verificar o status da rota
    assert response.status_code == 200, f"Falha ao acessar a rota: {endpoint} (Status: {response.status_code})"
    print(f"Teste bem-sucedido para a rota: {endpoint}")
    print(f"Status da rota: {response.status_code}\n")

@pytest.mark.parametrize("post_id, expected_title", [
    (1, "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"),  # Título do post com ID 1
    (2, "qui est esse"),  # Título do post com ID 2
    (3, "ea molestias quasi exercitationem repellat qui ipsa sit aut"),  # Título do post com ID 3
])
def test_post_by_id(post_id, expected_title):
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200, f"Falha ao acessar post com ID {post_id}"
    data = response.json()
    assert data["title"] == expected_title, f"Esperado: {expected_title}, Recebido: {data['title']}"
    print(f"Post com ID {post_id}: {data['title']} (Status: {response.status_code})\n")



# Teste para verificar quando um usuário não existe

def test_filter_users_by_name():
    # Teste para buscar usuários com o nome "Leanne Graham"
    response = requests.get(f"{BASE_URL}/users?name=Leanne Graham")
    assert response.status_code == 200, f"Erro ao buscar usuário Leanne Graham: {response.status_code}"
    
    data = response.json()
    print(f"Resposta da API: {data}")  # Mostra o conteúdo retornado pela API
    
    assert len(data) > 0, "Nenhum usuário encontrado com o nome Leanne Graham"
    print(f"Usuários encontrados com o nome Leanne Graham: {len(data)} (Status: {response.status_code})\n")



def test_filter_comments_by_post_id():
    # Teste para buscar comentários do post com ID 1
    response = requests.get(f"{BASE_URL}/comments?postId=1")
    assert response.status_code == 200, "Erro ao buscar comentários do post com ID 1"
    data = response.json()
    assert len(data) > 0, "Nenhum comentário encontrado para o post com ID 1"
    print(f"Comentários encontrados para o post com ID 1: {len(data)} (Status: {response.status_code})\n")

def test_user_details_by_id():
    # Teste para verificar os detalhes do usuário com ID 1
    user_id = 1
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 200, f"Erro ao buscar usuário com ID {user_id}"
    data = response.json()
    assert data["id"] == user_id, f"Esperado ID {user_id}, Recebido {data['id']}"
    print(f"Usuário com ID {user_id}: {data['name']} (Status: {response.status_code})\n")

def test_invalid_post_id():
    # Teste para um post inexistente
    invalid_id = 9999
    response = requests.get(f"{BASE_URL}/posts/{invalid_id}")
    assert response.status_code == 404, "Esperado status 404 para ID inexistente"
    print(f"Teste de ID inválido bem-sucedido (Status: {response.status_code})\n")

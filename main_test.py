import pytest
from main import app


@pytest.fixture
def client():
    """Cria um cliente de teste Flask"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_handler(client):
    """Testa se o endpoint retorna a mensagem esperada"""
    # Faz uma requisição GET para /
    response = client.get('/')
    
    # Verifica o resultado
    expected = "Hello World! I'm PYTHON app-b!"
    
    assert response.status_code == 200
    assert expected in response.get_data(as_text=True)

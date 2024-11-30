Pytest e Selenium: Testes Automatizados
Este repositório contém uma atividade desenvolvida como parte da disciplina Testes de Software, orientada pelo professor Érico Borgonove, para avaliação parcial do curso.

Descrição
O projeto explora a integração do framework Pytest com a biblioteca de automação de testes Selenium, abordando práticas de teste de interface de usuário em aplicações web. Ele demonstra como automatizar interações com navegadores, validar funcionalidades e criar fluxos de teste robustos.

🚀 Primeiros Passos
As instruções a seguir ajudarão você a obter uma cópia funcional deste projeto em sua máquina para fins de desenvolvimento ou aprendizado.

📋 Pré-requisitos
Antes de começar, certifique-se de que as seguintes ferramentas estejam instaladas:

Python 3.x: Linguagem utilizada no desenvolvimento dos testes.
pip: Gerenciador de pacotes do Python.
Selenium: Biblioteca para automação de navegadores.
Pytest: Framework para criação e execução de testes.
Requests: Requests é uma biblioteca Python para requisições HTTP simples e eficientes.
Driver do Navegador: O driver apropriado para o navegador usado (ex.: ChromeDriver para Google Chrome).

🔧 Instalação
Clone este repositório para o seu ambiente local:


git clone https://github.com/marcosacritica/Atividade_Pytest_Selenium.git
Navegue até o diretório do projeto:


cd Atividade_Pytest_Selenium
Instale as dependências listadas no arquivo requirements.txt:


pip install -r requirements.txt
⚙️ Executando os Testes
Para executar os testes automatizados, utilize o comando:


pytest
Este comando executará todos os testes criados no projeto e exibirá os resultados diretamente no terminal.

📂 Estrutura do Repositório

TESTE2/
├── py-selenium/
├── py_test
├── requirements.txt
└── README.md

py-selenium/: Contém os testes automatizados utilizando Pytest.
py_test/: Scripts para a abstração de páginas e componentes da aplicação.

requirements.txt: Arquivo contendo a lista de dependências necessárias.

🔍 Testes Realizados
Os testes cobrem os seguintes aspectos:

Testes de Navegação: Verificam se é possível acessar diferentes páginas do sistema.
Interação com Formulários: Testes para validar inputs, botões e submissões.
Validação de Mensagens: Garante que os resultados exibidos na interface estão de acordo com o esperado.

📏 Boas Práticas
O código segue as diretrizes de qualidade do Python, como o padrão PEP 8, para garantir clareza e legibilidade.

✒️ Autor
Marcos Almeida - Desenvolvimento do Projeto - GitHub
Érico Borgonove - Orientação Acadêmica

🎁 Agradecimentos
Ao professor Érico Borgonove, por sua orientação e suporte.
Aos colegas de curso, pelo incentivo e colaboração.

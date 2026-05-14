# 📇 Django Contact Manager - Sistema de Agenda de Contatos

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Django](https://img.shields.io/badge/Django-5.0-green.svg)](https://djangoproject.com)
[![SQLite](https://img.shields.io/badge/SQLite-3-blue.svg)](https://sqlite.org)
[![License](https://img.shields.io/badge/License-MIT-red.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-production--ready-brightgreen.svg)]()

## 📋 Sobre o Projeto

**Sistema completo de gerenciamento de contatos** desenvolvido com Django 5.0, ideal para:

- ✅ Agendas pessoais com múltiplos usuários
- ✅ Catálogo de clientes para pequenas empresas
- ✅ CRM básico para negócios
- ✅ Sistema de leads e acompanhamento

### 🎯 Diferenciais

- 🔐 **Autenticação completa** (registro, login, logout)
- 👤 **Controle por usuário** (cada usuário vê apenas seus contatos)
- 📸 **Upload de fotos** por contato
- 🏷️ **Categorização dinâmica** de contatos
- 🔍 **Busca integrada** por nome, telefone ou email
- 👁️ **Controle de visibilidade** (mostrar/esconder contatos)

## 🛠 Tecnologias Utilizadas

| Tecnologia | Versão | Finalidade |
|------------|--------|-------------|
| **Python** | 3.8+ | Linguagem principal |
| **Django** | 5.0 | Framework web |
| **SQLite3** | 3.x | Banco de dados (desenvolvimento) |
| **Pillow** | 10.0+ | Manipulação de imagens/uploads |
| **HTML5/CSS3** | - | Front-end |

## 🚀 Como Executar o Projeto

### Pré-requisitos

- Python 3.8 ou superior
- Git
- Pip (gerenciador de pacotes)

### Passo a Passo

1. Clone o repositorio:

`git clone https://github.com/JeffersonEstevo/PROJETO-AGENDA-DJANGO.git`    
`cd SEU_REPOSITORIO`

2. Crie um ambiente virtual:

Windows:  
`python -m venv venv`  
`venv\Scripts\activate`

Linux/Mac:  
`python3 -m venv venv`  
`source venv/bin/activate`  

3. Crie o arquivo requirements.txt com o conteudo:  
```
Django>=5.0,<5.1
Pillow>=10.0.0
python-dotenv>=1.0.0
```

4. Instale as dependencias:

`pip install -r requirements.txt`

5. Configure a SECRET_KEY:

Crie um arquivo .env com:   
```SECRET_KEY=sua-chave-secreta-aqui
DEBUG=True
```  

OU edite o arquivo sec.py:  
```var = "sua-chave-secreta-aqui"```

6. Execute as migracoes:

```python manage.py migrate```  v

7. Crie um superusuario:

```python manage.py createsuperuser```  

8. Inicie o servidor:

```python manage.py runserver```  

9. Acesse:
```
Site principal: http://127.0.0.1:8000
Admin: http://127.0.0.1:8000/admin
Registro: http://127.0.0.1:8000/user/create/
```  

## Estrutura do Projeto
```
contact-manager/
|-- manage.py
|-- requirements.txt
|-- .env
|-- project/
|   |-- settings.py
|   |-- urls.py
|   -- wsgi.py
|-- contact/
|   |-- models.py
|   |-- views.py
|   |-- urls.py
|   -- admin.py
|-- base_templates/
|-- base_static/
-- media/
```

## Rotas da Aplicacao

```
/ -> Pagina inicial
/search/ -> Busca
/contact/<id>/detail/ -> Detalhe do contato
/contact/create/ -> Criar contato
/contact/<id>/update/ -> Editar contato
/contact/<id>/delete/ -> Deletar contato
/user/create/ -> Registrar usuario
/user/login/ -> Login
/user/logout/ -> Logout
/user/update/ -> Atualizar perfil
/admin/ -> Painel administrativo
```

## Comandos Uteis

```
python manage.py runserver -> Inicia o servidor
python manage.py makemigrations -> Cria migracoes
python manage.py migrate -> Aplica migracoes
python manage.py createsuperuser -> Cria admin
python manage.py collectstatic -> Coleta arquivos estaticos
```

## Possiveis Problemas e Solucoes

```
Erro: No module named 'PIL'
Solucao: pip install Pillow

Erro: ImproperlyConfigured (SECRET_KEY)
Solucao: Configure o arquivo .env ou sec.py

Erro ao fazer upload de imagens
Solucao: chmod 755 media/ (Linux/Mac)

Erro: CSRF token missing
Solucao: Limpe os cookies do navegador
```

## Licenca

MIT License

## Autor

Jefferson Estevo

GitHub: [JeffersonEstevo](https://github.com/JeffersonEstevo)  
LinkedIn: [Jefferson Estevo](https://br.linkedin.com/in/jefferson-estevo-908a67237)  
Upwork: [Meu perfil no Upwork](https://www.upwork.com/freelancers/~01e2d7c7088c47c20e)  

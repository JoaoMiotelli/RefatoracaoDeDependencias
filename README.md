# RefatoracaoDeDependencias

> Exercício da disciplina de Clean Code referente à refatoração de um código para reduzir dependências e melhorar sua organização.

**Autor:** João Victor Miotelli Vitali  
**Curso:** Engenharia de Software – SATC  
**Disciplina:** Clean Code  
**Tema:** Refatoração de Dependências  
**Data:** Outubro de 2025  

---

## Objetivo

O projeto tem como finalidade refatorar um código de gerenciamento de usuários, com foco em:

- Reduzir dependências externas  
- Melhorar a organização e clareza  
- Separar responsabilidades em camadas distintas  
- Aumentar a testabilidade e manutenibilidade  
- Utilizar **apenas bibliotecas nativas do Python**

---

## Estrutura do Projeto

```
usuarios_refatorado/
├─ src/
│  └─ app/
│     ├─ __init__.py
│     ├─ domain.py
│     ├─ ports.py
│     ├─ repository.py
│     ├─ email.py
│     ├─ api.py
│     ├─ usecases.py
│     └─ cli.py
├─ main.py
└─ README.md
```

---

## ⚙️ Arquitetura e Organização

O código foi estruturado segundo os princípios de **Clean Architecture**, dividindo o sistema em **camadas independentes**:

| Camada | Arquivo | Descrição |
|--------|----------|------------|
| **Domínio** | `domain.py` | Contém o modelo `User` e funções puras do domínio. |
| **Portas (Interfaces)** | `ports.py` | Define contratos para repositórios, APIs e envio de e-mails. |
| **Repositório** | `repository.py` | Gerencia o armazenamento dos usuários em memória. |
| **Serviço de E-mail** | `email.py` | Registra mensagens de boas-vindas em um arquivo de log. |
| **Cliente de API** | `api.py` | Faz requisições a uma API pública usando apenas `urllib`. |
| **Casos de Uso** | `usecases.py` | Implementa as regras de negócio puras, sem efeitos colaterais. |
| **Interface CLI** | `cli.py` | Fornece o menu de interação com o usuário via terminal. |

---

## Funcionalidades

1. **Adicionar usuário** – Cria um novo usuário e registra um “e-mail” de boas-vindas.  
2. **Listar usuários** – Exibe todos os usuários e seus status (ativo/inativo).  
3. **Desativar usuário** – Desativa o usuário pelo ID informado.  
4. **Buscar usuário na API** – Consulta informações na API pública  
   [`https://jsonplaceholder.typicode.com/users/{id}`](https://jsonplaceholder.typicode.com/users/1).

---

## Tecnologias Utilizadas

**Python 3.10+**  
**Biblioteca padrão apenas:**
- `dataclasses`
- `json`
- `datetime`
- `pathlib`
- `urllib.request`
- `typing`

---

## Como Executar o Projeto

### 1️⃣ Criar e ativar um ambiente virtual (opcional)
```bash
python -m venv .venv
.venv\Scripts\activate    # Windows
source .venv/bin/activate # Linux / macOS
```

### 2️⃣ Executar o programa
```bash
python main.py
```

### 3️⃣ Navegar pelo menu interativo
```
=== Sistema de Usuários ===
1 - Adicionar usuário
2 - Listar usuários
3 - Desativar usuário
4 - Buscar usuário na API
0 - Sair
```

---

## Log de E-mails

Os “e-mails” enviados são registrados automaticamente no arquivo `log_email.txt`, localizado no diretório raiz do projeto.

Exemplo de saída:
```
2025-10-06 22:45:13 - usuario@email.com - Olá João, bem-vindo ao sistema!
```

---

## Melhorias Implementadas

- Separação clara de responsabilidades  
- Código modular e reutilizável  
- Funções puras e testáveis  
- Remoção de dependências externas (`httpx`, `rich`)  
- Organização em camadas independentes  
- Simplicidade e clareza de execução  

---

## Conclusão

Este projeto exemplifica a aplicação prática dos princípios de **Clean Code** e **Clean Architecture**, mostrando como uma refatoração adequada:

- Torna o sistema **mais compreensível e flexível**  
- Reduz o acoplamento entre componentes  
- Facilita testes e futuras expansões  
- Mantém o código **simples, limpo e sustentável**

---

### Desenvolvido por
**João Victor Miotelli Vitali**  
Engenharia de Software – SATC  
Disciplina: Clean Code  
Outubro de 2025

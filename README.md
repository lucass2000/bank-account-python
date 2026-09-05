# Bank Account Testing with Python

Projeto acadêmico desenvolvido durante o curso de Ciência da Computação com foco em **Engenharia de Software, testes automatizados, verificação e validação de software**.

O projeto simula operações bancárias simples e demonstra, de forma prática, como testes automatizados podem identificar falhas de lógica e validar uma implementação corrigida.

## Objetivos

- aplicar conceitos de Programação Orientada a Objetos;
- implementar regras de negócio para contas bancárias;
- criar testes automatizados com `unittest`;
- identificar bugs em uma versão propositalmente incorreta;
- corrigir as falhas encontradas;
- comparar o comportamento antes e depois das correções.

## Funcionalidades

A classe `Account` permite:

- criar uma conta com titular e saldo inicial;
- realizar depósitos;
- realizar saques;
- transferir valores entre contas;
- consultar o saldo;
- validar operações inválidas por meio de exceções.

## Estrutura do projeto

```text
bank-account-testing-python/
├── src/
│   ├── __init__.py
│   ├── account.py
│   └── account_buggy.py
├── tests/
│   ├── __init__.py
│   └── test_account.py
├── bug_demo/
│   └── buggy_tests.py
├── app.py
├── README.md
└── .gitignore
```

## Tecnologias

- Python 3
- `unittest`
- Programação Orientada a Objetos
- Tratamento de exceções
- Testes de software

## Como executar

Clone o repositório e entre na pasta do projeto.

### Executar os testes da versão corrigida

```bash
python -m unittest discover -s tests -v
```

Todos os testes devem ser aprovados.

### Executar a aplicação de demonstração

```bash
python app.py
```

## Demonstração dos bugs

O arquivo `src/account_buggy.py` mantém dois erros propositalmente, usados no projeto acadêmico para demonstrar o papel dos testes:

1. o método de saque não rejeita valores negativos;
2. o método de transferência debita a conta de origem, mas não credita a conta de destino.

Para executar apenas os testes que demonstram essas falhas:

```bash
python bug_demo/buggy_tests.py
```

Esses testes **devem falhar**, pois o objetivo é evidenciar os defeitos da implementação incorreta.

## Casos de teste

A versão principal cobre:

- depósito e saque válidos;
- saque acima do saldo disponível;
- saque com valor negativo;
- transferência entre contas;
- sequência de operações;
- saldo inicial inválido;
- titular vazio;
- tentativa de transferência para a própria conta.

## Principais aprendizados

- criação e execução de testes automatizados;
- identificação de erros lógicos;
- uso de exceções para validação de regras de negócio;
- organização de código em módulos;
- comparação entre implementação defeituosa e corrigida;
- importância de testes no ciclo de desenvolvimento de software.

## Contexto acadêmico

Este repositório organiza uma versão revisada de um **projeto acadêmico em grupo** desenvolvido na disciplina de Engenharia de Software.

Antes de publicar materiais produzidos pelo grupo (como relatório completo, documentos da faculdade ou código criado por outros integrantes), certifique-se de ter autorização dos demais participantes e remova dados pessoais como matrículas, e-mails e assinaturas.

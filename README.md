# Calculadora
![Python](https://img.shields.io/badge/Python-3.x-blue.svg) 
![Status](https://img.shields.io/badge/Status-Ativo-success)

Uma calculadora simples em **Python** que realiza as quatro operações básicas da matemática e que também possui um histórico com os cálculos efetuados.

---

## Pré-requisitos

Antes de executar, certifique-se de ter instalado:

- Python 3

- Git (para clonar o repositório)

---

## Funcionalidades

- **Cálculos matemáticos com as quatro operações básicas** (soma, subtração, multiplicação, divisão)
- **Menu interativo com 7 (sete) opções para a escolha do usuário**
- **Histórico com todos os cálculos efetuados pelo o usuário**
- **Opção de limpar todo o histórico de operações**
- **Persistência do histórico em arquivo `.json`**
- **Tratamento de erros e validações**

---

## Tecnologias utilizadas

- **Python 3**
- **JSON** para armazenamento
- **Bibliotecas nativas do python:**
  - `os`
  - `sys`
  - `json`

---

## Estrutura do projeto

```bash
projeto-calculadora/
|—— calculadora.py     # Código principal
|—— historico.json     # Arquivo do histórico (gerado automaticamente)
|—— README.md          # Documentação do projeto
|—— LICENSE            # Licença MIT
```

---

## Como executar

**1. Clone o repositório**
```bash
git clone https://github.com/kauasantos-dev/projeto-calculadora.git
cd projeto-calculadora
```

**2. Execute o programa**

```bash
python calculadora.py
```

**3. Use o menu interativo**

```bash
===== MENU DE OPÇÕES =====

Selecione uma opção abaixo (digite o número da opção):

[1]- Soma
[2]- Subtração
[3]- Divisão
[4]- Multiplicação
[5]- Histórico de operações
[6]- Limpar histórico
[7]- Sair
```

---

## Exemplo de uso

**1. Soma:**

```bash
Informe dois números ou mais (digite 'sair' para finalizar): 10
Informe dois números ou mais (digite 'sair' para finalizar): 20
Informe dois números ou mais (digite 'sair' para finalizar): sair

10 + 20 = 30
```

**2. Divisão:**

```bash
Informe o primeiro número: 10
Informe o segundo número: 2

10 / 2 = 5.0
```

**3. Histórico de operações**

```bash
Seu histórico de operações:

10 + 20 = 30

10 / 2 = 5.0
```

**4. Apagar histórico**

```bash
Histórico apagado com sucesso!
```

---

## Tratamento de erros e validações

- Números não podem conter letras, espaços ou caracteres especiais.

- Verificar se o usuário informou menos de dois números para efetuar a operação.

- Mensagens de erro caso o usuário realize alguma ação inválida.

---

## Contribuição

Contribuições são bem-vindas! 
Sinta-se à vontade para abrir uma issue ou enviar um pull request para melhorar o projeto.

---

## Licença

Este programa está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

---

## Autor

**Kavilly Kauã**

Estudante de **Análise e Desenvolvimento de Sistemas (ADS) - IFRN**

**Contato:**

- GitHub: [kauasantos-dev](https://github.com/kauasantos-dev)
- E-mail: [kavillykaua@gmail.com](kavillykaua@gmail.com)
# Validador de Boleto - Grupo Heineken

Um validador de boleto bancário desenvolvido com Flask e Python, baseado no design original do Grupo Heineken.

## 🚀 Funcionalidades

- ✅ Validação de código de barras de boleto (47 dígitos)
- ✅ Formatação automática do código durante a digitação
- ✅ Contador de números digitados em tempo real
- ✅ Interface responsiva e moderna
- ✅ Página de sucesso com estatísticas detalhadas
- ✅ Validação tanto no frontend quanto no backend

## 🛠️ Tecnologias

- **Backend**: Python 3.12+ com Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Gerenciamento de Pacotes**: uv (Python package manager)
- **Estilo**: Design responsivo baseado no Grupo Heineken

## 📋 Pré-requisitos

- Python 3.12 ou superior
- uv (Python package manager)

## 🔧 Instalação

1. Clone o repositório:

```bash
git clone <url-do-repositorio>
cd boleto_validador
```

2. Instale as dependências com uv:

```bash
uv sync
```

## 🚀 Como Executar

### Usando uv (Recomendado)

```bash
uv run python app.py
```

### Usando Python diretamente

```bash
python app.py
```

O servidor estará disponível em: `http://localhost:5000`

## 🧪 Como Testar

### Teste Manual

1. Acesse `http://localhost:5000`
2. Digite um código de boleto de 47 dígitos
3. Clique em "Validar dados"
4. Verifique a página de sucesso

### Teste com curl

```bash
# Teste da página principal
curl http://localhost:5000

# Teste de validação (substitua pelos seus 47 dígitos)
curl -X POST http://localhost:5000/validate \
  -d "codigo=12345678901234567890123456789012345678901234567"
```

## 📁 Estrutura do Projeto

```
boleto_validador/
├── app.py                 # Aplicação Flask principal
├── pyproject.toml         # Configuração do projeto (uv)
├── templates/
│   ├── index.html         # Página principal do validador
│   └── success.html       # Página de sucesso
├── static/               # Arquivos estáticos (CSS, JS, imagens)
└── README.md             # Este arquivo
```

## 🔄 Fluxo da Aplicação

1. **Página Principal** (`/`): Formulário de validação
2. **Validação** (`/validate`): Processa o código de barras
3. **Sucesso** (`/success`): Exibe resultado da validação

## ✨ Funcionalidades Detalhadas

### Validação de Código de Barras

- Verifica se o código possui exatamente 47 dígitos
- Remove caracteres não numéricos automaticamente
- Mantém a formatação original para exibição

### Interface do Usuário

- Formatação automática durante a digitação
- Contador visual de números digitados (X/47)
- Mensagens de erro claras e informativas
- Design responsivo para dispositivos móveis

### Página de Sucesso

- Exibe o código de barras formatado
- Mostra estatísticas (números digitados vs esperados)
- Botão para validar outro boleto
- Design consistente com a identidade visual

## 🎨 Design

O projeto mantém a identidade visual do Grupo Heineken, incluindo:

- Cores corporativas
- Tipografia consistente
- Layout responsivo
- Animações e transições suaves

## 🔧 Desenvolvimento

### Adicionando Dependências

```bash
uv add nome-do-pacote
```

### Executando em Modo Debug

```bash
uv run python app.py
```

(O modo debug já está ativado por padrão)

### Logs

Os logs da aplicação são exibidos no terminal durante a execução.

## 📝 Notas

- A aplicação valida apenas o formato (47 dígitos), não a autenticidade real do boleto
- O código está otimizado para performance e usabilidade
- Compatível com todos os navegadores modernos

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

Desenvolvido com ❤️ para o Grupo Heineken

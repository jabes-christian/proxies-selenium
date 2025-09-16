# Proxy Selenium

Este projeto foi desenvolvido para **coletar proxies públicos**, testar quais estão ativos e utilizá-los em **navegadores Selenium**, permitindo simular acessos via proxy.

---

## 🚀 Funcionalidades

- Busca proxies em sites públicos (ex: *free-proxy-list*, *sslproxies*).  
- Faz parsing da lista de proxies e salva em `proxies.txt`.  
- Testa cada proxy com `requests` e grava os válidos em `validado_proxies.txt`.  
- Utiliza o primeiro proxy válido para abrir o Chrome via Selenium.  .  

---

## 📂 Estrutura do Projeto

```
proxy_selenium/
│
├── pegar_proxy.py       # Classe BuscarProxy — busca, filtra e testa proxies
├── proxy.py             # Classe ExceutarProxy — roda Selenium com proxy
├── main.py              # Orquestrador: busca proxies e roda Selenium
├── requirements.txt     # Dependências do projeto
├── .gitignore           # Arquivos/pastas ignorados no Git
└── README.md            # Este documento
```

---

## 🔧 Requisitos

- Python **3.8+**
- Google Chrome instalado
- [ChromeDriver](https://chromedriver.chromium.org/) (instalado automaticamente via `webdriver-manager`)

---

## 📦 Instalação

1. Clone este repositório:

```bash
git clone https://github.com/SEU_USUARIO/NOME_REPO.git
cd NOME_REPO
```

2. Crie e ative um ambiente virtual (Windows PowerShell):

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

Se não tiver o `requirements.txt` ainda, gere com:

```bash
pip install requests beautifulsoup4 lxml selenium webdriver-manager
pip freeze > requirements.txt
```

---

## ▶️ Como usar

### Rodar com Selenium usando um proxy válido:
```bash
python main.py
```

O script:
- Busca proxies
- Testa a conectividade
- Seleciona o primeiro válido
- Abre o navegador Chrome configurado com esse proxy

---

## 🛡️ Observações de Segurança

⚠️ **Atenção:**  
- Proxies gratuitos são **instáveis** e podem cair a qualquer momento.  
- Não utilize este projeto em produção sem um **provedor de proxies confiável**.  
- **Não compartilhe** proxies com credenciais (`user:pass@host:port`) em repositórios públicos.  
- Use variáveis de ambiente em `.env` (que já está no `.gitignore`) para dados sensíveis.  
- O argumento `--ignore-certificate-errors` é usado apenas para contornar certificados inválidos — não é recomendável em sistemas críticos.

---

## 📖 Exemplos de uso

- Testar proxies antes de usar em um bot Selenium.  
- Coletar proxies para scraping leve (não recomendado para produção).  
- Entender como configurar **Selenium com proxies dinâmicos**.  

---

## 📌 Roadmap (possíveis melhorias)

- [ ] Suporte a proxies autenticados (usuário/senha).  
- [ ] Seleção aleatória de proxies válidos.  
- [ ] Re-testes periódicos para remover proxies inativos.  
- [ ] Dashboard simples para visualizar status dos proxies.  

---

## 👨‍💻 Autor

Desenvolvido por **Jabes Christian** 🚀  
Se quiser trocar uma ideia ou sugerir melhorias, só abrir uma **Issue** ou **Pull Request** aqui no GitHub.  

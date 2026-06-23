# Instalação e Execução do Projeto

## Requisitos

Antes de executar o projeto, certifique-se de possuir os seguintes softwares instalados:

### Python

Versão recomendada:

* Python 3.11 ou superior

# Criando Ambiente Virtual Python

Criar ambiente virtual:

Windows:

```bash
python -m venv .venv
```

Linux/Mac:

```bash
python3 -m venv .venv
```

---

# Ativando Ambiente Virtual

Windows (PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

Windows (CMD):

```cmd
.venv\Scripts\activate.bat
```

Linux/Mac:

```bash
source .venv/bin/activate
```

# Instalando Dependências

Instalar todas as dependências do projeto:

```bash
pip install -r requirements.txt
```

# Executando o Projeto

Iniciar aplicação:

```bash
fastapi dev
```

# Testando Localmente

Abrir navegador:

```text
http://localhost:8000
```

# Atualizando Dependências

Caso novas bibliotecas sejam instaladas:

```bash
pip freeze > requirements.txt
```

# Encerrando Ambiente Virtual

Quando terminar o uso:

```bash
deactivate
```

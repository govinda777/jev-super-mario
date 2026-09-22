# jev-super-mario

[![Assista à demonstração no YouTube](https://img.youtube.com/vi/YZVEo5IZlvk/maxresdefault.jpg)](https://youtu.be/YZVEo5IZlvk?si=Ul4-WN8fA4fHImrK)

> 📺 **Demonstração:** [Clique aqui para assistir ao Jev AI jogando no YouTube](https://youtu.be/YZVEo5IZlvk?si=Ul4-WN8fA4fHImrK)

Este é um projeto conceitual demonstrando como integrar o **Jev AI** (via SDK da TypeSafe) para jogar *Super Mario Bros.*. Ao invés de processar imagens, a arquitetura extrai o estado diretamente da memória (RAM) do emulador e toma decisões estruturadas em milissegundos.

O script `main.py` contém uma simulação de como enviar o estado do Mario (posição, inimigos próximos, buracos) e requisitar uma escolha de ação (`Choice`) e avaliação de perigo (`Score`) simultaneamente à API do Jev.

---

## Pré-requisitos Necessários

Para rodar este projeto, você precisa de:
1. **Git** (para clonar o repositório)
2. **Python 3.10 ou superior** e **pip**
3. **Chave de API TypeSafe (`TYPESAFE_API_KEY`)**

---

## Como Instalar os Pré-requisitos

Se você ainda não possui as ferramentas acima instaladas na sua máquina, siga as instruções para o seu sistema operacional:

### 1. No macOS

#### Opção A: Usando o Homebrew (Recomendado)
Se você tem o [Homebrew](https://brew.sh) instalado, abra o terminal e execute:
```bash
# Atualizar repositórios do Homebrew
brew update

# Instalar Python 3 e Git
brew install python git
```

#### Opção B: Instaladores Manuais
- **Git:** Abra o terminal e execute `xcode-select --install` para instalar as ferramentas de desenvolvedor da Apple (que já incluem o Git).
- **Python:** Baixe o instalador oficial `.pkg` em [python.org/downloads/macos](https://www.python.org/downloads/macos/) e execute a instalação.

---

### 2. No Linux (Ubuntu / Debian / Mint)

Abra o terminal e instale o Python, o gerenciador de pacotes pip, o módulo de ambientes virtuais (`venv`) e o Git:
```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv git
```

*(Em distribuições baseadas em Fedora/RedHat: `sudo dnf install -y python3 python3-pip git`)*

---

### 3. No Windows

#### Opção A: Usando o Winget (Terminal / PowerShell)
Abra o PowerShell como Administrador e execute:
```powershell
# Instalar o Python 3.11 (ou 3.12)
winget install Python.Python.3.11

# Instalar o Git
winget install Git.Git
```
Após a instalação, feche e reabra o terminal.

#### Opção B: Pelos Instaladores Oficiais (.exe)
1. **Python:**
   - Acesse [python.org/downloads/windows](https://www.python.org/downloads/windows/) e baixe o instalador da versão mais recente (3.10 ou superior).
   - **⚠️ IMPORTANTE:** Na primeira tela do instalador, marque a caixa **"Add python.exe to PATH"** antes de clicar em "Install Now".
2. **Git:**
   - Baixe e instale o Git pelo site oficial: [git-scm.com/download/win](https://git-scm.com/download/win).

---

### 4. Como Obter a Chave de API da TypeSafe

1. Acesse o site oficial da plataforma: [typesafe.ai](https://typesafe.ai).
2. Crie uma conta ou faça login com suas credenciais.
3. No painel de controle (Dashboard), acesse a seção de **API Keys**.
4. Clique em **Create API Key** (ou Gerar Chave), dê um nome e copie o valor da chave (ela será usada na variável `TYPESAFE_API_KEY`).

---

### Verificando as Instalações

Para confirmar que tudo está instalado corretamente, execute no terminal:

```bash
# Verificar a versão do Python (deve ser 3.10 ou superior)
python3 --version   # (No Windows pode ser apenas: python --version)

# Verificar o pip
python3 -m pip --version

# Verificar o Git
git --version
```

---

## Como Instalar as Dependências e Executar o Projeto

Com os pré-requisitos instalados, siga o passo a passo abaixo:

### 1. Clonar o Repositório
```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd jev-super-mario
```

### 2. Criar e Ativar o Ambiente Virtual (`venv`)
O ambiente virtual evita conflito entre dependências de diferentes projetos:

- **Linux / macOS:**
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

- **Windows (PowerShell):**
  ```powershell
  python -m venv .venv
  .venv\Scripts\Activate.ps1
  ```
  *(Se encontrar erro de política de execução no PowerShell, execute antes: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`)*

- **Windows (CMD):**
  ```cmd
  python -m venv .venv
  .venv\Scripts\activate.bat
  ```

### 3. Instalar as Dependências do Projeto

Com a virtualenv ativada (você verá `(.venv)` no início da linha de comando):
```bash
pip install -r requirements.txt
```

### 4. Configurar a Chave de API

Você pode configurar sua chave via arquivo `.env` ou variável de terminal:

#### Opção A: Usando arquivo `.env` (Recomendado)
Copie o modelo existente:
```bash
cp .env.example .env
```
Abra o arquivo `.env` no seu editor de texto e insira a chave obtida no painel da TypeSafe:
```env
TYPESAFE_API_KEY=sua_chave_api_aqui
```

#### Opção B: Definindo no Terminal
- **Linux / macOS:**
  ```bash
  export TYPESAFE_API_KEY="sua_chave_api_aqui"
  ```
- **Windows (PowerShell):**
  ```powershell
  $env:TYPESAFE_API_KEY="sua_chave_api_aqui"
  ```
- **Windows (CMD):**
  ```cmd
  set TYPESAFE_API_KEY=sua_chave_api_aqui
  ```

### 5. Executar o Projeto

Você pode executar o projeto de duas formas:

#### Modo 1: Simulação Rápida no Terminal (`main.py`)
Envia um estado estático simulado da RAM para a API Jev e exibe a decisão tomada:
```bash
python main.py
```

#### Modo 2: Ver o Jev Jogando ao Vivo na Sua Tela (`play.py`) 🎮
Abre o emulador real do NES com uma janela gráfica contendo o jogo e a telemetria ao vivo da IA:
```bash
python play.py
```

- **Controles da janela:**
  - Pressione **`R`**: Reinicia a fase (*Restart*).
  - Pressione **`Esc`** ou **`Q`**: Fecha a janela.
- **Opções adicionais:**
  - Apenas a tela do jogo (sem dashboard lateral):
    ```bash
    python play.py --display game
    ```
  - Escolher outra fase (ex: Mundo 1-2):
    ```bash
    python play.py --env SuperMarioBros-1-2-v0
    ```

---

## Resolução de Problemas Comuns

- **`TypeSafeError: No API key was provided`**:
  A variável `TYPESAFE_API_KEY` não foi definida. Crie o arquivo `.env` ou execute `export TYPESAFE_API_KEY="sua-chave"`.

- **`TypeSafeAuthenticationError: 401 Cannot authenticate with the server`**:
  A chave de API informada é inválida ou expirou. Verifique sua chave no painel da TypeSafe.

- **Comando `python` ou `pip` não encontrado**:
  O Python não foi adicionado à variável de ambiente `PATH` do sistema. Reinstale certificando-se de marcar a opção "Add to PATH" (no Windows) ou verifique sua instalação no Linux/Mac.

- **Erro de script desabilitado no PowerShell (`ExecutionPolicy`)**:
  Execute `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` no PowerShell e tente ativar a venv novamente.
# jev-super-mario

Este é um projeto conceitual demonstrando como integrar o **Jev AI** (via SDK da TypeSafe) para jogar *Super Mario Bros.*. Ao invés de processar imagens, a arquitetura extrai o estado diretamente da memória (RAM) do emulador e toma decisões estruturadas em milissegundos.

O script `main.py` contém uma simulação de como enviar o estado do Mario (posição, inimigos próximos, buracos) e requisitar uma escolha de ação (`Choice`) e avaliação de perigo (`Score`) simultaneamente à API do Jev.

## Como Executar na Sua Máquina Local

Para testar o script e fazê-lo funcionar com a API real do Jev, você precisa configurar o ambiente de desenvolvimento local na sua máquina.

### Pré-requisitos
- Python 3.10 ou superior.
- Uma conta e uma chave de API na TypeSafe (`TYPESAFE_API_KEY`).

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone <URL_DO_SEU_REPOSITORIO>
   cd jev-super-mario
   ```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**
   ```bash
   python -m venv .venv

   # No Windows:
   .venv\Scripts\activate

   # No Linux/Mac:
   source .venv/bin/activate
   ```

3. **Instale o SDK do TypeSafe:**
   Você precisará instalar a biblioteca para comunicação com a API.
   ```bash
   pip install typesafe-sdk
   ```

4. **Configure sua chave de API:**
   Defina a variável de ambiente com a sua chave fornecida pela TypeSafe.

   *No Linux/Mac:*
   ```bash
   export TYPESAFE_API_KEY="sua-chave-api-aqui"
   ```
   *No Windows (PowerShell):*
   ```powershell
   $env:TYPESAFE_API_KEY="sua-chave-api-aqui"
   ```

5. **Execute a simulação:**
   ```bash
   python main.py
   ```
   O script exibirá a ação selecionada no terminal. Como ele utiliza um Mock do Emulador (classe `Emulator` dentro do arquivo `main.py`), ele não precisa abrir o jogo para rodar o conceito de decisão.

## Indo Além: Jogando de Fato

O `main.py` usa dados *mockados* simulando a RAM. Para fazer o Jev **realmente jogar** na sua tela, você precisará:

1. **Um emulador integrável:** Instalar bibliotecas como `gym-retro` ou `nes-py` juntamente com `gym-super-mario-bros`.
2. **A ROM do jogo:** Obter o arquivo `.nes` original do Super Mario Bros. (lembre-se das implicações legais de uso de ROMs).
3. **Substituir o estado fixo no código:** Extrair as variáveis (posição X, Y do Mario e inimigos) lendo os endereços da RAM diretamente e enviando-os como JSON na variável `game_state`.
4. **Acoplar o emulador real:** Substituir a classe `Emulator` provida em `main.py` pelos comandos de input físico que controlam o ambiente do emulador (ex: `env.step(acao)`).

Para referência avançada com o emulador funcional completo, confira o projeto da comunidade: [fhshaik/typesafe-mario](https://github.com/fhshaik/typesafe-mario).
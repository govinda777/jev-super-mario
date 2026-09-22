"""
Script para iniciar o Super Mario com o Jev AI jogando em tempo real na tela.
"""
import os
import sys
from dotenv import load_dotenv

load_dotenv()

if not os.environ.get("TYPESAFE_API_KEY"):
    print("❌ Erro: TYPESAFE_API_KEY não foi encontrada!")
    print("Certifique-se de configurar sua chave no arquivo .env ou exportar a variável.")
    sys.exit(1)

from typesafe_mario.cli import main

if __name__ == "__main__":
    # Se o usuário não passou argumentos específicos, usa os padrões recomendados
    if len(sys.argv) == 1:
        sys.argv = [
            "typesafe-mario",
            "play",
            "--env", "SuperMarioBros-1-1-v0",
            "--frames-per-decision", "8"
        ]
    else:
        # Permite passar parâmetros extras como: python play.py --display game
        sys.argv = ["typesafe-mario", "play"] + sys.argv[1:]

    main()

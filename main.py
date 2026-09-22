try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

from typesafe_sdk import TypeSafeClient, Choice, Score

client = TypeSafeClient()

# 1. Estado vindo da RAM do emulador
game_state = {
    "mario": {"x": 120, "y": 32, "speed_x": 2.5, "is_mid_jump": False},
    "nearest_enemy": {"type": "goomba", "distance_x": 28, "time_to_reach_ms": 300},
    "upcoming_gap": {"distance_x": 80, "width": 16}
}

# 2. Chamada paralela ao Jev
response = client.system_one(
    state=game_state,
    questions={
        "action": Choice(
            instructions="Escolha a melhor ação para manter o Mario vivo e avançando",
            criteria={
                "stand_still": "Parar a movimentação",
                "go_right": "Andar para a direita",
                "jump": "Pular",
                "run": "Correr para a direita",
                "run_and_jump": "Correr e pular sobre inimigos ou buracos"
            }
        ),
        "danger_level": Score(
            instructions="Avalie o perigo do momento atual",
            criteria=["Seguro", "Atenção", "Perigo iminente"]
        )
    }
)

# 3. Execução no jogo
action_answer = response.answers["action"]
danger_answer = response.answers["danger_level"]

print(f"Ação escolhida pelo Jev: {action_answer.choice} (confiança: {action_answer.confidence:.0%})")
print(f"Nível de perigo avaliado: score {danger_answer.score:.2f} (confiança: {danger_answer.confidence:.0%})")

# Mock do emulador para evitar erro de execução (NameError)
class Emulator:
    def press_buttons(self, action):
        print(f"Executando ação no emulador: {action}")

emulator = Emulator()
emulator.press_buttons(action_answer.choice)

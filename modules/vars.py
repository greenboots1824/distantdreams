from .utils import loadfile, detectclear

# Deixando variáveis estáticas aqui
systemclear = detectclear()
config = loadfile("config/config.json")
#state = utils.loadfile("state/save.json")

# Estado do jogo
status = {
    "part": "start",
    "nextpart": None,
    "nextfile": None,
    "index": 0
}

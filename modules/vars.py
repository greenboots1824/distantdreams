from .utils import loadfile
from .utils import detectclear

# Deixando variáveis estáticas aqui
startfile = "scenes/intro.json"

systemclear = detectclear()

configpath = "config/config.json"
config = loadfile(configpath)

savepath = f"state/{config["savename"]}.json"
savefile = loadfile(savepath)

# Estado do jogo
status = {
    "part" : "start",
    "actualfile": None,
    "nextpart": None,
    "nextfile": None,
    "print_name": None,
    "index": 0
}

from . import utils as util

# Deixando variáveis estáticas aqui
startfile = "scenes/intro.json"

systemclear = util.detectclear()

configpath = "config/config.json"

# Checando as configurações
util.resetconfig()

config = util.loadfile(configpath)

savepath = f"state/{config["savename"]}.json"
savefile = util.loadfile(savepath)

# Estado do jogo
status = {
    "part" : "start",
    "actualfile": None,
    "nextpart": None,
    "nextfile": None,
    "print_name": None,
    "index": 0
}

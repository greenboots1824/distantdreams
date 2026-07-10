# Distant Dreams

## Documentações

- [Guia de configurações](CONFIG.md)  
    Guia para a compreensão e realizar a configuração e cada opção do jogo.

- [Guia de Hacking](JSON.md)  
    Guia para a compreensão e realizar modificações sobre hacking do projeto.

- [README](../README.md)  
    Retorna para o início do projeto e consequentemente, toda a descrição do jogo.

## Padrão JSON

Aqui é onde toda a magia do projeto está. Como o projeto é movido por estes arquivos em JSON, a formatação deles é relativamente simples e você pode entender mais olhando o [`engine.py`](../modules/engine.py). Portanto, a seguir, farei questão de explicar como funciona alguns parâmetros.

Vamos supor que estamos falando de `intro.json` no exemplo abaixo:

``` json
{
	"start": {
		"dialogs": [
			{
				"person": "Pessoa 1",
				"text": "Texto 1"
			},
			{
				"person": "Pessoa 2",
				"text": "Texto 2"
			},
			{
				"person": "Pessoa 3",
				"text": "Texto 3"
			},
			{
				"person": "Pessoa 4",
				"text": "Texto 4",
				"nextpart": "proxima_parte"
			}
		]
	},	
},
```

Ao invés da cena só continuar, ele aponta para outra cena usando `"nextpart"` dentro da array `game["start"]["dialogs"][3]` que fica como:

``` python
nextpart = game["start"]["dialogs"][3]["nextpart"]

print(nextpart)
# "proxima_parte"
```

O design de index foi usado justamente pensado para ser lido como uma linha seguida:

```
"start":
   | "dialogs": [0][1][2][3]
    \       \             ^
     \        \           |
       \        \         |
game["start"]["dialogs"][index]
```

---

### Variáveis e Valores Estáticos

Perceba como há alguns trechos estáticos:

- `start` --- O nome `start` é o começo estático em todos os arquivos JSON, porém pode como qualquer outro nome;
- `dialogs` --- Array de diálogos contendo todo o material do jogo;
  - Observe como também os diálogos vêm quebrados. Por exemplo, para expressar uma grande frase, você quebra em pedaços, ficando em pequenos trechos para cada array;
- `person` --- Nome do personagem. Sem segredo;
- `text` --- Diálogo respectivo ao personagem `person`.

---

Agora, estes abaixo têm funções específicas e "especiais":

- `nextpart` --- É como um "ponteiro" para continuar a história. Se caso for `None` e `nextfile` também, o programa vai simplesmente parar. O ponteiro funciona somente para parte LOCAIS do arquivo;
  - Como exemplo, dentro do **mesmo arquivo** haver `parte1` e `parte2` e você fazer transição entre duas partes `parte1 -> parte2`;
- `nextfile` --- É quase o mesmo conceito do `nextpart`, porém ele aponta de fato para um arquivo. Entretanto, o arquivo específicado é **relativo** ao `distantdream.py` também.  
Logo, você usa um caminho como `scenes/EXEMPLO.json`.

---

Continuando no mesmo arquivo acima, temos a continuação a seguir:

``` json
{
    "proxima_parte": {
        "dialogs": [
            {
                "person": "Pessoa 1",
                "text": "Texto 1"
            },
            {
                "person": "Pessoa 2",
                "text": "Texto 2"
            },
            {
                "person": "Pessoa 3",
                "text": "Texto 3"
            },
            {
                "person": "Pessoa 4",
                "text": "\nVocê deseja fazer isto?",
                "question": true,
                "options": [
                    {
                        "option": "Sim",
                        "nextfile": "scenes/example.json"
                    },
                    {
                        "option": "Não",
                        "nextpart": "etc"
                    }
                ]
            }
        ]
    }
},

{
    "etc": { 
        "dialogs" : [
            {
                "person": "Pessoa 1",
                "text": "Texto 1" 
            },
            {
                ...
            }
        ]
    }
}
```

---

#### Mais Variáveis...

- `question` --- Se caso for `true` em JSON, logo a `engine.py` altera o funcionamento normal e verifica a array `options`. Onde você dentro coloca o `option` para informar o texto da opção e em seguida usa uma continuação como o `nextfile` ou `nextpart`;
  - Observe também que você não precisa toda hora definir `question` como `false` só para informar à engine que não é uma pergunta;
- `options` --- É a array com as escolhas de acordo com a pergunta.

---

### Funcionamento Python

Mas antes de prosseguirmos, primeiramente, é muito mais interessante comentar à respeito sobre o funcionamento interno de `engine.py` com a função interna `main()` processa estes arquivos.

- Observe acima que a engine recebe um parâmetro de tipo string com o caminho **relativo** do arquivo JSON. Isto é, por conta de `distantdream.py` se localizar no `rootdir` do programa, logo, os caminhos são simplesmente fornecidos para `FILE` como `scenes/EXAMPLE_FILE.json`.

A engine usa a seguinte estrutura de variável para realizar a leitura:

``` python
# Arquivo: utils.py

def loadfile(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
```

``` python
# Arquivo: vars.py

startfile = "scenes/intro.json"

configpath = "config/config.json"
config = loadfile(configpath)

status = {
    "part" : "start",
    "actualfile": None,
    "nextpart": None,
    "nextfile": None,
    "print_name": None,
    "index": 0
}
```

``` python
# Arquivo: engine.py 

from . import utils as util
from . import vars as var

# Carrega o jogo na memória
game = util.loadfile(var.startfile)

var.part = "start"
var.nextpart = None
var.nextfile = None

var.index = 0

# Loop main
while True:
    dialogs = game[var.part]["dialogs"]
    section = dialogs[var.index]
    dialog = section["text"]
    
    # ...
```

Cada variável desta aqui serve para armazenar um estado do jogo. Todas estas são mutáveis e pertencentes ao arquivo de armazenamento de variáveis `vars.py`:

- `game` --- Variável pelo qual carrega o conteúdo do jogo na memória;
- `dialogs` --- Carrega a `dialogs` do arquivo escolhido;
- `section` --- Carrega regiões de dados nas arrays de `dialogs` de JSON;
- `part` --- Armazena a parte dentro do arquivo onde se encontra o código;
  - A parte inicial e padrão do código é normalmente `start`. Esta parte é estática. Você pode alterar, mas saiba que isto é um padrão em meu código original.

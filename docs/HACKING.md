# Distant Dream

## Veja Também

- [JSON](JSON.md)
- [README](../README.md)

## Hacking

Por conta do projeto ser open-source, você pode usar, reutilizar, acrescentar, modificar, recriar suas próprias histórias, o que pode ser muito interessante para você. Dando base para uma infinidade de coisas!

O próprio design do projeto permite isto. Pois funciona da seguinte maneira:

```
distantdream (rootdir)
├── distantdream.py
├── modules
│   ├── engine.py
│   └── utils.py
├── scenes (folder)
│   └── intro.json (start file)
└── settings.json
```

Como é observado, por padrão, o projeto vem com algumas pastas e arquivos. Darei-lhe uma explicação bem breve do que esperar e os propósitos de cada pasta e arquivo.

### Python

#### `distantdreams.py`

É somente o "main" do projeto. É por onde o jogo chama os módulos e faz a execução de todo o projeto. Você pode executá-lo usando Python com:

- Windows

`py distantdreams.py` ou `python distantdreams.py`

- Linux/MacOS

`python distantdreams.py` ou `./distantdreams.py` (se houver a permissão de executar)

Depois o jogo abre-se normalmente, executando os módulos e fazendo todo o jogo funcionar.

#### `modules`

É a pasta onde os módulos do projeto ficam. Serve para justamente guardar tudo o que jogo precisa para funcionar. Por exemplo:

- `engine.py` é o motor do jogo. É ele quem lê o todo o conteúdo de algum arquivo JSON da pasta `scenes`.
- `utils.py` serve para armazenar funções como: "limpar tela", "efeito de digitação", etc. Praticamente utilitários internos mesmo.

É onde fica todo o funcionamento "nos bastidores" do projeto. Isto é, essencial. Pode ser colocado o que você quiser! Ou seja, acrescentar, modificar o que já existe e remover também.

### JSON

#### `scenes`

É a pasta onde fica-se todas as cenas, cenários, diálogos e tudo que envolve a parte do jogo principal. Dentro dele, ficam os arquivos JSON com todos os cenários.

Tudo começa por um arquivo escolhido para ser inicial, como exemplo o `intro.json`. Isto está definido no arquivo principal `distantdream.py` como:

``` python
from modules import engine

def main():
    engine.main("scenes/intro.json")

if __name__ == "__main__":
    main()
```

Neste caso, ele está chamando o `main(file)` de `engine.py` pra executar a interpretação do conteúdo de `intro.json` em `scenes`. Observe que é um caminho relativo, pois o *rootdir* é simplesmente `distantdreams`.

Claro, ninguém irá te impedir de começar por um arquivo de outro nome, além de ser totalmente possível.

O esquema feito é que cada arquivo representa um local. Por exemplo:

Na sua história, tem uma *intro*, *casa*, nesta casa, uma *cozinha*, *quarto*, *banheiro*, uma *rua* e *praça*. Aí, você faz cada cenário desse em um arquivo para cada:

```
scenes
├── bathroom.json
├── bedroom.json
├── house.json
├── intro.json
├── kitchen.json
├── road.json
└── square.json
```

Dentro de seus respectivos arquivos, tem seus cenários feitos a mão e desenhados com base na criatividade e nível de detalhes do criador.

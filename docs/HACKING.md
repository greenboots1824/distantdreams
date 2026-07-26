# Distant Dreams

## Documentações

- [Guia de configurações](CONFIG.md)  
    Guia para a compreensão e realizar a configuração e cada opção do jogo.

- [Guia de JSON](JSON.md)  
    Guia para a compreensão e realizar as configurações em relação ao JSON do jogo.

- [README](../README.md)  
    Retorna para o início do projeto e consequentemente, toda a descrição do jogo.

## Hacking

Por conta do projeto ser open-source, você pode usar, reutilizar, acrescentar, modificar, recriar suas próprias histórias, o que pode ser muito interessante para você. Dando base para uma infinidade de coisas!

O próprio design do projeto permite isto. Pois funciona da seguinte maneira:

```
distantdream (rootdir)
├── config
│   ├── config.json
│   └── defaultconfig.json
├── distantdreams.py
├── modules
│   ├── banner.py
│   ├── cli.py
│   ├── common.py
│   └── engine.py
├── scenes
│   └── intro.json (static file)
└── state
    └── save.json
```

Como é observado, por padrão, o projeto vem com algumas pastas e arquivos. Darei-lhe uma explicação bem breve do que esperar e os propósitos de cada pasta e arquivo.

### Explicação

#### `config`

É a pasta onde carrega as configurações do jogador. Para saber mais, consulte a [*documentação de configurações*](CONFIG.md).

- `config.json` é a configuração ativa do jogo, a configuração programada para ser modificada em jogo. Esta é a configuração pelo qual o jogo carrega e usa.
- `defaultconfig.json` é a configuração de reset do jogo. Útil caso você queira redefinir alguma configuração, verificar os valores ou de alguma forma, perdeu o arquivo de configuração. Esta configuração **não é** usada e nem modificada durante jogo.

#### `distantdreams.py`

É somente o "main" do projeto. É por onde o jogo chama os módulos e faz a execução de todo o projeto. Você pode executá-lo usando Python com:

##### Windows

`py distantdreams.py` ou `python distantdreams.py`

##### Linux/MacOS

`python distantdreams.py` ou `./distantdreams.py` (se houver a permissão de executar)

Se no caso de você usar `./` e der um erro como:  
`permission denied: ./distantdreams.py`  
Dê `chmod u+x distantdreams.py` e tente novamente.

Depois o jogo abre-se normalmente, executando os módulos e fazendo todo o jogo funcionar.

#### `modules` 

É a pasta onde os módulos do projeto ficam. Serve para justamente guardar tudo o que jogo precisa para funcionar. Por exemplo:

- `banner.py` é onde fica armazenado o banner/créditos e o aviso do jogo;
- `cli.py` é onde fica armazenado os argumentos do programa;
- `common.py` serve para armazenar funções como: "limpar tela", "efeito de digitação", etc. Praticamente utilitários internos e variáveis;
- `engine.py` é o motor do jogo. É ele quem lê o todo o conteúdo de algum arquivo JSON da pasta `scenes`.

É onde fica todo o funcionamento "nos bastidores" do projeto. Isto é, essencial. Pode ser moldado da forma que você quiser! Ou seja, acrescentar, modificar o que já existe e remover também.

#### `scenes`

É a pasta onde fica-se todas as cenas, cenários, diálogos e tudo que envolve a parte do jogo principal. Dentro dele, ficam os arquivos JSON com todos os cenários.

Tudo começa por um arquivo escolhido para ser inicial, como exemplo o `intro.json`. Isto está definido no arquivo principal `distantdreams.py`.  
Isto é, ele está chamando o `main()` de `engine.py`. Porém para executar a interpretação do conteúdo de `intro.json` em `scenes`, ele usa da variável `startfile` em `common.py`.  

- Observe que `startfile` é um caminho relativo, pois o *rootdir* é simplesmente `distantdreams`.

#### Considerações Finais

Claro, ninguém irá te impedir de começar por um arquivo de outro nome, além de ser totalmente possível.

O esquema feito é que cada arquivo representa um local. Por exemplo:

Na sua história, tem uma *intro*, *casa*, nesta casa, uma *cozinha*, *quarto*, *banheiro*, uma *rua* e *praça*. Após a definição do ambiente, você faz cada cenário desse para um arquivo cada:

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

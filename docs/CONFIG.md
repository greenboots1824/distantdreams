# Distant Dreams

## Documentações

- [Guia de JSON](JSON.md)  
    Guia para a compreensão e realizar as configurações em relação ao JSON do jogo.

- [Guia de Hacking](HACKING.md)  
    Guia para a compreensão e realizar modificações sobre hacking do projeto.

- [README](../README.md)  
    Retorna para o início do projeto e consequentemente, toda a descrição do jogo.

## Explicação

Se você não baixou o jogo na pressa sem ler miniciosamente esta parte essencial do projeto, parabéns por sua paciência!

A configuração do jogo funciona baseada em um arquivo de configuração em JSON. Portanto explicarei a função de dois arquivos JSON que podem ser encontrados na pasta `config`. 

- `config.json`  
    Este é o arquivo modificável e destinado ao usuário final.  
    O jogador deve usar este arquivo para customizar a experiência.  

    *O projeto vem por padrão sem este arquivo. É normal e esperado.  
    Você pode tanto copiar ele manualmente de `defaultconfig.json` ou simplesmente executar o jogo.*

- `defaultconfig.json`  
    Arquivo de configuração "imutável". Destinado somente para backups e como o "padrão" para se usar e inclusive restaurar o `config.json` ao padrão usando este.  
    *Não foi destinado para ser modificado pelo jogador final.*

*Observação: usarei os parâmetros de `defaultconfig.json` para nosssos exemplos.*

- `defaultconfig.json`

```json
{
    "interval_min": 0.02,
    "interval_max": 0.04,
    "pause_dialog": 0.25,
    "long_pause": 0.2,
    "pause_enter": false,
    "skip_warning": false,
    "skip_banner": false,
    "first_time": true,
    "clear_dialog": false,
    "savename": "save",
    "save": false,
    "load_savefile": false
}
```

---

#### `interval_min` / `interval_max`  

Ao ajustar estes valores (`min` deve ser menor que `max`), é alterado a velocidade que o programa digita os diálogos.

`random.uniform()` pega estes valores de tipo `float` e realiza um cálculo para que haja um número aleatório entre `min` e `max`.

#### `pause_dialog`

É o tempo entre uma linha de diálogos e o outro.  
É um valor de tipo de `float` em segundos.

#### `long_pause`

É o tempo entre uma linha de diálogos e o outro.  
É um valor de tipo de `float` em segundos.

Se caso `pause_enter` for `false`, logo haverá um tempo antes de se iniciar o próximo bloco de diálogos.

#### `pause_enter`

É um valor booleano que diz se usará ENTER entre os blocos de diálogos para continuar.

Portanto, se for `true`, a cada bloco de diálogo, ele solicitará que use ENTER para continuar.

#### `skip_banner`

É um valor booleano que diz respeito ao banner inicial do programa.

Permitindo ou não a exibição do banner inicial.

#### `skip_warning`

É um valor booleano que diz respeito ao aviso inicial do programa.

Permitindo selecionar se deseja ou não exibir o aviso inicial quando abrir o programa.

#### `first_time`

Variável que diz respeito se você já jogou o jogo antes.

Ela não é realmente destinada para o usuário final alterar, porém pode sim ser alterada.

Não é algo que pode trazer algo útil em troca ao configurar. Portanto, ele habilita apenas as perguntas no inicio do programa quando está `true`.

#### `clear_dialog`

Variável que define se deverá limpar o terminal após os blocos de diálogos.

Se for `true`, será limpo o terminal toda vez que sair de um bloco de diálogos ao outro.

#### `savename`

É o nome do arquivo de salvamento em JSON que ficará na pasta `state`.

Note que não é preciso colocar `.json` no final do nome. Além disso, você pode gerir vários arquivos de salvamento desta forma.

#### `save`

Define se deve ou não salvar o jogo quando usar `CTRL-C`.

Se caso `true`, o jogo salvará o arquivo `savefile` na pasta `state` quando sair usando o `CTRL-C`.

#### `load_savefile`

Define se deve ou não carregar o arquivo de salvamento de jogo.

Se caso for `true`, o jogo carregará o arquivo indicado.

*Detalhe: se o arquivo `savename` não existir, o programa vai apenas começar totalmente do zero.*

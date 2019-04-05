# Descrição

Este projeto trata do desenvolvimento de um software open source do tipo ChatBot que tem como objetivo:
- Ser capaz de tirar dúvidas técnicas relacionado a problemas de informática para o usuário final em um local de trabalho com arquitetura Cliente-Servidor;
- Ser capaz de conversar com o usuário final sobre outros assuntos utilizando a linguagem mais natural e próxima do humano o possível.

## Tecnologias incorporadas ao projeto:
- AIML(Artificial Intelligence Markup Language);
- Corpus;
- Google Sheets;
- Python 3.

## Instalação 
```
$ python3 -m venv ChatBot
$ cd ChatBot/
$ source bin/activate
$ git clone https://github.com/leonardogt4/Support-ChatBot.git
$ cd Support-ChatBot
$ pip3 install -r requirements.txt 

```
## Executar
Importante: Toda vez que sair do shell, deve-se executar o source para ativar o virtualenv: 
```source bin/activate``` dentro do  ChatBot/.

```
$ python3 ws.py
```
Acessar o navegador: http://127.0.0.1:8089/

## Estruturação das pastas
```
.
└── ChatBot
    ├──Support-ChatBot
        └──│ 
            ├── etc                 # Diretorio de configurações
            │   └── db.sqlite.sql
            ├── modules             # Diretorio de modulos gerais
            │    └── parole.py      # Classe  principal de resposta.
            │    └── models.py      # ORM de base de acesso ao banco de dados. 
            ├── README.md 
            ├── requirements.txt    # Depedencias Python
            ├── templates           # Paginas html
            │   └── index.html
            ├── vars                # Banco de dados
            │   └── chat.sqlite
            └── ws.py               # Executavel principal

```


## 

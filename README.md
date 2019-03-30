## Support-ChatBot-Python

# Instalação 
```
$ python3 -m venv ChatBot
$ cd ChatBot/
$ source bin/activate
$ git clone https://github.com/leonardogt4/Support-ChatBot.git
$ cd Support-ChatBot
$ pip3 install -r requirements.txt 

```
# Executar
Importante: Toda vez que sair do shell, deve-se executar o source para ativar o virtualenv: 
```source bin/activate``` dentro do  ChatBot/.

```
$ ./ws.py
```
Acessar o navegador: http://127.0.0.1:8089/

# Estruturação das pastas
```
├── etc                 # Diretorio de configurações
│   └── db.sqlite.sql
├── modules             # Diretorio de modulos gerais
├── README.md 
├── requirements.txt    # Depedencias Python
├── templates           # Paginas html
│   └── index.html
├── vars                # Banco de dados
│   └── db.sqlite
└── ws.py               # Executavel principal

```



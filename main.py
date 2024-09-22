import re

def categorizar_token(token):
    if re.match(r'^[a-zA-Z_]\w*$', token):
        return 'IDENTIFICADOR'
    elif re.match(r'^\d+$', token):
        return 'NÚMERO'
    elif re.match(r'^[+\-*/=]$', token):
        return 'OPERADOR'
    elif token in ['(', ')', '{', '}', ';']:
        return 'DELIMITADOR'
    else:
        return 'DESCONHECIDO'

def analisador_lexico(arquivo_entrada):
    try:
        with open(arquivo_entrada, 'r') as arquivo:
            for linha_num, linha in enumerate(arquivo, 1):
                tokens = re.findall(r'\w+|[+\-*/=(){};]', linha)
                for token in tokens:
                    categoria = categorizar_token(token)
                    print(f"Linha {linha_num}: Token '{token}' -> {categoria}")
    except FileNotFoundError:
        print(f"Arquivo '{arquivo_entrada}' não encontrado.")

arquivo_entrada = 'text.txt'

analisador_lexico(arquivo_entrada)
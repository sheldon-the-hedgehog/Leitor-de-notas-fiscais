import re

def extrair_chave_acesso(texto):
    chave = re.search(r'(\d{4} ){10}\d{4}', texto)
    if chave:
        return chave.group()
    else:
        return "dado não encontrado"
    
def extrair_data_emissão(texto):
    chave = re.search(r'\d{2}/\d{2}/\d{4}',texto)
    if chave:
        return chave.group()
    else:
        return "dado não encontrado"  

def extrair_valor_total(texto):
    chave = re.search(r'VALOR\n?\s*TOTAL:\s*\n?R?\$?\s*([\d\.,]+)', texto)
    if chave:
        return chave.group(1)
    else:
        return "dado não encontrado"
    
def extrair_ncms(texto):
    chaves =  re.findall(r'\b(\d{8})\b', texto)
    if chaves:
        chaves_unicas = sorted(set(chaves))
        return chaves_unicas 
    else:
        return "dado não encontrado"
        
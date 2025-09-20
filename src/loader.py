import fitz
import os
import checks as ck
import extrator as ex
import pandas as pd

def processar_pasta(pasta, caminho_planilha):
    dados = []

    for arquivo in os.listdir(pasta):
        if arquivo.lower().endswith('.pdf'):
            conteudo_arquivo = ""
            arquivo = os.path.join(pasta, arquivo)
            
            with fitz.open(arquivo) as doc:
                for pagina in doc:
                    conteudo_arquivo += pagina.get_text()

            chave_de_acesso = ex.extrair_chave_acesso(conteudo_arquivo)
            data_de_emissão = ex.extrair_data_emissão(conteudo_arquivo)
            valor_total = ex.extrair_valor_total(conteudo_arquivo)
            ncms = ex.extrair_ncms(conteudo_arquivo)

            if ck.verifica_ncms(ncms) and ck.verfica_data(data_de_emissão):
                dados.append({
                    "Chave de acesso": chave_de_acesso,
                    "Data de emissão": data_de_emissão,
                    "Valor total": valor_total
                })
    
    dados_finais = pd.DataFrame(dados)
    dados_finais.to_excel(caminho_planilha, index=False)
    print("Planilha criada com sucesso")

def processar_arquivo_individual(arquivo):
    conteudo_arquivo = ""
    with fitz.open(arquivo) as doc:
        for pagina in doc:
            conteudo_arquivo += pagina.get_text()

    chave_de_acesso = ex.extrair_chave_acesso(conteudo_arquivo)
    data_de_emissão = ex.extrair_data_emissão(conteudo_arquivo)
    valor_total = ex.extrair_valor_total(conteudo_arquivo)
    ncms = ex.extrair_ncms(conteudo_arquivo)

    print(f"\na chave de acesso é: {chave_de_acesso}")
    print(f"a data de emissão é: {data_de_emissão}")       
    print(f"o valor total é: R$ {valor_total}")
    print(f"ncm: {ncms}")    

    if ck.verifica_ncms(ncms) and ck.verfica_data(data_de_emissão):
        print("financiavel")
    else: 
        print("não financiavel")


            
  
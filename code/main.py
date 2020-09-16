##Arquivo de inicialização do processo de cópia dos arquivos para o Bucket na GCP
##Nome do Bucket: teste_boavista
##Repositorio: source_data
##Desc: Por ser um teste, as bases estarão HARDCODED no código

from src_bigquery.envia_compboss_bigquery import client_load_comp_boss
from src_bigquery.envia_billofmaterials_bigquery import client_load_bill_of_materials
from src_bigquery.envia_pricequote_bigquery import client_load_price_quote
from valida_arq_origem import valida_comp_boss, valida_bill_of_materials, valida_price_quote
from copia_arq_bucket import upload_arquivo
from datetime import datetime

print('###  PROGRAMA DE CARGA DAS 3 BASES  ###')
print('### Desenvolvido por: Leonardo Lins ###')
print('###         Data: 15/09/2020        ###\n')
print('Início do processamento...\n')

###
###Declaracao de variaveis
###

hora_processamento = datetime.now()

nome_bucket = 'teste_boavista'
repo_destino = 'source_data'

v_comp_boss_name = 'source_data/comp_boss.csv'
v_arq_comp_boss = '/home/leonardo/Entrevista/TesteEngenheiroDados/data/comp_boss/comp_boss.csv'

v_bill_of_materials_name = 'source_data/bill_of_materials.csv'
v_bill_of_materials_path = '/home/leonardo/Entrevista/TesteEngenheiroDados/data/bill_of_materials/bill_of_materials.csv'

v_price_quote_name = 'source_data/price_quote.csv'
v_price_quote_path = '/home/leonardo/Entrevista/TesteEngenheiroDados/data/price_quote/price_quote.csv'

#############################################
###                                         #
###     BASE COMP_BOSS                      #
###                                         #

v_valida_comp_boss = valida_comp_boss()

#se a base comp_boss.csv for existente, ela será copiada para o bucket via GSUTIL
if v_valida_comp_boss == True:
	print(f'{hora_processamento} Iniciando processamento...')
	v_exec_comp_boss = upload_arquivo(nome_bucket, v_arq_comp_boss, v_comp_boss_name)

	if v_exec_comp_boss == True:
		print(f'{hora_processamento} Processo de carga no Storage da base comp_boss concluído.')
	else:
		print(f'{hora_processamento} Erro no processo de copia da base comp_boss. Programa copia_arq_bucket.py')

else:
	print(f'{hora_processamento} Erro ao validar disponibilidade da base comp_boss na origem')

##Inicio do processo de carga da base de dados COMP_BOSS.csv no BigQuery
v_executa_bigquery_compboss = client_load_comp_boss()

#############################################
###                                         #
###     BASE bill_of_materials              #
###                                         #
                                 
v_bill_of_materials = valida_bill_of_materials()

#se a base bill_of_materials.csv for existente, ela será copiada para o bucket via GSUTIL
if v_bill_of_materials == True:
	print(f'{hora_processamento} Iniciando processamento...')
	v_exec_copy_bill = upload_arquivo(nome_bucket, v_bill_of_materials_path, v_bill_of_materials_name)

	if v_exec_copy_bill == True:
		print(f'{hora_processamento} Processo de carga no Storage da base bill_of_materials concluído.')
	else:
		print(f'{hora_processamento} Erro no processo de copia da base bill_of_materials. Programa copia_arq_bucket.py')

else:
	print(f'{hora_processamento} Erro ao validar disponibilidade da base bill_of_materials na origem')

##Inicio do processo de carga da base de dados bill_of_materials.csv no BigQuery
v_executa_bigquery_billofmaterials = client_load_bill_of_materials()

#############################################
###                                         #
###     BASE price_quote                    #
###                                         #

v_price_quote = valida_price_quote()

#se a base price_quote.csv for existente, ela será copiada para o bucket via GSUTIL
if v_price_quote == True:
	print(f'{hora_processamento} Iniciando processamento...')
	v_exec_copy_price = upload_arquivo(nome_bucket, v_price_quote_path, v_price_quote_name)

	if v_exec_copy_price == True:
		print(f'{hora_processamento} Processo de carga da base no Storage copy_price_quote concluído.')
	else:
		print(f'{hora_processamento} Erro no processo de copia da base copy_price_quote. Programa copia_arq_bucket.py')

else:
	print(f'{hora_processamento} Erro ao validar disponibilidade da base copy_price_quote na origem')

##Inicio do processo de carga da base de dados price_quote.csv no BigQuery
v_executa_bigquery_price_quote = client_load_price_quote()


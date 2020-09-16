##Este programa realiza a validação dos arquivos na origem para carrega-los no Bucket

import os
from datetime import datetime
#Declaração das variaveis de nome das bases e PATH

hora_processamento = datetime.now()

v_comp_boss_name = 'comp_boss.csv'
v_arq_comp_boss = '/home/leonardo/Entrevista/TesteEngenheiroDados/data/comp_boss/comp_boss.csv'
v_arq_comp_boss_valid = os.path.exists('/home/leonardo/Entrevista/TesteEngenheiroDados/data/comp_boss/comp_boss.csv')

v_bill_of_materials_name = 'bill_of_materials.csv'
v_bill_of_materials = '/home/leonardo/Entrevista/TesteEngenheiroDados/data/bill_of_materials/bill_of_materials.csv'
v_bill_of_materials_valid = os.path.exists('/home/leonardo/Entrevista/TesteEngenheiroDados/data/bill_of_materials/bill_of_materials.csv')

v_price_quote_name = 'price_quote.csv'
v_price_quote = '/home/leonardo/Entrevista/TesteEngenheiroDados/data/price_quote/price_quote.csv'
v_price_quote_valid = os.path.exists('/home/leonardo/Entrevista/TesteEngenheiroDados/data/price_quote/price_quote.csv')

#Funcao de validação da existência da base comp_boss
def valida_comp_boss():

	if v_arq_comp_boss_valid == True:
		print(f'{hora_processamento} == Base {v_comp_boss_name} existente na origem!')
		print(f'{hora_processamento} Aprovada para processamento.')
		return True
	else:
		print(f'{hora_processamento} Houve um problema, a base não foi localizada ou o nome está incorreto!')
		print(f'{hora_processamento} Não aprovada para processamento.')
		return False

#Funcao de validação da existência da base bill_of_materials
def valida_bill_of_materials():

	if v_bill_of_materials_valid == True:
		print(f'\n{hora_processamento} == Base {v_bill_of_materials_name} existente na origem!')
		print(f'{hora_processamento} Aprovada para processamento.')
		return True
	else:
		print(f'{hora_processamento} Houve um problema, a base não foi localizada ou o nome está incorreto!')
		print(f'{hora_processamento} Não aprovada para processamento.')
		return False

#Funcao de validação da existência da base price_quote
def valida_price_quote():

	if v_price_quote_valid == True:
		print(f'\n{hora_processamento} == Base {v_price_quote_name} existente na origem!')
		print(f'{hora_processamento} Aprovada para processamento.')
		return True
	else:
		print(f'{hora_processamento} Houve um problema, a base não foi localizada ou o nome está incorreto!')
		print(f'{hora_processamento} Não aprovada para processamento.')
		return False

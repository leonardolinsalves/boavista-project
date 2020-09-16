from copia_arq_bucket import upload_arquivo

nome_bucket = 'teste_boavista'
repo_destino = 'source_data'

v_comp_boss_name = 'comp_boss.csv'
v_arq_comp_boss = '/home/leonardo/Entrevista/TesteEngenheiroDados/data/comp_boss/comp_boss.csv'

v_bill_of_materials_name = 'bill_of_materials.csv'
v_bill_of_materials = '/home/leonardo/Entrevista/TesteEngenheiroDados/data/bill_of_materials/bill_of_materials.csv'

v_price_quote_name = 'price_quote.csv'
v_price_quote = '/home/leonardo/Entrevista/TesteEngenheiroDados/data/price_quote/price_quote.csv'

upload_arquivo(nome_bucket, v_arq_comp_boss, repo_destino)
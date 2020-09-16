from google.cloud import bigquery
from datetime import datetime

hora_processamento = datetime.now()
key_2 = '/home/leonardo/Entrevista/key_access/key_2.json'

print(f'{hora_processamento} Iniciando processo de carga do arquivo do Bucket no Bigquery')

def client_load_price_quote():

    # Construindo um Object Client do Bigquery, utilizando a chave .json de autenticação
    client = bigquery.Client.from_service_account_json(key_2)

    # id da tabela que será criada - <projeto>.<conjuntodedados>.<tabela>
    table_id = "apt-entropy-289618.conjunto_dados_boavista.price_quote"

    #Layout da base COMP_BOSS para carga no bigquery
    job_config = bigquery.LoadJobConfig(
        schema=[
            bigquery.SchemaField("tube_assembly_id", "STRING"),
            bigquery.SchemaField("supplier", "STRING"),
            bigquery.SchemaField("quote_date", "STRING"),
            bigquery.SchemaField("annual_usage", "STRING"),
            bigquery.SchemaField("min_order_quantity", "STRING"),
            bigquery.SchemaField("bracket_pricing", "STRING"),
            bigquery.SchemaField("quantity", "STRING"),
            bigquery.SchemaField("cost", "STRING"),
        ],
        skip_leading_rows=1,
    )
    uri = "gs://teste_boavista/source_data/price_quote.csv"

    load_job = client.load_table_from_uri(
        uri, table_id, job_config=job_config
    )  #Criando uma requisição de API

    load_job.result()  #Aguarda execução do Job

    table = client.get_table(table_id)
    print(f"{hora_processamento} Foram carregados {table.num_rows} linhas na tabela {table_id}")
    # Fim processo


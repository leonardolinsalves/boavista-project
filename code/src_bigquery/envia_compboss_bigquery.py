from google.cloud import bigquery
from datetime import datetime

hora_processamento = datetime.now()
key_2 = '/home/leonardo/Entrevista/key_access/key_2.json'

print(f'{hora_processamento} Iniciando processo de carga do arquivo do Bucket no Bigquery')

def client_load_comp_boss():

    # Construindo um Object Client do Bigquery, utilizando a chave .json de autenticação
    client = bigquery.Client.from_service_account_json(key_2)

    # id da tabela que será criada - <projeto>.<conjuntodedados>.<tabela>
    table_id = "apt-entropy-289618.conjunto_dados_boavista.comp_boss"

    #Layout da base COMP_BOSS para carga no bigquery
    job_config = bigquery.LoadJobConfig(
        schema=[
            bigquery.SchemaField("component_id", "STRING"),
            bigquery.SchemaField("component_type_id", "STRING"),
            bigquery.SchemaField("type", "STRING"),
            bigquery.SchemaField("connection_type_id", "STRING"),
            bigquery.SchemaField("outside_shape", "STRING"),
            bigquery.SchemaField("base_type", "STRING"),
            bigquery.SchemaField("height_over_tube", "STRING"),
            bigquery.SchemaField("bolt_pattern_long", "STRING"),
            bigquery.SchemaField("bolt_pattern_wide", "STRING"),
            bigquery.SchemaField("groove", "STRING"),
            bigquery.SchemaField("base_diameter", "STRING"),
            bigquery.SchemaField("shoulder_diameter", "STRING"),
            bigquery.SchemaField("unique_feature", "STRING"),
            bigquery.SchemaField("orientation", "STRING"),
            bigquery.SchemaField("weight", "STRING"),
        ],
        skip_leading_rows=1,
    )
    uri = "gs://teste_boavista/source_data/comp_boss.csv"

    load_job = client.load_table_from_uri(
        uri, table_id, job_config=job_config
    )  #Criando uma requisição de API

    load_job.result()  #Aguarda execução do Job

    table = client.get_table(table_id)
    print(f"{hora_processamento} Foram carregados {table.num_rows} linhas na tabela {table_id}")
    # Fim processo


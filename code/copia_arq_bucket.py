#Programa de copia de dados para o bucket utilizando a ferramenta GSUTIL

from google.cloud import storage
import os
from datetime import datetime

#Declaração das variáveis
hora_processamento = datetime.now()
key_2 = '/home/leonardo/Entrevista/key_access/key_2.json'

#Inicio das funcoes com execucao dos copies dos dados
import sys


def upload_arquivo(bucket_name, source_file_name, destination_blob_name):
    """Carregando o arquivo no Bucket."""
    # bucket_name = "your-bucket-name"
    # source_file_name = "local/path/to/file"
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client.from_service_account_json(key_2)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        f"{hora_processamento} Arquivo {source_file_name} carregado com sucesso em {destination_blob_name}"
        )
    return True

#!/usr/bin/python3
import base64
from azure.identity import DefaultAzureCredential
from azure.keyvault.certificates import CertificateClient
from azure.keyvault.secrets import SecretClient
from cryptography.hazmat.primitives.serialization import pkcs12
from cryptography.hazmat.primitives import serialization
import os

### THIS SECTION TO BE WRITTEN BY YOU ###

credential = DefaultAzureCredential()

vault_url = "https://pa193-keyvault-petrj.vault.azure.net/"
client = SecretClient(vault_url=vault_url, credential=credential)

secret_name = os.getenv("client_secret")
print(secret_name)
certificate_secret = client.get_secret(secret_name)


### PARSE CERTIFICATE AND STORE TO FILE

cert_bytes = base64.b64decode(certificate_secret.value)
private_key, public_certificate, additional_certificates = pkcs12.load_key_and_certificates(cert_bytes,None)

with open ("/data/pa193-cert.key", "wb") as prv_file:

    key = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )
    prv_file.write( key )

with open ("/data/pa193-cert.cert", "wb") as pub_file:

    pem = public_certificate.public_bytes(
        encoding=serialization.Encoding.PEM        
    )

    pub_file.write( pem )

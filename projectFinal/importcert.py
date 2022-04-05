import boto3
import gencert
from os.path import exists
def generatecertificate():
    if exists("arn.txt"):
        f = open("arn.txt", "r+")
        return f.read()
    else:
        acm = boto3.client('acm')
        response = acm.import_certificate(
        Certificate=gencert.certifictate_pem,
        PrivateKey=gencert.private_key_pem,
        CertificateChain=gencert.ca_certifictate_pem,
  )
        arn = response["CertificateArn"]
        f = open("arn.txt", "w+")
        f.write(arn)
        return arn
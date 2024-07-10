from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import requests
import json
import os

def generateDid():
  # Generate RSA key pair
  key = rsa.generate_private_key(
      public_exponent=65537,
      key_size=2048,
  )

  private_key = key.private_bytes(
      encoding=serialization.Encoding.PEM,
      format=serialization.PrivateFormat.TraditionalOpenSSL,
      encryption_algorithm=serialization.NoEncryption()
  )

  public_key = key.public_key().public_bytes(
      encoding=serialization.Encoding.PEM,
      format=serialization.PublicFormat.SubjectPublicKeyInfo
  )

  did_document = {
      "@context": "https://www.w3.org/ns/did/v1",
      "id": "did:web:ryan-boustany.github.io",
      "verificationMethod": [
          {
              "id": "did:web:ryan-boustany.github.io#key-1",
              "type": "RsaVerificationKey2018",
              "controller": "did:web:ryan-boustany.github.io",
              "publicKeyPem": public_key.decode('utf-8')
          }
      ],
      "authentication": [
          "did:web:ryan-boustany.github.io#key-1"
      ]
  }

  # Create .well-known directory if it doesn't exist
  os.makedirs('.well-known', exist_ok=True)

  # Save DID document to .well-known/did.json
  with open('.well-known/did.json', 'w') as f:
      json.dump(did_document, f, indent=4)
    
  return private_key

if __name__ == "__main__":
   print(generateDid())
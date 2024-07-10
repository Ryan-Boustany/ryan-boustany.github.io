import requests
import json


def verifyDID():
  did_url = "https://ryan-boustany.github.io/.well-known/did.json"
  response = requests.get(did_url)

  if response.status_code == 200:
      did_document = response.json()
      return True
  else:
      return False


if __name__ == "__main__":
   print(verifyDID())
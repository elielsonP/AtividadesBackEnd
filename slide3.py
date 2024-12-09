from pydantic import BaseModel
from threading import Thread
import requests
import time
import uvicorn

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Numeros(BaseModel):
  numero1: float
  numero2: float
@app.post('/mutiplicacao')
def multiplicar(numeros: Numeros):
  resultado = numeros.numero1 * numeros.numero2
  return {'resultado': resultado}

def iniciar_servidor():
  conf = uvicorn.Config(app, host="127.0.0.1", port=8000, 
   log_level="info")
  server = uvicorn.Server(conf)   # Changed 'config' to 'conf'
  server.run()

thread_servidor = Thread(target=iniciar_servidor)
thread_servidor.start()

time.sleep(5)  # Increased sleep time to 5 seconds to give the server more time to start

dados = {'numero1': 2, 'numero2': 1}
response = requests.post('http://127.0.0.1:8000/mutiplicacao', json=dados)

if response.status_code == 200:
  print(response.json())
else:
  print("Erro na requisição", response.status_code)
from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

# Contador de llamadas
call_counter = 0


'''
Returns the current date in the format specified by the user.
'''
@app.post("/fecha")
def get_date(formato_largo: bool):
    global call_counter
    call_counter += 1
    now = datetime.now()
    if formato_largo:
        return now.strftime("%Y-%m-%d %H:%M:%S")
    else:
        return now.strftime("%Y-%d-%m")


'''
Returns the number of calls to the server.
'''
@app.get("/contador")
def get_counter():
    global call_counter
    return {"contador": call_counter}


#Para ejecutar correr en consola lo siguiente:
# uvicorn app:app --reload --host 0.0.0.0

#Para chequear la request POST se puede utilizar el programa POSTMAN.
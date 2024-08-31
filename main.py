from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Modelo de datos para una película
class Pelicula(BaseModel):
    id: int
    titulo: str
    director: str
    año: int
    genero: str

# Base de datos simulada
peliculas_db = []

# Endpoint para obtener todas las películas
@app.get("/PELICULAS", response_model=List[Pelicula])
def obtener_peliculas():
    return peliculas_db

# Endpoint para obtener una película por ID
@app.get("/OBTENER INFORMACION/{pelicula_id}", response_model=Pelicula)
def obtener_pelicula(pelicula_id: int):
    for pelicula in peliculas_db:
        if pelicula.id == pelicula_id:
            return pelicula
    raise HTTPException(status_code=404, detail="Película no encontrada")

# Endpoint para agregar una nueva película
@app.post("/AGREGAR PELICULAS", response_model=Pelicula)
def agregar_pelicula(pelicula: Pelicula):
    peliculas_db.append(pelicula)
    return pelicula

# Endpoint para actualizar una película existente
@app.put("/ACTUALIZAR PELICULAS/{pelicula_id}", response_model=Pelicula)
def actualizar_pelicula(pelicula_id: int, pelicula_actualizada: Pelicula):
    for index, pelicula in enumerate(peliculas_db):
        if pelicula.id == pelicula_id:
            peliculas_db[index] = pelicula_actualizada
            return pelicula_actualizada
    raise HTTPException(status_code=404, detail="Película no encontrada")

# Endpoint para eliminar una película
@app.delete("/ELIMINAR PELICULAS/{pelicula_id}")
def eliminar_pelicula(pelicula_id: int):
    for index, pelicula in enumerate(peliculas_db):
        if pelicula.id == pelicula_id:
            del peliculas_db[index]
            return {"detail": "Película eliminada"}
    raise HTTPException(status_code=404, detail="Película no encontrada")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

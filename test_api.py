from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Test API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    query: str

responses = {
    'horario': 'Nuestro horario es de lunes a viernes de 9:00 AM a 6:00 PM',
    'contacto': 'Puedes contactarnos al email soporte@empresa.com o al teléfono 123-456-7890',
    'productos': 'Ofrecemos servicios de desarrollo web, aplicaciones móviles y consultoría',
    'precios': 'Los precios varían según el proyecto. Contáctanos para cotización',
    'ubicacion': 'Estamos ubicados en el centro de la ciudad',
    'soporte': 'Nuestro soporte está disponible 24/7'
}

@app.post("/api/query")
async def query_test(request: QueryRequest):
    query = request.query.lower()
    
    for key, answer in responses.items():
        if key in query:
            return {"success": True, "answer": answer}
    
    return {
        "success": False,
        "answer": "No encontré información. Intenta: horario, contacto, productos, precios, ubicacion, soporte"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Copilot Studio API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    query: str

def get_db_connection():
    # Railway proporciona DATABASE_URL automáticamente
    database_url = os.getenv("DATABASE_URL")
    if database_url:
        return psycopg2.connect(database_url)
    else:
        # Fallback para desarrollo local
        return psycopg2.connect(
            host=os.getenv("DB_HOST", "localhost"),
            database=os.getenv("DB_NAME", "chatbot_db"),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT", "5432")
        )

@app.post("/api/query")
async def query_database(request: QueryRequest):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute(
            "SELECT answer FROM faq WHERE question ILIKE %s LIMIT 1",
            (f"%{request.query}%",)
        )
        
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        
        if result:
            return {"success": True, "answer": result[0]}
        else:
            return {
                "success": False, 
                "answer": "No encontré información sobre esa consulta. ¿Puedes ser más específico?"
            }
            
    except Exception as e:
        return {"success": False, "answer": "Error al procesar la consulta"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
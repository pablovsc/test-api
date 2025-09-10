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

@app.get("/api/query")
async def query_database():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute(
            "SELECT question, answer FROM faq "
        )
        """ WHERE question ILIKE %s",
            (f"%{request.query}%",)
        """
        
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        
        if results:
            if len(results) == 1:
                return {"success": True, "answer": results[0][1]}
            else:
                answers = [{"topic": row[0], "answer": row[1]} for row in results]
                return {"success": True, "multiple_results": True, "answers": answers}
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
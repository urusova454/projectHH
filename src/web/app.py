import psycopg2
import uvicorn
from src.settings import PORT, PASSWORD, DBNAME, HOST, USER

from src.repos.vacancies import Vacancy
from fastapi import Depends, FastAPI, status
from pydantic import BaseModel

app = FastAPI()

def get_conn():
    try:
        conn = psycopg2.connect(
            port=PORT,
            password=PASSWORD,
            dbname=DBNAME,
            host=HOST,
            user=USER
        )
        yield conn
        conn.commit()
    except BaseException:
        conn.rollback()
    finally:
        conn.close()

class VacancyCreate(BaseModel):
    name_vacancy: str
    salary: int
    address: str
    description: str
    url: str


@app.get("/vacancies")
def get_all_vacancies(conn = Depends(get_conn)):
    vacancy_repo = Vacancy(conn)
    vacancies = vacancy_repo.get_all()
    return {"vacancies": vacancies}

@app.get("/vacancies/{vacancy_id}")
def get_vacancy(vacancy_id: int, conn = Depends(get_conn)):
    vacancy_repo = Vacancy(conn)
    vacancy = vacancy_repo.get(vacancy_id)
    return vacancy.model_dump_json()

@app.post("/vacancies", status_code=status.HTTP_201_CREATED)
def create_vacancy(vacancy: VacancyCreate, conn = Depends(get_conn)):
    vacancy_repo = Vacancy(conn)
    vacancy_repo.create((vacancy.name_vacancy, vacancy.salary, vacancy.address, vacancy.description, vacancy.url))
    return vacancy

@app.put("/vacancies/{vacancy_id}")
def update_vacancy(vacancy_id: int,vacancy: VacancyCreate, conn = Depends(get_conn)):
    vacancy_repo = Vacancy(conn)
    new_values = (
        vacancy.name_vacancy,
        vacancy.salary,
        vacancy.address,
        vacancy.description,
        vacancy.url
    )
    vacancy = vacancy_repo.update(vacancy_id, new_values)
    return vacancy

@app.delete("/vacancies/{vacancy_id}")
def delete_vacancy(vacancy_id: int, conn = Depends(get_conn)):
    vacancy_repo = Vacancy(conn)
    vacancy = vacancy_repo.delete(vacancy_id)
    return vacancy





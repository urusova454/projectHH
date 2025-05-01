from src.repos.vacancies import Vacancy
from src.config.database import conn
from fastapi import Depends, FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()


class VacancyCreate(BaseModel):
    name_vacancy: str
    salary: int
    address: str
    description: str
    url: str


@app.get("/vacancies")
def get_all_vacancies(conn = Depends(conn)):
    vacancy_repo = Vacancy(conn)
    vacancies = vacancy_repo.get_all()
    return {"vacancies": vacancies}

@app.get(
    "/vacancies/{vacancy_id}",
    description="Получение вакансии по идентификатору"
)
def get_vacancy(vacancy_id: int, conn = Depends(conn)):
    vacancy_repo = Vacancy(conn)
    vacancy = vacancy_repo.get(vacancy_id)
    if not vacancy:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Вакансии с UUID: '{vacancy_id}' не существует"
        )
    return vacancy.model_dump_json()

@app.post(
    "/vacancies",
    status_code=status.HTTP_201_CREATED
)
def create_vacancy(vacancy: VacancyCreate, conn = Depends(conn)):
    vacancy_repo = Vacancy(conn)
    vacancy_repo.create((vacancy.name_vacancy, vacancy.salary, vacancy.address, vacancy.description, vacancy.url))
    return vacancy

@app.put(
    "/vacancies/{vacancy_id}",
    description="Обновление данных по вакансии"
)
def update_vacancy(vacancy_id: int,vacancy: VacancyCreate, conn = Depends(conn)):
    vacancy_repo = Vacancy(conn)
    if not vacancy_repo.get(vacancy_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Вакансии с UUID: '{vacancy_id}' не существует"
        )
    new_values = (
        vacancy.name_vacancy,
        vacancy.salary,
        vacancy.address,
        vacancy.description,
        vacancy.url
    )
    vacancy = vacancy_repo.update(vacancy_id, new_values)
    return vacancy

@app.delete(
    "/vacancies/{vacancy_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    description="Удаление вакансии по идентификатору",
)
def delete_vacancy(vacancy_id: int, conn = Depends(conn)):
    vacancy_repo = Vacancy(conn)
    if not vacancy_repo.get(vacancy_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Вакансии с UUID: '{vacancy_id}' не существует"
        )
    vacancy = vacancy_repo.delete(vacancy_id)
    return vacancy





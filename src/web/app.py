from src.repos.vacancies import VacancyRepository
from src.config.database import get_conn
from fastapi import Depends, FastAPI, status, HTTPException
from pydantic import BaseModel
from uuid import UUID, uuid4
from src.web.schemas.vacancy import VacancySchema
from src.web.dependencies.vacancy import VacancyList
from src.domain.vacancies import Vacancy
app = FastAPI()

@app.get(
    "/vacancies",
    status_code=status.HTTP_200_OK,
    description="Получение списка всех вакансий",
    response_model=VacancyList,
)
def get_all_vacancies(conn = Depends(get_conn)):
    vacancy_repo = VacancyRepository(conn)
    vacancies = vacancy_repo.get_all()
    vacancies_data = [Vacancy.model_validate(v) for v in vacancies]
    return {"vacancies": vacancies_data}

@app.get(
    "/vacancies/{vacancy_id}",
    status_code=status.HTTP_200_OK,
    description="Получение вакансии по идентификатору",
    response_model=Vacancy
)
def get_vacancy(vacancy_id: UUID, conn = Depends(get_conn)):
    vacancy_repo = VacancyRepository(conn)
    vacancy = vacancy_repo.get(vacancy_id)
    if not vacancy:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Вакансии с UUID: '{vacancy_id}' не существует"
        )
    return vacancy

@app.post(
    "/vacancies",
    status_code=status.HTTP_201_CREATED,
    description="Создание вакансии",
    response_model=Vacancy
)
def create_vacancy(vacancy: VacancySchema, conn = Depends(get_conn)):
    id = uuid4()
    vacancy_repo = VacancyRepository(conn)
    vacancy_repo.create((str(id),vacancy.name, vacancy.salary, vacancy.address, vacancy.description, vacancy.url))

    return vacancy

@app.put(
    "/vacancies/{vacancy_id}",
    status_code=status.HTTP_200_OK,
    description="Обновление данных по вакансии",
    response_model=Vacancy
)
def update_vacancy(vacancy_id: UUID,vacancy: VacancySchema, conn = Depends(get_conn)):
    vacancy_repo = VacancyRepository(conn)
    if not vacancy_repo.get(vacancy_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Вакансии с UUID: '{vacancy_id}' не существует"
        )
    new_values = (
        vacancy.name,
        vacancy.salary,
        vacancy.address,
        vacancy.description,
        vacancy.url
    )
    vacancy = vacancy_repo.update(str(vacancy_id), new_values)
    return vacancy

@app.delete(
    "/vacancies/{vacancy_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    description="Удаление вакансии по идентификатору",
    response_model=None
)
def delete_vacancy(vacancy_id: UUID, conn = Depends(get_conn)):
    vacancy_repo = VacancyRepository(conn)
    if not vacancy_repo.get(vacancy_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Вакансии с UUID: '{vacancy_id}' не существует"
        )
    vacancy = vacancy_repo.delete(str(vacancy_id))
    return vacancy





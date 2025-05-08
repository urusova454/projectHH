from src.domain.vacancies import Vacancy
from fastapi import Depends, FastAPI, status, HTTPException

from src.repos.vacancies import VacancyRepo
from src.config.database import get_conn
from src.web.schemas.vacancy import VacancySchema
from src.web.dependencies.vacancy import VacancyList
from uuid import UUID, uuid4

app = FastAPI()


@app.get(
    "/vacancies",
    status_code=status.HTTP_200_OK,
    description="Получение списка всех вакансий",
    response_model = VacancyList
)
def get_all_vacancies(conn = Depends(get_conn)):
    vacancy_repo = VacancyRepo(conn)
    vacancies = vacancy_repo.get_all()
    return VacancyList(vacancies = [vacancy for vacancy in vacancies])

@app.get(
    "/vacancies/{vacancy_id}",
    status_code=status.HTTP_200_OK,
    description="Получение вакансии по идентификатору",
    response_model= Vacancy
)
def get_vacancy(vacancy_id: UUID, conn = Depends(get_conn)):
    vacancy_repo = VacancyRepo(conn)
    vacancy = vacancy_repo.get(str(vacancy_id))
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
    response_model= Vacancy
)
def create_vacancy(vacancy: VacancySchema, conn = Depends(get_conn)):
    vacancy_repo = VacancyRepo(conn)
    keycloak_id = uuid4()
    values = (
        str(keycloak_id),
        vacancy.name,
        vacancy.salary,
        vacancy.address,
        vacancy.description,
        vacancy.url
    )
    created_vacancy = vacancy_repo.create(values)
    if not created_vacancy:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Не удалось создать вакансию"
        )
    return created_vacancy

@app.put(
    "/vacancies/{vacancy_id}",
    status_code=status.HTTP_200_OK,
    description="Обновление данных по вакансии",
    response_model= Vacancy
)
def update_vacancy(vacancy_id: UUID,vacancy: VacancySchema, conn = Depends(get_conn)):
    vacancy_repo = VacancyRepo(conn)
    if not vacancy_repo.get(str(vacancy_id)):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
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
    status_code = status.HTTP_204_NO_CONTENT,
    description = "Удаление вакансии по идентификатору",
    response_model = None
)
def delete_vacancy(vacancy_id: UUID, conn = Depends(get_conn)):
    vacancy_repo = VacancyRepo(conn)
    if not vacancy_repo.get(str(vacancy_id)):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Пользователя с UUID: '{vacancy_id}' не существует"
        )
    vacancy = vacancy_repo.delete(str(vacancy_id))
    return vacancy

from fastapi import Query
from pydantic import BaseModel
from src.domain.vacancies import Vacancy


class VacancyList(BaseModel):
    vacancies: list[Vacancy] = Query(default_factory=list, description="Список вакансий")
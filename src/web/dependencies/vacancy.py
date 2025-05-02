from dataclasses import dataclass
from fastapi import Query
from pydantic import BaseModel
from domain.vacancy import Vacancy


class VacancyList(BaseModel):
    vacancies: list[Vacancy] = Query(default=list, description="Список вакансий")
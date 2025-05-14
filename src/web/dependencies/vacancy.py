from dataclasses import dataclass
from fastapi import Query
from src.domain.vacancies import Vacancy

@dataclass
class VacancyList:
    vacancies: list[Vacancy] = Query(default_factory=list, description="Список вакансий")
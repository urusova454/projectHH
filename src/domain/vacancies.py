from datetime import datetime
from typing import List, Optional, Any
from pydantic import BaseModel, HttpUrl, Field

class Area(BaseModel):
    id: str
    name: str
    url: HttpUrl

class Type(BaseModel):
    id: str
    name: str

class LogoUrls(BaseModel):
    logo_90: str = Field(..., alias="90")
    logo_240: str = Field(..., alias="240")
    original: str

class EmployerRating(BaseModel):
    total_rating: str
    reviews_count: int

class Employer(BaseModel):
    id: Optional[str] = None
    name: str
    url: Optional[HttpUrl] = None
    alternate_url: Optional[HttpUrl] = None
    logo_urls: Optional[LogoUrls] = None
    vacancies_url: Optional[HttpUrl] = None
    accredited_it_employer: bool
    employer_rating: Optional[EmployerRating] = None
    trusted: bool

class Snippet(BaseModel):
    requirement: Optional[str] = None
    responsibility: Optional[str] = None

class WorkingHours(BaseModel):
    id: str
    name: str

class WorkScheduleByDays(BaseModel):
    id: str
    name: str

class ProfessionalRole(BaseModel):
    id: str
    name: str

class Experience(BaseModel):
    id: str
    name: str

class Employment(BaseModel):
    id: str
    name: str

class EmploymentForm(BaseModel):
    id: str
    name: str

class BillingType(BaseModel):
    id: str
    name: str

class KeySkill(BaseModel):
    name: str

class LanguageLevel(BaseModel):
    id: str
    name: str

class Language(BaseModel):
    id: str
    name: str
    level: LanguageLevel

class Vacancy(BaseModel):
    id: str
    premium: bool
    billing_type: BillingType
    relations: List[Any]
    name: str
    insider_interview: Optional[Any] = None
    response_letter_required: bool
    area: Area
    salary: Optional[Any] = None
    salary_range: Optional[Any] = None
    type: Type
    address: Optional[Any] = None
    allow_messages: bool
    experience: Experience
    schedule: Type
    employment: Employment
    department: Optional[Any] = None
    show_contacts: bool
    contacts: Optional[Any] = None
    description: str
    branded_description: Optional[Any] = None
    vacancy_constructor_template: Optional[Any] = None
    key_skills: List[KeySkill]
    accept_handicapped: bool
    accept_kids: bool
    archived: bool
    response_url: Optional[Any] = None
    specializations: List[Any]
    professional_roles: List[ProfessionalRole]
    code: Optional[Any] = None
    hidden: bool
    quick_responses_allowed: bool
    driver_license_types: List[Any]
    accept_incomplete_resumes: bool
    employer: Employer
    published_at: datetime
    created_at: datetime
    initial_created_at: datetime
    negotiations_url: Optional[Any] = None
    suitable_resumes_url: Optional[Any] = None
    apply_alternate_url: HttpUrl
    has_test: bool
    test: Optional[Any] = None
    alternate_url: HttpUrl
    working_days: List[Any]
    working_time_intervals: List[Any]
    working_time_modes: List[Any]
    accept_temporary: bool
    languages: List[Language]
    approved: bool
    employment_form: EmploymentForm
    fly_in_fly_out_duration: List[Any]
    internship: bool
    night_shifts: bool
    work_format: List[Any]
    work_schedule_by_days: List[WorkScheduleByDays]
    working_hours: List[WorkingHours]
    show_logo_in_search: Optional[Any] = None


class GeneralVacancy(BaseModel):
    id: str
    premium: bool
    name: str
    department: Optional[Any] = None
    has_test: bool
    response_letter_required: bool
    area: Area
    salary: Optional[Any] = None
    salary_range: Optional[Any] = None
    type: Type
    address: Optional[Any] = None
    response_url: Optional[Any] = None
    sort_point_distance: Optional[Any] = None
    published_at: datetime
    created_at: datetime
    archived: bool
    apply_alternate_url: HttpUrl
    show_logo_in_search: Optional[Any] = None
    insider_interview: Optional[Any] = None
    url: HttpUrl
    alternate_url: HttpUrl
    relations: List[Any]
    employer: Employer
    snippet: Snippet
    show_contacts: bool
    contacts: Optional[Any] = None
    schedule: Type
    working_days: List[Any]
    working_time_intervals: List[Any]
    working_time_modes: List[Any]
    accept_temporary: bool
    fly_in_fly_out_duration: List[Any]
    work_format: List[Any]
    working_hours: List[WorkingHours]
    work_schedule_by_days: List[WorkScheduleByDays]
    night_shifts: bool
    professional_roles: List[ProfessionalRole]
    accept_incomplete_resumes: bool
    experience: Experience
    employment: Employment
    employment_form: EmploymentForm
    internship: bool
    adv_response_url: Optional[Any] = None
    is_adv_vacancy: bool
    adv_context: Optional[Any] = None
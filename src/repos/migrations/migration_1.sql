
CREATE TABLE IF NOT EXISTS vacancy(
    id_vacancy SERIAL PRIMARY KEY,
    name_vacancy VARCHAR(50) NOT NULL,
    salary INT,
    address VARCHAR(100),
    description TEXT NOT NULL,
    url VARCHAR(100)
);


INSERT INTO vacancy (name_vacancy, salary, address, description, url)
VALUES
    ('Frontend Developer (React)', 120000, 'Москва, ул. Тверская, 15', 'Ищем frontend-разработчика с опытом работы от 2 лет. Знание React, Redux, TypeScript. Удалённая работа возможна.', 'https://example.com/job/123'),
    ('Backend Developer (Python)', 150000, 'Санкт-Петербург, Невский пр., 45', 'Разработка высоконагруженных сервисов на Python (Django/FastAPI). Опыт с PostgreSQL, Docker.', 'https://example.com/job/456'),
    ('Менеджер по продажам', 80000, 'Екатеринбург, ул. Ленина, 10', 'Активные продажи IT-решений. Общение с клиентами, проведение презентаций. Опыт в B2B продажах от 1 года.', 'https://example.com/job/789'),
    ('Data Analyst', 110000, 'Новосибирск, ул. Советская, 33', 'Анализ больших данных, построение отчётов в Power BI/Tableau. Знание SQL, Python (Pandas, NumPy).', 'https://example.com/job/101'),
    ('UX/UI Designer', 95000, 'Казань, ул. Баумана, 7', 'Проектирование интерфейсов, создание прототипов в Figma. Опыт работы в команде разработки.', 'https://example.com/job/112'),
    ('Системный администратор', 90000, 'Москва, ул. Ленинградская, 25', 'Обслуживание корпоративной IT-инфраструктуры. Настройка серверов, сети, техподдержка сотрудников.', 'https://example.com/job/131'),
    ('Маркетолог', 75000, 'Краснодар, ул. Красная, 100', 'Разработка и проведение рекламных кампаний. Ведение соцсетей, контекстная реклама, аналитика.', 'https://example.com/job/141'),
    ('DevOps Engineer', 180000, 'Москва, ул. Пушкина, 5', 'Настройка CI/CD, работа с Kubernetes, AWS/GCP. Опыт с Terraform, Ansible.', 'https://example.com/job/151'),
    ('Тестировщик (QA Engineer)', 85000, 'Владивосток, ул. Светланская, 50', 'Ручное и автоматизированное тестирование веб-приложений. Знание Selenium, Postman.', 'https://example.com/job/161'),
    ('Копирайтер', 60000, 'Ростов-на-Дону, ул. Большая Садовая, 30', 'Написание продающих текстов, SEO-оптимизация. Опыт работы с интернет-магазинами.', 'https://example.com/job/171');

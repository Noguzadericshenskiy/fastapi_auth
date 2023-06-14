up: # запуск контейнера с БД в фоне
	docker compose -f docker-compose_db.yml up -d

up_build: # запуск контейнера с БД
	docker compose -f docker-compose_db.yml up --build

down: # остановка контейнера с БД
	docker compose -f docker-compose_db.yml down

down_net: # убить сетку контейнера
	docker compose -f docker-compose_db.yml down && docker network prune --force

al_init: #инициализация alembic и создание папки alembic
	alembic init alembic

al_rev: # создание ревизии возможно указать -m "описание"
	alembic	revision --autogenerate

al_upg: # апгрейд до последней ревизии
	alembic upgrade head

al_down: #откат назад к предыдущей ревизии
	alembic downgrade -1

app_start: # старт приложения
	uvicorn main:app --reload



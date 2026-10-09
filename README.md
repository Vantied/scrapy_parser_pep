# Асинхронный парсер PEP на Scrapy

Паук Scrapy собирает с peps.python.org номер, название и статус всех PEP и формирует два CSV-отчёта.

## Результаты

- `results/pep_<дата>.csv` — список всех PEP: номер, название, статус.
- `results/status_summary_<дата>.csv` — сводка: количество PEP в каждом статусе и общее число (Total).

## Технологии

Python 3.10+, Scrapy, pytest.

## Как запустить

```bash
git clone https://github.com/Vantied/scrapy_parser_pep.git
cd scrapy_parser_pep
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
scrapy crawl pep
```

## Что я вынес из проекта

- Архитектура Scrapy: пауки, Items, Pipelines, экспорт через FEEDS.
- Разница между синхронным парсингом на BeautifulSoup и асинхронным на Scrapy.

## Автор

Иван Богатов — [GitHub](https://github.com/Vantied) · Telegram [@Ivan_bogatov55](https://t.me/Ivan_bogatov55)

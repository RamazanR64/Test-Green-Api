# Green API AutoTests

Автоматизированные тесты для методов SendMessage и getChatHistory API Green API.

## Требования

- Python 3.8+
- pip (Python package manager)
- Chrome WebDriver (для Selenium тестов)

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/your-username/green-api-tests.git
cd green-api-tests
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Создайте файл `.env` в корневой директории проекта со следующими переменными:
```
GREEN_API_INSTANCE_ID=your_instance_id
GREEN_API_TOKEN=your_api_token
TEST_PHONE_NUMBER=79001234567
GREEN_API_EMAIL=your_email@example.com
GREEN_API_PASSWORD=your_password
```

## Структура проекта

```
green-api-tests/
├── tests/
│   ├── __init__.py
│   ├── test_api.py
│   └── test_web.py
├── test_results/
│   ├── screenshots/
│   └── reports/
├── requirements.txt
├── README.md
└── .env
```

## Запуск тестов

### Запуск всех тестов:
```bash
pytest -v
```

### Запуск только API тестов:
```bash
pytest -v -m api
```

### Запуск только Selenium тестов:
```bash
pytest -v -m selenium
```

### Генерация HTML-отчета:
```bash
pytest --html=test_results/report.html
```

## Результаты тестов

- Скриншоты сохраняются в директорию `test_results/screenshots/`
- HTML-отчеты сохраняются в директорию `test_results/reports/`

## Маркеры тестов

- `@pytest.mark.api` - тесты API методов
- `@pytest.mark.selenium` - тесты веб-интерфейса

#

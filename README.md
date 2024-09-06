# OTUS_selenium_UI

## Структура проекта

```bash
OTUS_selenium_UI/
│
├── page_objects/           # Реализация Page Object для каждой страницы
│
├── tests/                  # Каталог с тестами
│   └── test_start.py       # Тесты
│
├── progs/                  # Вспомогательные программы
│   ├── allure-2.13.9.tgz   # Архив для первичной установки Allure
│   └── cm_linux_amd64      # Бинарный файл для запуска Selenoid
│
├── requirements.txt        # Список пакетов, необходимых для работы проекта
├── docker-compose.yml      # Конфигурация Docker Compose для запуска OpenCart, БД и админки
├── conftest.py             # Конфигурационный файл для тестов
├── pytest.ini              # Конфигурационный файл для настроек запуска тестов
└── README.md               # Описание проекта и инструкции по запуску
```

## Команды для запуска
### Запуск Selenoid:
```bash
./cm_linux_amd64 selenoid start
```

### Запуск Selenoid UI:
```bash
docker run -d --name selenoid-ui --network selenoid -p 8090:8080 aerokube/selenoid-ui:1.10.11 --selenoid-uri http://selenoid:4444
```

### Запуск OpenCart, БД и админки:
```bash
OPENCART_PORT=8081 PHPADMIN_PORT=8888 LOCAL_IP=$(hostname -I | grep -o "^[0-9.]*") docker compose up
```
### Запуск Jenkins:
```bash
docker run -p 8080:8080 -p 50000:50000 --restart=on-failure -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts-jdk21
```

## Jenkins
В Jenkins настроена джоба Selenium_tests_opencart. Джоба запускается с параметрами:

- Адрес executor (Selenoid)
- Адрес приложения (OpenCart)
- Браузер
- Версия браузера
- Количество потоков

## Отчетность
Отчетность собирается с помощью Allure, по окночанию работы джобы. В отчеты прикрепляются скриншоты при падении тестов.


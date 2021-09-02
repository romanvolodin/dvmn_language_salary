# Прикидываем будущую зарплату

Скрипт скачивает вакансии с сайтов HeadHunter и SuperJob, и считает среднюю зарплату для каждого языка программирования.


## Требования

Для запуска вам понадобится Python 3.6 или выше.

Необходимо получить ключи для доступа к API:
- HeadHunter
- SuperJob


## Переменные окружения

Настройки проекта берутся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `main.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступные переменные:

- `HEADHUNTER_API_KEY` — ключ для доступа к API HeadHunter. 
- `SUPERJOB_API_KEY` — ключ для доступа к API SuperJob. 

Пример:

```env
HEADHUNTER_API_KEY=2496bf54e82920wr3478f1ce7b58221d8d6
SUPERJOB_API_KEY=2496bf54e82920wr3478f1ce7b58221d8d6
```

## Запуск

Скачайте код с GitHub. Установите зависимости:

```sh
pip install -r requirements.txt
```

Запустите скрипт:

```sh
python main.py
```

Примеры вывода:
```sh

```

## Цели проекта

Код написан в учебных целях — для курса по Python на сайте [Devman](https://dvmn.org).
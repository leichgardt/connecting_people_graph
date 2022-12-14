# Connecting people graph
Приложение социальных связей.
Реализовано с помощью структуры неориентированного связного графа. 
Граф представлен в виде матрицы смежности.

![Матрица смежности](https://evileg.com/media/users/mafulechka/photos/photo_rgj2unT.jpg)

# Требования
* python 3.10+

# Установка
Создайте виртуальную среду и установите зависимости
```shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

# Запуск
Для запуска выполните команду в терминале 
```shell
uvicorn main:app
```

# Использование
По ссылке http://127.0.0.1:8000/docs вы сможете протестировать приложение.

Для создания новых коммуникаций в графе отправьте POST-запрос с журналом коммуникаций в виде JSON по адресу 
`/new_communication_journal`:
```json
{
  "communications": [
    {
      "person_1_id": 1,
      "person_2_id": 2
    },{
      "person_1_id": 2,
      "person_2_id": 3
    },{
      "person_1_id": 1,
      "person_2_id": 3
    }
  ]
}
```

Для получения графа выполните GET-запрос по адресу `/graph`. В ответ вы получите JSON с матрицей смежности, 
статистикой по связям пользователей и URL на сгенерированное изображение графа.

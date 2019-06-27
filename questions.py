QUIZ_QUESTIONS = [
    {
        "question": "Сколько байт в 1 Кбайте?",
        "answers": [
            {"text": "1000 байт", "value": 0},
            {"text": "1024 байт", "value": 1},
            {"text": "8 байт", "value": 0},
            {"text": "8000 байт", "value": 0},
        ]
    },

    {
        "question": "Что из ниже перечисленного не является языком программирования?",
        "answers": [
            {"text": "PHP", "value": 0},
            {"text": "C#", "value": 0},
            {"text": "JavaScript", "value": 0},
            {"text": "HTML", "value": 1},
        ]

    },

    {
        "question": "Что значит ошибка сервера, обозначаемая кодом 500?",
        "answers": [
            {"text": "Not Found", "value": 0},
            {"text": "Internal Server Error", "value": 1},
            {"text": "FatalError", "value": 0},
            {"text": "Bad Gateway", "value": 0},
        ]

    },

    {
        "question": "Укажите компилируемый язык программирования:",
        "answers": [
            {"text": "Java", "value": 1},
            {"text": "JavaScript", "value": 0},
            {"text": "PHP", "value": 0},
            {"text": "Ruby", "value": 0},
        ]

    },

    {
        "question": "Переведите число 88, представленное в десятеричной системе счисления, в восьмеричную систему.",
        "answers": [
            {"text": "11", "value": 0},
            {"text": "202", "value": 0},
            {"text": "130", "value": 1},
            {"text": "110", "value": 0},
        ]

    },

    {
        "question": "Определите язык программирования по фрагменту кода:\n"
                        "package com.example;\n"
                        "class Car {\n"
                        "String color = 'black'; //instance variable \n"
                        "void accelerate() { \n"
                        " int speed = 90; //local variable }}",
        "answers": [
            {"text": "Java", "value": 1},
            {"text": "1C", "value": 0},
            {"text": "XML", "value": 0},
            {"text": "Фрагмент слишком мал, чтобы что-то определить", "value": 0},
        ]

    },

    {
        "question": "Сколько операционных систем в смартфоне?",
        "answers": [
            {"text": "1 ОС", "value": 0},
            {"text": "3 ОС", "value": 0},
            {"text": "4 ОС", "value": 0},
            {"text": "2 ОС", "value": 1},
        ]

    },

    {
        "question": "Какого языка программирования не существует?",
        "answers": [
            {"text": "A", "value": 1},
            {"text": "B", "value": 0},
            {"text": "C", "value": 0},
            {"text": "D", "value": 0},
        ]

    },

    {
        "question": "Сколько байт в 1 пикселе?",
        "answers": [
            {"text": "3 байта", "value": 0},
            {"text": "16 байт", "value": 0},
            {"text": "Невозможно перевести пиксели в байты.", "value": 1},
            {"text": "1024 байта", "value": 0},
        ]

    },

    {
        "question": "Решите логическую задачу.\n"
                    "Вадим, Сергей и Михаил изучают различные иностранные языки: китайский японский и арабский. На вопрос, какой язык изучает каждый из них, один ответил: «Вадим изучает китайский, Сергей не изучает китайский, а Михаил не изучает арабский». Впоследствии выяснилось, что в этом ответе только одно утверждение верно, а два других ложны.",

        "answers": [
            {"text": "Вадим изучает китайский, Сергей – арабский, Михаил – японский.", "value": 0},
            {"text": "Сергей изучает китайский язык, Михаил – японский, Вадим – арабский", "value": 1},
            {"text": "Михаил изучает китайский, Вадим – японский, Сергей – арабский.", "value": 0},
        ]

    },
]

"""
PROF_QUESTIONS = {
        {
            "question": "Сколько байт в 1 Кбайте?",
            "answers": ["1 - 1000 байт", "2 - 1024 байт(правильный)", "3 - 8 байт", "4 - 8000 байт"]
        },
        {
            "question": "Что из ниже перечисленного не является языком программирования?",
            "answers": ["1 - PHP", "2 - C#", "3 - JavaScript", "4 - HTML(правильный)"]
        },
        {
            "question": "Укажите компилируемый язык программирования:",
            "answers": ["1 - Java(правильный)", "2 - JavaScript", "3 - PHP", "4 - Ruby"]
        },
        {
            "question": "Что значит ошибка сервера, обозначаемая кодом 500?",
            "answers": ["1 - Not Found", "2 - Bad Gateway", "3 - Internal Server Error(правильный)", "4 - FatalError"]
        },
        {
            "question": "Переведите число 88, представленное в десятеричной системе счисления, в восьмеричную систему.",
            "answers": ["1 - 11", "2 - 130(правильный)", "3 - 202", "4 - 110"]
        },
        {
            "question": "Какого языка программирования не существует?",
            "answers": ["1 - A(правильный)", "2 - B", "3 - С", "4 - D"]
        },
        {
            "question": "Определите язык программирования по фрагменту кода:\n"
                        "package com.example;\n"
                        "class Car {\n"
                        "String color = 'black'; //instance variable \n"
                        "void accelerate() { \n"
                        " int speed = 90; //local variable }}",
            "answers": ["1 - XML", "2 - Java(правильный)", "3 - 1C", "4 - Фрагмент слишком мал, чтобы что-то определить"]
        },
        {
             "question": "Сколько байт в 1 пикселе?",
             "answers": ["1 - 3", "2 - 16", "3 - Невозможно перевести пиксели в байты.(правильный)", "4 - 1024"]
        },
        {
             "question": "Как расшифровывается HTML тег '<br>'",
             "answers": ["1 - bitrate (скорость передачи битов)", "2 - breakrow (перенос строки)(правильный)", "3 - brown (коричневый)", "4 - такого тега в HTML нет"]
        },
        {
             "question": "Сколько операционных систем в смартфоне?",
             "answers": ["1 - 1 ОС", "2 - 2 ОС(правильный)", "3 - 3 ОС", "4 - 4 ОС"]
        }
}
"""
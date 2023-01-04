import requests
import json

available_endpoints = {
    'Nivel 1': {
        'Lección 1': 'https://besvc.capacitateparaelempleo.org/api/Tests/es/435cb895-ded7-4965-8798-9740c3ac589a/View',
        'Lección 2': 'https://besvc.capacitateparaelempleo.org/api/Tests/es/c9cbafb5-96d9-4254-87ea-7017a37ec8c7/View'
    },
    'Nivel 2': {
        'Lección 1': 'https://besvc.capacitateparaelempleo.org/api/Tests/es/f8d30a8c-3f00-4475-ac5b-ba9d793eb081/View',
        'Lección 2': 'https://besvc.capacitateparaelempleo.org/api/Tests/es/0f982feb-2952-4bfb-ba60-09ad014b10ea/View',
        'Lección 3': 'https://besvc.capacitateparaelempleo.org/api/Tests/es/a0511bcb-678d-4e1e-bab9-9013fbfddfeb/View'
    },
    'Nivel 3': {
        'Lección 1': 'https://besvc.capacitateparaelempleo.org/api/Tests/es/a0511bcb-678d-4e1e-bab9-9013fbfddfeb/View'
    },
    'Nivel 4': {
        'Lección 1': 'https://besvc.capacitateparaelempleo.org/api/Tests/es/be8db28e-7519-41c5-b985-74c9f15b19c5/View'
    }
}


def getQuestions(endpoint):
    response = requests.get(endpoint)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        print(f'Error al obtener las preguntas {response.status_code}')
        input("\nPresione Enter...")
        exit()


def menu():
    levels = list(available_endpoints.keys())
    while True:
        lessons = list()
        for i, nivel in enumerate(available_endpoints):
            print(f'{i + 1} - {nivel}')
            lessons.append(list(available_endpoints[nivel].keys()))
        try:
            nivel = int(input('Selecciona el nivel: '))-1
            if nivel < 0 or nivel > len(levels):
                print('Opción no válida')
                input("\nPresione Enter...")
                continue
            print(f'\n\nHas seleccionado el nivel {levels[nivel]}\n\n')
        except KeyboardInterrupt:
            print('Saliendo...')
            input("\nPresione Enter...")
            exit()
        except:
            print('Opción no válida')
            input("\nPresione Enter...")
            continue
        break
    while True:
        for i, leccion in enumerate(lessons[nivel]):
            print(f'{i + 1} - {leccion}')
        try:
            leccion = int(input('Selecciona la lección: '))-1
            if leccion < 0 or leccion > len(lessons[nivel]):
                print('Opción no válida')
                continue
            print(
                f'\n\nHas seleccionado la lección {lessons[nivel][leccion]}\n\n')
        except:
            print('Opción no válida')
            continue
        break
    return available_endpoints[levels[nivel]][lessons[nivel][leccion]]


def questionParser(question):
    pregunta = question['questionText']
    respuesta = ""
    if (question['questionTypeId'] == 1):  # Unica respuesta
        respuesta = f"-> {question['answerOptions'][0]['answerText']}"
    elif (question['questionTypeId'] == 2):  # Multiple respuesta
        for answer in question['answerOptions']:
            respuesta += f"-> {answer['answerText']}\n"
    elif (question['questionTypeId'] == 3):  # Ordenar
        for i, answer in enumerate(question['answerOptions']):
            respuesta += f"{i+1}.- {answer['answerText']}\n"
    else:
        respuesta = 'Tipo de pregunta desconocida'
    return f"{pregunta}\n{respuesta}\n"


def main():
    print("Bienvenido a las respuestas de Capacitate para el Empleo")
    print("Selecciona el nivel y la lección que deseas obtener las respuestas")
    endpoint = menu()
    questions = getQuestions(endpoint)
    print(f'{"*"*5}Respuestas de {questions["name"]}{"*"*5}\n')
    for question in questions['questions']:
        print(questionParser(question))


main()
input("\nPresione Enter para salir...")

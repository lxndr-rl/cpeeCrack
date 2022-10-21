import requests
import json

available_endpoints = {
    'Nivel 1': {
        'Lección 1': 'https://besvc.capacitateparaelempleo.org/api/Tests/es/3e451f9e-0799-45a2-aba2-6900a079ea16/View',
        'Lección 2': 'https://besvc.capacitateparaelempleo.org/api/Tests/es/bfe7bb44-3891-4156-9d53-4898311a31fd/View'
    },
    'Nivel 2': {
        'Lección 1': 'https://besvc.capacitateparaelempleo.org/api/Tests/es/b885b619-69b4-4006-be25-cdb753331e0d/View',
        'Lección 2': 'https://besvc.capacitateparaelempleo.org/api/Tests/es/f7151aa7-34d8-4fa4-98ca-9cbbb7bc26bf/View'
    },
    'Nivel 3': {
        'Lección 1': 'https://besvc.capacitateparaelempleo.org/api/Tests/es/076a25e5-5b44-4b7a-b3e2-9ec79ce49c09/View'
    },
    'Nivel 4': {
        'Lección 1': 'https://besvc.capacitateparaelempleo.org/api/Tests/es/f97b35ae-635b-4748-9530-a8e97b5d28a9/View'
    }
}


def getQuestions(endpoint):
    response = requests.get(endpoint)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        print(f'Error al obtener las preguntas {response.status_code}')
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
                continue
            print(f'\n\nHas seleccionado el nivel {levels[nivel]}\n\n')
        except KeyboardInterrupt:
            print('Saliendo...')
            exit()
        except:
            print('Opción no válida')
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
        respuesta = f"1.- {question['answerOptions'][0]['answerText']}\n2.- {question['answerOptions'][1]['answerText']}"
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

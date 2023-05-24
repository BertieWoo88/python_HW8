'''
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной

Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения 
и удаления данных



'''

import os

filename = 'text.txt'
fields = ["Фамилия", "Имя", "Телефон", "Описание"]


def saveData(filename, data): # Функция сохранения данных в файл
    with open(filename, 'w', encoding='utf-8') as fout:

        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')
    print('данные обновлены')        

def readData(filename: str):  # Функция выгрузки данных из файл
    data = []
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data


def getNewPerson(): # Функция добавления человека в базу
    phoneDirectory= readData(filename)    
    newRecord = dict()
    for i in range(len(fields)):
        newRecord[fields[i]]=(input(f'введите данные по полю "{fields[i]}": ')) 
    phoneDirectory.append(newRecord)
    saveData(filename, phoneDirectory) 


def searchData(searchedData, fieldNum): # Функция поиска по определенному полю
    phoneDirectory= readData(filename)
    tick = 0
    find = False
    printIndent()
    print('Результаты поиска: ')
    for line in phoneDirectory:
        tick+=1
        if searchedData.lower() in line[fields[fieldNum]].lower():
            find = True
            print(f'{tick}', end=" ")
            print(*line.values()) 

    if  find == False: print(f'{searchedData} не найдена среди данных поля {fields[fieldNum]}')       
    os.system('pause')

def askSearch(): # Меню поиска данных
    while True:
        printIndent()
        print('Меню поиска')
        for i in range(len(fields)):
            print(f'{i} - поиск по полю {fields[i]}')    
        print(f'{len(fields)} - выход в главное меню')
        answer = int(input('Введите номер меню: '))              
        if answer == len(fields): break
        if 0 <= answer <len(fields):
            searched =input('введите искомое значение:')
            searchData(searched, answer)

def printAllData(): # Функция вывода всех данных
    phoneDirectory= readData(filename)
    tick=0
    printIndent()
    print('Данные справочника:')
    for line in phoneDirectory:
        tick+=1
        print(f'{tick}', end=" ")
        print(*line.values())
    os.system('pause')

def printIndent(): # Функция вывода отступа для лучшей читаемости данных с консоли
    print()
    for i in range(20):
        print('_', end='')
    print()    


def remRecord(): # Функция удаления записи по введенному индексу
    printAllData()
    RecIndex = int(input('введите номер записи которую следует удалить: '))-1
    phoneDirectory= readData(filename)
    phoneDirectory.pop(RecIndex)
    saveData(filename, phoneDirectory)
    os.system('pause') 

def changeRecord(): # меню изменения записи
    printAllData()
    recIndex = int(input('введите номер записи которую следует редактировать: '))-1
    print(*enumerate(fields))
    fieldsIndex = int(input('введите номер поля для редактирования: '))
    phoneDirectory= readData(filename)
    phoneDirectory[recIndex][fields[fieldsIndex]] = input('введите новые данные: ')
    saveData(filename, phoneDirectory)
    os.system('pause')  

def AskAction(): # Функция вывода главного меню
    while True:
        printIndent()
        print('Главное меню. \n'
              '0 - ввести новую запись \n'
              '1 - войти в меню поиска \n'
              '2 - вывести все данные \n'
              '3 - удалить запись из справочника \n'
              '4 - редактировать запись из справочника \n'
              '5 - выйти из программы \n'
              'Что вы хотите сделать?:', end=' ')
        answer = int(input())

        if answer == 5:
            return
        elif answer == 0:
            getNewPerson()
        elif answer == 2:
            printAllData()    
        elif answer == 1:
            askSearch()
        elif answer == 3:
            remRecord()
        elif answer == 4:
            changeRecord()       

AskAction()
    





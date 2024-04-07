from flask import Flask
from flask import render_template, request
from processing import predict
from preprocessing import data_preparation

app = Flask(__name__)

@app.route('/')
def main():
        return render_template('index.html')

@app.route('/ml', methods = ['get','post'])
def ml():
        my_message = ''
        my_message1 = ''
        my_result = ''
        error = False
        if request.method == 'POST':
                names = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10', 'x11']
                my_list1 = [request.form.get(name) for name in names]
                my_list = []
                #x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11
                for name in names:
                        try:
                                my_list.append(float(request.form.get(name)))
                        except:
                                error = True
                                break
                if my_list[10] not in (0, 90):
                        error = True
                if error == False:
                        x = data_preparation(my_list)
                        y1, y2 = predict(x)
                        print(y1, y2)
                        my_message1 = f'''РЕЗУЛЬТАТ: 
                                        Модуль упругости при растяжении, ГПа:/n = {str(float(y1))}, 
                                        Прочность при растяжении, МПа:/n = {str(float(y2))}'''
                        my_message = f'''ВЫ ВВЕЛИ: Угол нашивки(град) = {my_list[0]}, Шаг нашивки = {my_list[1]}, Плотность нашивки = {my_list[2]}, 
                                        Соотношение матрица-наполнитель = {my_list[3]}, Плотность (кг/м3) = {my_list[4]}, 
                                        Модуль упругости (ГПа) = {my_list[5]}, Количество отвердителя (м.%) = {my_list[6]}, 
                                        Содержание эпоксидных групп (%_2) = {my_list[7]}, Температура вспышки (С_2) = {my_list[8]}, 
                                       'Поверхностная плотность (г/м2) = {my_list[9]}, Потребление смолы, г/м2 = {my_list[10]}'''
                else:
                        my_message1 = 'ОШИБКА. Следует вводить вещественные числа, отделяя дробную часть точкой.'
                        my_message = f'''ВЫ ОШИБОЧНО ВВЕЛИ: Угол нашивки(град) = '{my_list1[0]}', Шаг нашивки = '{my_list1[1]}', Плотность нашивки = '{my_list1[2]}', 
                                        Соотношение матрица-наполнитель = '{my_list1[3]}', Плотность (кг/м3) = '{my_list1[4]}', 
                                        Модуль упругости (ГПа) = '{my_list1[5]}', Количество отвердителя (м.%) = '{my_list1[6]}', 
                                        Содержание эпоксидных групп (%_2) = '{my_list1[7]}', Температура вспышки (С_2) = '{my_list1[8]}', 
                                       'Поверхностная плотность (г/м2) = '{my_list1[9]}', Потребление смолы, г/м2 = '{my_list1[10]}' '''
        return render_template(template_name_or_list='ml.html', p_message = my_message, p_message1 = my_message1)

#app.run() #Используется только при локальном запуске
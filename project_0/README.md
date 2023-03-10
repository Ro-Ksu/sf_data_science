# Проект 0. Угадай число

## Оглавление
[1. Описание проекта](https://github.com/Ro-Ksu/sf_data_science/tree/main/project_0/README.md#Описание-проекта)  
[2. Какой кейс решаем?](https://github.com/Ro-Ksu/sf_data_science/tree/main/project_0/README.md#Какой-кейс-решаем)  
[3. Используемый алгоритм решения](https://github.com/Ro-Ksu/sf_data_science/tree/main/project_0/README.md#Используемый-алгоритм-решения)  
[4. Результат](https://github.com/Ro-Ksu/sf_data_science/tree/main/project_0/README.md#Результат)  
[5. Выводы](https://github.com/Ro-Ksu/sf_data_science/tree/main/project_0/README.md#Выводы)
<!---[3. Краткая информация о данных](https://github.com/Ro-Ksu/sf_data_science/tree/main/project_0/README.md#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](https://github.com/Ro-Ksu/sf_data_science/tree/main/project_0/README.md#Этапы-работы-над-проетком) --->


### **Описание проекта**
Угадать загаданное компьютером число за минимальное число попыток.

:arrow_up: [к оглавлению](https://github.com/Ro-Ksu/sf_data_science/tree/main/project_0/README.md#Оглавение)


### **Какой кейс решаем?**
Нужно написать программу, которая угадывает число за минимальное число попыток

**Условия соревнования:**
- Компьютер загадывает целое число от 1 до 100, и нам его нужно угадать. Под "угадать", подразумевается "написать программу, которая угадывает число".
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.
- Необходимо добиться того, чтобы программа угадывала число меньше, чем за 20 попыток.

**Метрики качества**  
Результаты оцениваются по среднему количеству попыток при 1000 повторений. Необходимо добиться минимального количества попыток.

**Что практикуем**  
- Учимся писать хороший код на *Python*
- Учимся работать с *IDE*
- Учимся работать с *GitHub*


<!---### Краткая информация о данных
....

:arrow_up: [к оглавлению](https://github.com/Ro-Ksu/sf_data_science/tree/main/project_0/README.md#Оглавение)

### Этапы работы над проектом
....

:arrow_up: [к оглавлению](https://github.com/Ro-Ksu/sf_data_science/tree/main/project_0/README.md#Оглавение) --->


### **Используемый алгоритм решения**
**Бинарный поиск числа**  
Алгоритм, при котором каждый раз выбирается число из середины диапазона и исключается половина оставшихся чисел.  
:mag: Ссылка на подробное описание алгоритма на сайте [SkillFactory](https://blog.skillfactory.ru/glossary/binarnyj-poisk/)  

:arrow_up: [к оглавлению](https://github.com/Ro-Ksu/sf_data_science/tree/main/project_0/README.md#Оглавение)


### **Результат**
Получившийся алгоритм в среднем угадывает число за 5 попыток.

:arrow_up: [к оглавлению](https://github.com/Ro-Ksu/sf_data_science/tree/main/project_0/README.md#Оглавение)  


### **Выводы**  
Алгоритм решения подобран верно, вероятно, не совсем корректно отработаны границы диапазона.

:arrow_up: [к оглавлению](https://github.com/Ro-Ksu/sf_data_science/tree/main/project_0/README.md#Оглавение)
# Выполнила: Донченко М.А. ИУ5Ц-73Б
from operator import itemgetter

class Group():
    def __init__(self, id, name, count_people, course_id):
        self.id = id
        self.name = name
        self.count_people = count_people
        self.course_id = course_id

class Course():
    def __init__(self, id, name):
        self.id = id
        self.name = name

class GroupCourse():
    def __init__(self, group_id, course_id):
        self.group_id = group_id
        self.course_id = course_id

Courses = [
    Course(1, 'Математический анализ'),
    Course(2, 'Аналитическая геометрия'),
    Course(3, 'Инженерная графика'),
    Course(4, 'Начертательная геометрия'),
    Course(5, 'Программирование Python'),
]

Groups = [  
    Group(1, 'ИУ5-11', 25, 1),
    Group(2, 'ИУ5-12', 27, 2),
    Group(3, 'ИУ5-13', 23, 1),
    Group(4, 'ИУ5-14', 30, 4),
    Group(5, 'ИУ5-15', 22, 1),

    Group(6, 'ИУ6-11', 25, 5),
    Group(7, 'ИУ6-12', 27, 1),
    Group(8, 'ИУ6-13', 23, 4),
    Group(9, 'ИУ6-14', 30, 5),
    Group(10, 'ИУ6-15', 22, 1),

    Group(11, 'ИУ7-11', 23, 3),
    Group(12, 'ИУ7-12', 24, 1),
    Group(13, 'ИУ7-13', 30, 2),
    Group(14, 'ИУ7-14', 30, 1),
    Group(15, 'ИУ7-15', 22, 3),

    Group(16, 'ИУ7-11', 23, 3),
    Group(17, 'ИУ7-12', 24, 2),
    Group(18, 'ИУ7-13', 30, 5),
    Group(19, 'ИУ7-14', 30, 1),
    Group(20, 'АК7-15', 22, 1),
    
    Group(21, 'РК5-11', 25, 2),
    Group(22, 'АК5-12', 27, 4),
    Group(23, 'РК5-13', 23, 2),
    Group(24, 'РК5-14', 30, 1),
    Group(25, 'РК5-15', 22, 3),

    Group(26, 'РК6-11', 25, 1),
    Group(27, 'РК6-12', 27, 2),
    Group(28, 'РК6-13', 23, 5),
    Group(29, 'РК6-14', 30, 2),
    Group(30, 'РК6-15', 19, 3),
]

Group_Courses = [
    GroupCourse(1,1),
    GroupCourse(2,1),
    GroupCourse(3,1),
    GroupCourse(4,1),
    GroupCourse(5,1),

    GroupCourse(1,2),
    GroupCourse(2,2),
    GroupCourse(3,2),
    GroupCourse(4,2),
    GroupCourse(5,2),
]

def main():
    # Соединение данных один-ко-многим 
    one_to_many = [(e.name, e.count_people, d.name) 
        for d in Courses 
        for e in Groups 
        if e.course_id == d.id]
    
    # Соединение данных многие-ко-многим
    many_to_many_tPrep = [(d.name, ed.course_id, ed.group_id) 
        for d in Courses 
        for ed in Group_Courses 
        if d.id == ed.course_id]
    
    many_to_many = [(e.name, e.count_people, Course_name) 
        for Course_name, course_id, group_id in many_to_many_tPrep
        for e in Groups if e.id == group_id]
    
    print('РК1 Выполнила Донченко М.А. ИУ5Ц-73Б')
    print()
    print('Задание B1')
    res_b1 = []
    for i in one_to_many:
        if i[0][0] == "А":
            res_b1.append((i[0], i[2]))
    print(res_b1)

    print()
    print('Задание B2')
    res_b2_unsorted = []
    for d in Courses:
        d_Group = list(filter(lambda i: i[2]==d.name, one_to_many))       
        if len(d_Group) > 0:
            d_sals = [sal for _,sal,_ in d_Group]
            d_sals_min = min(d_sals)
            res_b2_unsorted.append((d.name, d_sals_min))

    res_b2 = sorted(res_b2_unsorted, key=itemgetter(1))
    print(res_b2)
    
    print()
    print('Задание B3')
    res_b3 = []
    for i in one_to_many:
            res_b3.append((i[0], i[2]))
    res_b3_sorted = sorted(res_b3, key=itemgetter(0))
    print(res_b3_sorted)
    
    
if __name__ == '__main__':
    main()
course=['mca','mba',30,40]
course.append('pgdca')
print(course)
course.extend(('mca','mba','4a','4b'))
print(course)
print(course.index('mba'))
print(course.count('mba'))
print(course)
print(course.pop())
print(course)
course.remove('4a')
print(course)

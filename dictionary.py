people = []

for _ in range(3):
  name = input('Enter your name: ')
  age = input('Enter your age: ')
  favorite_color = input('Enter your favorite color: ')
  
  person = {
    'name':name,
    'age': age,
    'favorite color': favorite_color
    }
  people.append(person)
  
for number in range(len(people)):
  person = people[number]
  favorite_color = person['favorite color']
  if favorite_color == 'blue':
    print(person['name'])
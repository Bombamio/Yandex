with open('work_test.txt', 'r', encoding='utf-8') as file:
    numbers = file.read()
result = [int(num) for num in numbers.split()]
with open('work_test.txt', 'w', encoding='utf-8') as file:
    file.write(str(sum(result)))
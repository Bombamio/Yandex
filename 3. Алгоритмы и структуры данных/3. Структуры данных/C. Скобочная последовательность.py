class Stack:

    def __init__(self):
        # Для хранения элементов в списке используем приватный атрибут. 
        # На его приватность указывают два подчёркивания в имени.
        self.__items = []

    def push(self, item):
        """Добавить элемент в стек."""
        self.__items.append(item)

    def pop(self):
        """Взять элемент из стека."""
        return self.__items.pop()

    def peek(self):
        """Посмотреть последний элемент без изъятия."""
        return self.__items[-1]

    def size(self):
        """Вернуть размер стека."""
        return len(self.__items)


def is_correct_bracket_seq(brackets):
    len_brackets = len(brackets)
    if len_brackets == 0:
        return True

    brackets_stack = Stack()
    for i in brackets:
        if i in ('(', '[', '{'):
            brackets_stack.push(i)
        elif i in (')', ']', '}') and brackets_stack.size() == 0:
            return False
        elif i in (')', ']', '}'):
            if i == ')' and brackets_stack.peek() == '(':
                brackets_stack.pop()
            elif i == ']' and brackets_stack.peek() == '[':
                brackets_stack.pop()
            elif i == '}' and brackets_stack.peek() == '{':
                brackets_stack.pop()
            else:
                return False
    return False if brackets_stack.size() != 0 else True


if __name__ == '__main__':
    """Главная фукция."""
    with open('input.txt', 'r') as file_in:
        a = str(file_in.readline())

    with open('output.txt', 'w') as file_out:
        file_out.write(str(is_correct_bracket_seq(a)))
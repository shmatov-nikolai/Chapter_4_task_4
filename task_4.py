"""
4)ContactList
Создайте класс ContactList, который должен наследоваться от
встроенного класса list. В нем должен быть реализован метод
search_by_name, который должен принимать имя, и возвращать список
всех совпадений. Замените all_contacts = [ ] на all_contacts =
ContactList(). Создайте несколько контактов, используйте метод
search_by_name.
"""
class List:
    def __init__(self):
        self.all_contacts = []

    def search_by_name(self, *args):
        for name in args:
            self.all_contacts.append(name)
        args = list(set(args))
        print(args)
        print(self.all_contacts)
        for i in args:
            if i in self.all_contacts:
                if self.all_contacts.count(i)>1:
                    print(f"совпадения: {i}")

class ContactList(List):

    def __init__(self):
       super(ContactList,self).__init__()

listok = ContactList()
listok.search_by_name('Bob', 'marli', 'Bob', 'Kenny', 'Tom', 'Tom')




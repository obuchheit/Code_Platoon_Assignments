class ContactList:
    

    def __init__(self, name, contacts):
        self.set_name = name
        self.set_contacts = contacts

        self.get_contacts = self.set_contacts
        self.get_name = self.set_name



    def add_contact(self, contact):
        self.set_contacts.append(contact)

    def find_shared_contacts():
        pass

    def remove_contact(self, name):
        for obj in self.set_contacts:
            if name in obj.values():
                self.set_contacts.remove(obj)



my_list = ContactList('My List', [])
my_list.set_name = 'New Name'
print(my_list.get_name)


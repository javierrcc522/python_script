from  contact import Contact

name = str(input('Enter your name: '))
number = str(input('Enter your phone number '))
address = str(input('Enter your address '))
note =  str(input('Enter a note '))

all_contacts = [Contact('Javier', '541-490-1234','portland', 'he likes sc2')]

def add_contact(name, number, address, note):
    new_contact = Contact(name, number, address, note)
    all_contacts.append(new_contact)

def find_contact(name, all_contacts):
    contact_found = False
    for contact_info in all_contacts:
        if contact_info.name == name:
            print(contact_info.name, contact_info.number, contact_info.address, contact_info.note)
            contact_found = True
    if contact_found == False:
        print('no one found')


def main():
    add_contact(name, number, address, note)
    search_name = str(input('find someone '))
    find_contact(search_name, all_contacts)


if __name__ == '__main__':
    main()
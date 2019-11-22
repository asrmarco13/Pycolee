def who_do_you_know():
    people_list = []
    people_knows = input('Insert people names separated by comma (eg. ","): ')
    for person in (people_knows.split(',')):
        people_list.append(person.strip())

    return people_list


def ask_user(people_list):
    person = input('Insert person name: ')
    if person in people_list:
        print('{} is present in the list'.format(person))
    else:
        print('{} isn\'t present in the list'.format(person))


people_list = who_do_you_know()
ask_user(people_list)

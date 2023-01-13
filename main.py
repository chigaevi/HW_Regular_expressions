import csv
import re


def distrib_name():
    i = 0
    for worker in contacts_list:
      if worker[1] == '' and worker[2] == '':
          name_worker = worker[0].split()
          for ind in range(len(name_worker)):
              contacts_list[i][ind] = name_worker[ind]
          i += 1
      elif worker[1] != '' and worker[2] == '':
          name_worker = [worker[0]]
          name_worker.extend(worker[1].split())
          for ind in range(len(name_worker)):
              contacts_list[i][ind] = name_worker[ind]
          i += 1
      else:
          i += 1
    return contacts_list


def edit_phone_number():
    i = 0
    for worker in contacts_list:
        phone_number = worker[5]
        pattern = r'(\+7|^8)\s*\(*(\d{3})\)*\s*\-*(\d{3})\s*\-*(\d{2})\s*\-*(\d{2})\s*\(*(доб.)*\s*(\d{4})*\)*'
        rep = r'+7(\2)\3-\4-\5 \6\7'
        new_number = re.sub(pattern,rep,phone_number)
        contacts_list[i][5] = new_number
        i += 1
    return contacts_list

def join_records():
    i = 0
    for worker in contacts_list:
        lastname = worker[0]
        for ind in range(i, len(contacts_list)):
             if lastname == contacts_list[ind][0]:
                for ind2 in range(len(contacts_list[0])):
                    if contacts_list[ind][ind2] == '' or worker[ind2] == '':
                        contacts_list[i][ind2] = contacts_list[ind][ind2] + worker[ind2]
                contacts_list[ind] = contacts_list[i]
        i += 1
    # collecting a new list without duplicates:
    new_contacts_list = []
    for i in contacts_list:
        if i in new_contacts_list:
            continue
        else:
            new_contacts_list.append(i)
    return new_contacts_list


if __name__ == '__main__':
    with open("phonebook_raw.csv") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    distrib_name()
    edit_phone_number()
    contacts_list = join_records()

    with open("phonebook.csv", "w", encoding='cp1251') as f:
      datawriter = csv.writer(f)
      datawriter.writerows(contacts_list)

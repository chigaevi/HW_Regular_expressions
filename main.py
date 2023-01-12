import csv
import re


def distrib_name():
    i = 0
    for staff in contacts_list:
      if staff[1] == '' and staff[2] == '':
          name_staff = staff[0].split()
          for ind in range(len(name_staff)):
              contacts_list[i][ind] = name_staff[ind]
          i += 1
          # print(name_staff)
      elif staff[1] != '' and staff[2] == '':
          name_staff = [staff[0]]
          name_staff.extend(staff[1].split())
          for ind in range(len(name_staff)):
              contacts_list[i][ind] = name_staff[ind]
          i += 1
          # print(name_staff)
      else:
          i += 1

def edit_phone_number():
    i = 0
    for staff in contacts_list:
        phone_number = staff[5]
        pattern = r'(\+7|^8)\s*\(*(\d{3})\)*\s*\-*(\d{3})\s*\-*(\d{2})\s*\-*(\d{2})\s*\(*(доб.)*\s*(\d{4})*\)*'
        rep = r'+7(\2)\3-\4-\5 \6\7'
        new_number = re.sub(pattern,rep,phone_number)
        contacts_list[i][5] = new_number
        i += 1

def join_records():
    i = 0
    count_staff = len(contacts_list)
    count_prop = len(contacts_list[0])
    for staff in contacts_list:
        if i+1 == count_staff:
            continue
        lastname = staff[0]
        for ind in range(i, count_staff):
             if lastname == contacts_list[ind][0]:
                for ind2 in range(count_prop):
                    if contacts_list[ind][ind2] == '' or staff[ind2] == '':
                        contacts_list[i][ind2] = contacts_list[ind][ind2] + staff[ind2]
                        contacts_list[ind][ind2] = contacts_list[i][ind2]
        i += 1

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

from pprint import pprint
import csv
import re

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)
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



distrib_name()
edit_phone_number()
pprint(contacts_list)

# for staff in contacts_list:


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV

# with open("phonebook.csv", "w", encoding='cp1251') as f:
#   datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
#   datawriter.writerows(contacts_list)

import os
import time

period = int(input('How often do you want to count files (s:second) : '))
print("**Program started***")
print(f"Files will be counted every {period} seconds... ")
file_1, dir_1 = 0, 0
file_2, dir_2 = 0, 0
count = 0
total_query = 0
start_time = time.time()

while True:
    dir_name = 'C:/python/'
    dir_name2 = 'D:/Siemens'
    for r, directory, files in os.walk(dir_name):
        for dir in directory:
            dir_1 += 1
        for fil in files:
            file_1 += 1

    total_1 = dir_1 + file_1

    for r2, directory2, files2 in os.walk(dir_name2):
        for dir2 in directory2:
            dir_2 += 1
        for fil2 in files2:
            file_2 += 1

    total_2 = dir_2 + file_2

    print('-'*70)
    print(f'{count+1}-) counted with os.walk (C:/python): {file_1} file, {dir_1} directory, {total_1} total object')
    print(f'{count+1}-) counted with os.walk 2 (D:/Siemens): {file_2} file, {dir_2} directory, {total_2} total object')
    dir_1, file_1 = 0, 0
    dir_2, file_2 = 0, 0
    time.sleep(period)
    count += 1
    total_query += 2
    if count >= 10:
        request = input('Do you want to continue or enough (c/e) :')
        if request == "c":
            count = 0
            continue
        else:
            end_time = time.time()
            print(f'Exiting the count... Total query is : {total_query}\n'
                  'Total query time (second) :', round(end_time-start_time,2))
            break









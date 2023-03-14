import xlrd, xlwt
import subprocess
import re
import os
# import xlrd
# book = xlrd.open_workbook("C:/Users/jiaqi17/Desktop/test.xls")
# sh = book.sheet_by_index(0)
# file_lis = []
# for rx in range(1, sh.nrows):
#     path = sh.cell_value(rx, 0)
#     filename = sh.cell_value(rx, 1)
#     file_lis.append(path+filename)
# print(file_lis)
# format_lis = []

# for i in file_lis:
#     tridArgsPath = ("trid.exe " + i + " -ae")
#     try:
#         a = subprocess.check_output(tridArgsPath).decode('utf-8').strip().split('\n')
#         print(a)
#         p = re.compile(r'[(](.*?)[)]', re.S)
#         m = re.findall(p, str(a))
#         if len(m) > 2:
#             print(m[1])
#             format_lis.append(m[1])
#         else:
#             format_lis.append(" ")
#     except:
#         format_lis.append(" ")


# for i in format_lis:
#     print(i)

def show_all_files(dire):
    """
    input the directory, show the mimetype of the files

    :param dire:
    :return:
    """
    for home, subdirs, files in os.walk(dire):
        for idx, fil in enumerate(files):
            print(fil)


if __name__ == '__main__':
    show_all_files("C:/Users/jiaqi17/Desktop/test37")



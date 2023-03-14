import magic
import json
import os
import subprocess
import re

# load the mimetype - extension convert list
with open("mimetype-extension conversion.json", 'r') as openfile:
    convert_dict = json.load(openfile)


def search_all_files_without_extension(dire):
    """
    given the file_folder path, putting all the files without extension paths into the list

    :param dire: the path of the directory

    :return:the updated list of all paths
    """
    file_lis = []
    for home, subdirs, files in os.walk(dire):
        for idx, fil in enumerate(files):
            if "." not in fil: # search only files without extension
                file_lis.append(home+"/"+fil)
    return file_lis


def append_extensions(file_lis):
    """
    this func is to append extensions based on the mimetypes

    :param file_lis: the list of files
    :return:
    """
    for file in file_lis:
        mimetype = magic.from_file(file, mime=True)
        if mimetype in convert_dict.keys():
            if mimetype == "application/octet-stream": # if the type is the octet-stream, using trid to append.
                tridArgsPath = ("trid.exe " + file + " -ae")
                try:
                    a = subprocess.check_output(tridArgsPath).decode('utf-8').strip().split('\n')
                    print(a)
                    p = re.compile(r'[(](.*?)[)]', re.S)
                    m = re.findall(p, str(a))
                    if len(m) > 2:
                        continue
                    else:  # # if trid can't decide, append .bin
                        extension = convert_dict.get(mimetype)
                        path_after = file + extension
                        try:
                            os.rename(file, path_after)
                        except:
                            print(file + " can't be processed.")
                except:
                    extension = convert_dict.get(mimetype)
                    path_after = file + extension
                    try:
                        os.rename(file, path_after)
                    except:
                        print(file + " can't be processed.")
            else:    # other types use the convert vocabulary
                extension = convert_dict.get(mimetype)
                path_after = file + extension
                try:
                    os.rename(file, path_after)
                except:
                    print(file + " can't be processed.")


def show_all_files_mimetype(dire):
    """
    input the directory, show the mimetype of the files

    :param dire:
    :return:
    """
    for home, subdirs, files in os.walk(dire):
        for idx, fil in enumerate(files):
            mimetype = magic.from_file(home+"/"+fil, mime=True)
            print(home+"/"+fil, "%", mimetype)


if __name__ == '__main__':
    file_lis_target = search_all_files_without_extension("C:/Users/jiaqi17/Desktop/test37")  # change the directory in the path
    append_extensions(file_lis_target)

import tkinter as tk
from tkinter import ttk
import os
from tkinter import filedialog
import tkinter.messagebox
import ttkbootstrap
import xlwt
import datetime
now = datetime.datetime.now()
select_lis = []
lis_before = []
lis_after = []

# renaming


def show_all_files(dire, root, tree):
    """
    given the file_folder path, using the Treeview to show all the files in the subfolder

    :param dire: the path of the directory
    :param root: the root of the treeview
    :param tree: the treeview created
    :return:the updated treeview
    """
    for home, subdirs, files in os.walk(dire):
        for idx, dire in enumerate(subdirs):
            sub_path = home+"/"+dire
            sub_id = tree.insert(root, idx, text=dire, values=home+"/"+dire, open=0)
            select_lis.append(home+"/"+dire)
            if var1.get():
                show_all_files(sub_path, sub_id, tree)
        for idx, fil in enumerate(files):
            tree.insert(root, idx, text=fil, values=home+"/"+fil)
            select_lis.append(home+"/"+fil)
        break
    return tree


def rename_file(replace_bf, replace_af, file_path):
    """
    This function is designed to rename the files.

    :param replace_bf: the character you want to replace
    :param replace_af: the character you want to replace with
    :param file_path: the original file path
    :return:
    """
    t1 = "\\\\?\\"
    t2 = file_path
    t2 = t2.replace("/", "\\")
    p = t1 + t2
    t2_lis = t2.split("\\")
    src = p
    if replace_bf in t2_lis[-1]:
        t2_lis[-1] = t2_lis[-1].replace(replace_bf, replace_af)
        file_renamed = "\\".join(t2_lis)
        t3 = file_renamed
        dest = t1 + t3
        print(src, dest)
        try:
            os.rename(src, dest)
        except:
            tk.messagebox.showinfo(title='Wrong',
                                   message=src + " can't be renamed.")
        lis_before.append(t2)
        lis_after.append(t3)

def quick_rename(file_path):
    """
    This is the function for the quick renaming, to strip all the |$|-|_|&|@|=|;|/|:|+|,|?|\|{|^|}|%|`|]|"|>|[|~|<|#||| in the file paths.
    :param replace_bf:
    :param replace_af:
    :param file_path:
    :return:
    """
    t1 = "\\\\?\\"
    t2 = file_path
    t2 = t2.replace("/", "\\")
    p = t1 + t2
    t2_lis = t2.split("\\")
    src = p
    if ("$" in t2_lis[-1]) or ("_" in t2_lis[-1]) or ("&" in t2_lis[-1]) or ("@" in t2_lis[-1]) or ("=" in t2_lis[-1]) or (";" in t2_lis[-1]) or ("/" in t2_lis[-1]) or (":" in t2_lis[-1]) or ("+" in t2_lis[-1]) or ("," in t2_lis[-1]) or ("?" in t2_lis[-1]) or ("\\" in t2_lis[-1]) or ("{" in t2_lis[-1]) or ("^" in t2_lis[-1]) or ("}" in t2_lis[-1]) or ("%" in t2_lis[-1]) or ("`" in t2_lis[-1]) or ("]" in t2_lis[-1]) or ("\"" in t2_lis[-1]) or (">" in t2_lis[-1]) or ("[" in t2_lis[-1]) or ("~" in t2_lis[-1]) or ("<" in t2_lis[-1]) or ("#" in t2_lis[-1]):
        t2_lis[-1] = t2_lis[-1].replace("#", "").replace("$", "").replace("-", "").replace("_", "").replace("&", "").replace("@", "").replace("=", "")\
            .replace("=", "").replace(";", "").replace("/", "").replace(":", "").replace("+", "").replace(",", "").replace("?", "")\
            .replace("\\", "").replace("{", "").replace("}", "").replace("^", "").replace("%", "").replace("`", "").replace("]", "")\
            .replace("\"", "").replace(">", "").replace("[", "").replace("~", "").replace("<", "").replace("#", "").replace("|", "")
        file_renamed = "\\".join(t2_lis)
        t3 = file_renamed
        dest = t1 + t3
        print(src, dest)
        try:
            os.rename(src, dest)
        except:
            tk.messagebox.showinfo(title='Wrong',
                                    message = src + " can't be renamed.")
        lis_before.append(t2)
        lis_after.append(t3)

def browse_button():
    select_lis.clear()
    for item in tree1.get_children("I001"):
        tree1.delete(item)
    filename = filedialog.askdirectory()
    goTo.delete("1.0", "end")
    goTo.insert("end-1c", filename)
    show_all_files(filename, root1, tree1)


def replace_button():
    # adjust the sequence so that the former renaming won't lead to the sub file not found
    select_lis_reordered = sorted(select_lis, key=len, reverse=True)
    for i in select_lis_reordered:
        print(i)
    before = replace_before.get(1.0, "end-1c")
    after = replace_after.get(1.0, "end-1c")
    for i in select_lis_reordered:
        rename_file(before, after, i)
    lbl_completed.config(text="Renaming completed. Please refresh the path.")
    export_all_Button.place(x=700, y=400, width=40, height=30)

def quick_button():
    # adjust the sequence so that the former renaming won't lead to the sub file not found
    select_lis_reordered = sorted(select_lis, key=len, reverse=True)
    for i in select_lis_reordered:
        print(i)
    for i in select_lis_reordered:
        quick_rename(i)
    lbl_completed.config(text="Renaming completed. Please refresh the path.")
    export_all_Button.place(x=700, y=400, width=40, height=30)

def show_help():
    result = tk.messagebox.showinfo(title = 'help',message='I am help info. More questions please contact Philo Wang (jiaqi17@illinois.edu)')
    print(result)

def export_all():
    lbl_message_for_replace.config(text="Exporting...")
    xl = xlwt.Workbook(encoding='utf-8')
    sheet = xl.add_sheet('Renamed Files', cell_overwrite_ok=False)
    sheet.write(0, 0, "Name")
    sheet.write(0, 1, "New Name")
    for i in range(0, len(lis_before)):
        sheet.write(i+1, 0, lis_before[i])
        sheet.write(i+1, 1, lis_after[i])
    xl.save('FilesChange-'+str(now.strftime("%Y%m%d%H%M%S"))+'.xls')
    with open('FilesChange-'+str(now.strftime("%Y%m%d%H%M%S"))+'.txt',"w") as f:
        for i in range(0, len(lis_before)):
            f.write("<premis:event xmlns:premis=\"http://www.loc.gov/premis/v3\"" + "\n")
            f.write("xsi:schemaLocation=\"http://www.loc.gov/premis/v3 http://www.loc.gov/standards/premis/v3/premis.xsd\" version=\"3.0\">" + "\n")
            f.write("<premis:eventIdentifier>" + "\n")
            f.write("<premis:eventIdentifierType>UUID</premis:eventIdentifierType>" + "\n")
            f.write("<premis:eventIdentifierValue>?</premis:eventIdentifierValue>" + "\n")
            f.write("</premis:eventIdentifier>" + "\n")
            f.write("<premis:eventDateTime>"+now.strftime("%Y-%m-%dT%H:%M:%SZ")+"</premis:eventDateTime>" + "\n")
            f.write("<premis:eventDetailInformation>" + "\n")
            f.write("<premis:eventDetail>prohibited characters removed: program=\"sanitize_names\"; version=\"?\"</premis:eventDetail>" + "\n")
            f.write("</premis:eventDetailInformation>" + "\n")
            f.write("<premis:eventOutcome></premis:eventOutcome>" + "\n")
            f.write("<premis:eventOutcomeDetail>" + "\n")
            f.write("<premis:eventOutcomeDetailNote>Original name=\""+lis_before[i]+"\"; cleaned up name=\""+lis_after[i]+"\"</premis:eventOutcomeDetailNote>" + "\n")
            f.write("</premis:eventOutcomeDetail>" + "\n")
            f.write("</premis:eventOutcomeInformation>" + "\n\n\n\n\n\n")
    lbl_message_for_replace.config(text="DONE.")

frame_all = tk.Tk()
frame_all.title("BulkRenamingForLibraryCollections")
frame_all.iconbitmap('favicon.ico')
frame_all.geometry('800x600')
note1 = ttk.Notebook(frame_all,width=800, height=600)
note1.pack(fill=tk.BOTH, expand=True)
frame = tk.Frame(frame_all)
frame2 = tk.Frame(frame_all)
frame3 = tk.Frame(frame_all)

style = ttkbootstrap.Style("sandstone")
menubar = tk.Menu(frame_all)
menubar.add_command(label="Help", command = show_help)
frame_all['menu'] = menubar


def goTothis():
    select_lis.clear()
    for item in tree1.get_children("I001"):
        tree1.delete(item)
    path = goTo.get(1.0, "end-1c")
    show_all_files(path, root1, tree1)

# TextBox Creation
goTo = tk.Text(frame,
               height=1,
               width=800)

goTo.place(x=0,y=0, width=600, height=30)

# Button Creation
searchButton = tk.Button(frame,
                         text="browse",
                         command=browse_button)
searchButton.place(x=650,y=0, width=50, height=30)

# Button Creation
goButton = tk.Button(frame,
                     text="GO",
                     command=goTothis)
goButton.place(x=600,y=0, width=40, height=30)

quickButton = tk.Button(frame,
                        text="Quick Rename",
                        command=quick_button)
quickButton.place(x=620, y=300, width=100, height=30)
lbl_quick = tk.Label(frame,  wraplength=150, text="repalce all whitespaces and |$||_|&|@|=|;|/|:|+|,|?|\|{|^|}|%|`|]|\"|>|[|~|<|#|||")
lbl_quick.place(x=595, y=250, width=150, height=50)

lbl = tk.Label(frame, text="")
lbl.place(x=0, y=40, width=600, height=10)

tree1 = ttk.Treeview(frame, show="tree")
root1 = tree1.insert("", 0, text="Files", open=1)
vsb = ttk.Scrollbar(frame, orient="vertical", command=tree1.yview)
vsb.place(x=550, y=50, height=400)
tree1.configure(yscrollcommand=vsb.set)
tree1.place(x=0, y=50, width=550, height=400)
replaceButton = tk.Button(frame,
                          text="replace",
                          command=replace_button)
replaceButton.place(x=710, y=180, width=50, height=30)
lbl_bf = tk.Label(frame, text="Replace:")
lbl_bf.place(x=600, y=105, width=50, height=20)
lbl_af = tk.Label(frame, text="With:")
lbl_af.place(x=600, y=135, width=50, height=20)
replace_after = tk.Text(frame,
                        height=1,
                        width=20)

replace_after.place(x=650, y=130, width=120, height=30)

replace_before = tk.Text(frame,
                         height=1,
                         width=20)

replace_before.place(x=650, y=100, width=120, height=30)
lbl_completed = tk.Label(frame, wraplength=100)
lbl_completed.place(x=600, y=430, width=150, height=100)
var1 = tk.BooleanVar()
if_sub_folders = tk.Checkbutton(frame, text='sub_folder', variable=var1, onvalue=True, offvalue=False)
if_sub_folders.select()
if_sub_folders.place(x=550, y=30, width=100, height=30)

lbl_message_for_replace = tk.Label(frame, text="Exporting:")
lbl_message_for_replace.place(x=600, y=400, width=100, height=30)
export_all_Button = tk.Button(frame,
                     text="export",
                     command=export_all)



# searchfor

search_for_lis = []
long_path = []

def search_for():
    search_for_lis.clear()
    for item in tree3.get_children("I001"):
        tree3.delete(item)
    path = Findthis.get(1.0, "end-1c")
    target = Finditem.get(1.0, "end-1c")
    search_all_files(path, root2, tree2, target)
    for i in range(0, len(search_for_lis)):
        tree3.insert(root3, i, text=search_for_lis[i], values=search_for_lis[i])
    lbl_count.config(text="Found " + str(len(search_for_lis)) + " files.")
    lbl_message.place_forget()
    tk.messagebox.showinfo(title='Done',
                           message='Search finished.')

def search_for_long_path():
    long_path.clear()
    for item in tree3.get_children("I001"):
        tree3.delete(item)
    path = Findthis.get(1.0, "end-1c")
    search_all_long_files(path, root2, tree2)
    for i in range(0,len(long_path)):
        tree3.insert(root3, i , text=long_path[i], values=long_path[i])
    lbl_count.config(text = "Found "+str(len(long_path))+" files.")
    tk.messagebox.showinfo(title='Done',
                           message='Long Path files Search finished.')
    exportButton.place(x=650, y=500, width=50, height=30)

def browse_button2():
    filename = filedialog.askdirectory()
    Findthis.delete("1.0", "end")
    Findthis.insert("end-1c", filename)

def search_all_long_files(dire, root, tree):
    """
    given the file_folder path, using the Treeview to show all the files in the subfolder

    :param dire:
    :param root:
    :param tree:
    :return:
    """
    for home, subdirs, files in os.walk(dire):
        for idx, dire in enumerate(subdirs):
            sub_path = home+"/"+dire
            print(len(sub_path))
            sub_id = tree.insert(root, idx, text=dire, values=home+"/"+dire, open=0)
            search_all_long_files(sub_path, sub_id, tree)
        for idx, fil in enumerate(files):
            sub_path = home + "/" + fil
            if len(sub_path) >= 255:
                tree.insert(root, idx, text=fil, values=home+"/"+fil)
                long_path.append(home+"/"+fil)
        break
    return tree

def search_all_files(dire, root, tree, search_char):
    """
    given the file_folder path, using the Treeview to show all the files in the subfolder

    :param dire:
    :param root:
    :param tree:
    :return:
    """
    for home, subdirs, files in os.walk(dire):
        for idx, dire in enumerate(subdirs):
            sub_path = home+"/"+dire
            if search_char in dire:
                search_for_lis.append(home + "/" + dire)
            sub_id = tree.insert(root, idx, text=dire, values=home+"/"+dire, open=0)
            search_all_files(sub_path, sub_id, tree, search_char)
        for idx, fil in enumerate(files):
            if search_char in fil:
                tree.insert(root, idx, text=fil, values=home+"/"+fil)
                search_for_lis.append(home+"/"+fil)
        break
    return tree

def export_longpath():
    lbl_message.config(text="Exporting...")
    xl = xlwt.Workbook(encoding='utf-8')
    sheet = xl.add_sheet('Long Path Files', cell_overwrite_ok=False)
    for i in range(0, len(long_path)):
        sheet.write(i, 0, long_path[i])
    xl.save('longpath-'+str(now.strftime("%Y%m%d%H%M%S"))+'.xls')
    lbl_message.config(text="DONE.")


# TextBox Creation
Findthis = tk.Text(frame2,
                   height=1,
                   width=800)

Findthis.place(x=100,y=0, width=600, height=30)

Finditem = tk.Text(frame2,
               height=1,
               width=800)

Finditem.place(x=100,y=50, width=450, height=30)

# Button Creation
FindButton = tk.Button(frame2,
                       text="Search",
                       command=search_for)

FindButton.place(x=550,y=50, width=40, height=30)
browseButton2 = tk.Button(frame2,
                          text="browse",
                          command=browse_button2)
browseButton2.place(x=650,y=0, width=50, height=30)

LongPathButton = tk.Button(frame2,
                           text="Search for long path files",
                           command=search_for_long_path)

LongPathButton.place(x=630,y=50, width=150, height=30)

exportButton = tk.Button(frame2,
                         text="export",
                         command = export_longpath)
exportButton.place(x=650, y=500, width=50, height=30)
exportButton.place_forget()

lbl_count = tk.Label(frame2)
lbl_count.place(x=600, y=100, width=100, height=20)

lbl_dire = tk.Label(frame2, text="Search in:")
lbl_dire.place(x=0, y=5, width=100, height=20)

lbl_or = tk.Label(frame2, text="or")
lbl_or.place(x=600, y=50, width=20, height=20)

lbl_searchitem = tk.Label(frame2, text="Contain:")
lbl_searchitem.place(x=0, y=55, width=100, height=20)

lbl_message = tk.Label(frame2, text="Please wait...")
lbl_message.place(x=600, y=200, width=200, height=100)

tree2 = ttk.Treeview(frame2, show="tree")
root2 = tree2.insert("", 0, text="Files", open=1)


tree3 = ttk.Treeview(frame2, show="tree")
root3 = tree3.insert("", 0, text="Files", open=1)
vsb = ttk.Scrollbar(frame2, orient="vertical", command=tree3.yview)
vsb.place(x=550, y=100, height=400)
tree3.configure(yscrollcommand=vsb.set)
vsb_h = ttk.Scrollbar(frame2, orient="horizontal", command=tree3.xview)
vsb_h.place(x=0, y=500, width=550)
tree3.configure(xscrollcommand=vsb_h.set)
tree3.place(x=0, y=100, width=550, height=400)




# trid
def fun_trid():
    """
    created by Tracy Popp

    :return:
    """
    import os, subprocess, pathlib
    from tkinter.filedialog import askdirectory

    rootDir = askdirectory() #navigate to the directory where you would like to start trid analysis

    #make sure this path matches the path to trid.exe on the machine you're running the script on
    tridDir = ("trid.exe")

    outfile = open('files.txt', 'w', encoding='utf-8')
    tridOut = open("tridOutput.txt-"+str(now.strftime("%Y%m%d%H%M%S"))+".txt", 'w', encoding='utf-16')

    file_count = 0
    fileList = []
    # traversing the dir tree code from here: https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python

    for root, dirs, files in os.walk(rootDir):
        level = root.replace(rootDir, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)), file=outfile)
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))
            tridFilePath = (os.path.join(tridDir,root,f))
            tridFileNorm = (os.path.normpath(tridFilePath))
            tridArgsPath = (tridDir+" " + '"{}"'.format(tridFileNorm) + " -ce -v") #getting quotes to print tip found here: https://stackoverflow.com/questions/27757133/how-to-print-variable-inside-quotation-marks/27757142
            subprocess.call(tridArgsPath, stdout=tridOut)
            file_count += 1
            fileList.append(f)

    outfile.write("\n".join(fileList)) #unpacking the list elements from fileList and writing them out to the outfile
    print("\n""\n" "TrID processed", file_count,  "files", file=outfile)
    tridOut.close()
    outfile.close()
    lbl_trid_feedback = tk.Label(frame3, wraplength=300,
                         text="Done. Find the output file in the same directory as this tool. ")
    lbl_trid_feedback.place(x=10, y=300, width=800, height=200)

TrIDButton = tk.Button(frame3,
                     text="Choose a directory",
                     command=fun_trid)
TrIDButton.place(x=350,y=230, width=150, height=30)
lbl_trid_intro = tk.Label(frame3,  wraplength=300, text="This function allows users to browse to a directory, scans the directory for files without extensions. TRiD tries to identify the file types and append an appropriate file extension. The script should also create a report identifying which files have been modified. ")
lbl_trid_intro.place(x=10, y=10, width=800, height=200)
note1.add(frame, text='Rename')
note1.add(frame2, text='Search')
note1.add(frame3, text='TrID')
frame_all.mainloop()
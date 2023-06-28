# 2023-DigitalPresTool
This tool is designed and developed by Digital Preservation Department in UIUC library. The purpose of this tool is to assist the library staff manage the archive documents and files.
## Table of Contents
- [Version Control](#Version)
- [What is DigitalPresTool](#What)
- [Why use DigitalPresTool](#Why)
- [How to Download](#download)  
- [Rename](#rename)  
- [Search](#search)  
- [TrID](#TrID)  
## Version Control<a name="Version"></a>
- v1.0, 01/2023
## What is DigitalPresTool<a name="What"></a>
DigitalPresTool is a tool for facilitating the preservation process. It currently includes renaming the files, identifying long path files and expending extensions to extentionless files.
## Why use DigitalPresTool<a name="Why"></a>
- RENAMING 
- Long Path Files 
- Extension Appending 
## How to Download<a name="download"></a>
1. Go to [dowloading address](https://github.com/PhiloJiaqiWang/2023-DigitalPresTools)
2. click on 'Code'  
![Image text](https://github.com/PhiloJiaqiWang/2023-DigitalPresTools/blob/main/imgs/download1.png)
3. click on download ZIP 
![Image text](https://github.com/PhiloJiaqiWang/2023-DigitalPresTools/blob/main/imgs/download2.png)
4. unzip the file and go in to the folder, find the Bulkrenaming.exe and click on that  
![Image text](https://github.com/PhiloJiaqiWang/2023-DigitalPresTools/blob/main/imgs/download3.png)
## Rename<a name="rename"></a>
![Image text](https://github.com/PhiloJiaqiWang/2023-DigitalPresTools/blob/main/imgs/Rename1.png)
- A  
Enter the path of the target directory, and press go.
- B  
Browse the path of the target directory directly.
- C  
Check this if you want to include the sub_folders. (ps:hidden files already included)
- D  
Enter the character you want to replace and replace with here, and click on the replace button.
- E  
This panel is to show the structure of the target directory. This panel will be shown after click on the go or browse.
- F  Quick Rename  
This button is for the quick renaming, once clicking on the button, it'll strip all these characters from the target directory.
![Image text](https://github.com/PhiloJiaqiWang/2023-DigitalPresTools/blob/main/imgs/Rename2.png)
- G  
After the renaming is completed, click on the export button. A csv file includes the original file names and the renamed file names will be generated under the same folder you put the Bulkrenaming.exe.
![Image text](https://github.com/PhiloJiaqiWang/2023-DigitalPresTools/blob/main/imgs/Rename3.png)
## Search<a name="search"></a>
![Image text](https://github.com/PhiloJiaqiWang/2023-DigitalPresTools/blob/main/imgs/Search1.png)
- A  
Browse the target directory
- B  
Enter the character or characters you want to find here, and click on the Search Button.
- C  
Instead of doing B, click on this button to search in the target directory the long name file paths.
- D  
After clicking on the Search Button or Search for long path files Button, all the files that falls into the scope will be shown here.
![Image text](https://github.com/PhiloJiaqiWang/2023-DigitalPresTools/blob/main/imgs/Search2.png)
- F  
Shows the number of files that meet the conditions
- G  
If you are searching for the long path files, after the search, an export button will appaer. Click on the Export Button, a csv file includes all the long file paths will be generated under the same folder you put the Bulkrenaming.exe.
## TrID<a name="TrID"></a>
![Image text](https://github.com/PhiloJiaqiWang/2023-DigitalPresTools/blob/main/imgs/TRID1.png)
- A  
Click on this button to browse the target directory. The script calls the command line version of the program, allows users to browse to a directory, scans the directory for files without extensions. TRiD tries to identify the file types and append an appropriate file extension. The script should also create a report identifying which files have been modified. The report is also under the same folder as you put the Bulkrenaming.exe 

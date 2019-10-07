# ICS File To Folder Structure
> This program takes an ics file as its input, processes its content, and creates a customized folder structure on the platform its ran on. Using the simplest specifications, a single folder will be created for every single event's start date.

## Anatomy of an ics file
To understand how this program works, let's first understand how an ics file is composed.

In an ics file every event is described as follows:
```
BEGIN:VEVENT
DTSTAMP:20190930T162515Z
UID:5a1a71f7-56da-4581-954a-03187c47d6d6
DTSTART:20191015T130000Z
DTEND:20191015T143000Z
LOCATION:PC-Unterrichtsraum 5\, Währinger Straße 29 2.OG
SUMMARY:051111-4 PUE Repetitorium Mathematische Grundlagen der Informatik 1
URL:https://ufind.univie.ac.at/de/course.html?lv=051111&semester=2019W#gr4
END:VEVENT
```
This program processes every single event, and creates a folder based on the `DTSTART` attribute's value.

## Installation and Execution
```
git clone https://github.com/Peti0401/ics-to-folder-struct.git

cd ics-to-folder-struct

python3 main.py
```

## Usage example

Make sure to point to an existing file with ics extension.
```
Enter the path of the ics file: /full/path/to/file.ics
```

Choose a directory to which you would like to generate the directories.
```
Enter the path of the enclosing directory: /some/path/to/dir
```

Decide whether you want to include specific sub-directories into the generated directories. You can specify as many sub-directories and nesting-levels as you wish. 
```
Would you like to specify sub-directories? (yes/no) - 
```

Input - Output examples in case of choosing the option `yes`:

* `my-dir` creates `/some/path/to/dir/2019_12_01/my-dir`
* `my-dir/sub1` creates `/some/path/to/dir/2019_12_01/my-dir/sub1`
* `my-dir/sub2` creates `/some/path/to/dir/2019_12_01/my-dir/sub2`

Decide whether you want to include specific files into the generated directories or sub-directories.
```
Would you like to specify files? (yes/no) - 
```
Input - Output examples in case of choosing the option `yes`:

* `my-file.txt` creates `/some/path/to/dir/2019_12_01/my-file.txt`
* `my-dir/my-file.txt` creates `/some/path/to/dir/2019_12_01/my-dir/my-file.txt`

Well done, you are ready!
```
Directories created!
```

## TODOS
The program is in a functioning state at this point, howver, it is pretty far from being ready. The following features and improvements are planned to be developed in the future:

- [ ] Handle invalid input exceptions
- [ ] Specify content for files
- [ ] Create a GUI option
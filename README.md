![alt text](https://www.geeksultd.com/wp-content/uploads/2020/06/image.png)
# AirBnB Clone
This project is a collaborative project by Sean Taylor and Usman Abdul Jabbar as a part of the Holberton School curriculum.

## Description
This project aims to replicate the usage of a data management system with the help of Python classes, JSON and other methods, including a custom console to efficiently create, delete, view and manage users and data.

This repository contains all the necessary code to replicate the usage of such a data storage system with Python classes acting as the backbone of the entire system and aided by the a console attached to this repo for convenience.

In addition to to all the necessary code available in this repo, as a part of the Holberton School curriculum test files have been added to indicate the usage of unittest modules in Python.

As a simple overview of the file structure:
- All classes/data structures are available in the /models folder.
- All unit tests are available in the /tests directory.
- The console is available root of this repository.
- The initial test/main files offered by the Holberton intranet are in the /main_files folder.

# The Console
The console is an incredible addition to the data management segment of the AirBnB clone project. Its goal is to efficiently create, store, destory and recall data with a few strokes.

The console could be executes by simply invoking it in the terminal
```
./console
```
## Supported Commands & Usage
The console comes with a number of unique commands that would help you parse through the data. Some of the commnads supported by the console are:
- help | This command allows you to view help for any command below and also showcases usage examples.
```
help create
```
- quit / EOF | These commands allow you to exit the console.
```
quit | EOF
```
- create | This command allows you to create a given data structure of any class, given that it exists. Upon successful creation, the console prints out the unique ID generated for the very object it just created. For more info, run `help create' in the console.
```
create City
```
- show | This command allows you to show a specific object that may or may not be present. For more info, run `help show` in the console.
```
show BaseModel 8fc93a0c-3b96-4af4-abf4-e40311533c90
```
- destroy | This command allows you to destroy a specific object that may or may not be present. For more info, run `help destroy` in the console.
```
destroy BaseModel 8fc93a0c-3b96-4af4-abf4-e40311533c90
```
- all | This command allows you tou view all the objects present. However, the all command also accepts an additional argument if one needs to view all the objects of a given class. For more info, run `help all` in the console.
```
all
```
or
```
all User
```
- update | This command allows you to update attributes of a specific object given that may or may not be present. For more info, run `help update` in the console.
```
update BaseModel 8fc93a0c-3b96-4af4-abf4-e40311533c90 message 'just a random text dummy'
```

## Files
|           FILE NAME           |                                             DESCRIPTION                                            |
|:-----------------------------:|:--------------------------------------------------------------------------------------------------:|
| AUTHORS                       | Contains the names and emails of the contributors                                                  |
| console.py                    | Console that eases the management of all the data                                                  |
| models/*                      | Contains all the individual models necessary to create different types of data                     |
| models/engine/file_storage.py | Contains the core functions and code responsible for storing and pulling out data.                 |
| main_files/*                  | Contains all the main files provided by the Holberton School curriculum to ensure expected output. |

```
AirBnB_clone$ ls -l
├── AUTHORS
├── console.py
├── file.json
├── main_files
│   ├── test_base_model_dict.py
│   ├── test_base_model.py
│   ├── test_save_reload_base_model.py
│   └── test_save_reload_user.py
├── models
│   ├── amenity.py
│   ├── base_model.py
│   ├── city.py
│   ├── engine
│   │   ├── file_storage.py
│   │   ├── __init__.py
│   │   └── README.md
│   ├── __init__.py
│   ├── place.py
│   ├── README.md
│   ├── review.py
│   ├── state.py
│   └── user.py
├── README.md
└── tests
    └── README.md
```

### AUTHORS
- Sean Taylor - sean.taylor[at]holbertonschool.com
- Usman Abdul Jabbar - usmangta[at]gmail.com | UsmanJabbar.com

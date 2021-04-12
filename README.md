# Youtube_Video_Downloader
A Python program to open a window where we can put a youtube video link and click the download button to download it.

## Requirements:
- Install pytube library from pypi.org This library is used to get functions that can download youtube videos
- Install tkinter library from pypi.org This library is used for creating a GUI and it has lots of function in it.

## Pytube library:
- pytube is a very serious, lightweight, dependency-free Python library (and command-line utility) for downloading YouTube Videos.
- It has no third party dependencies and aims to be highly reliable.
- pytube also makes pipelining easy, allowing you to specify callback functions for different download events, such as on progress or on complete.
- Finally pytube also includes a command-line utility, allowing you to quickly download videos right from terminal.

## Python GUI – tkinter:
- Python offers multiple options for developing GUI (Graphical User Interface). Out of all the GUI methods, tkinter is the most commonly used method. It is a standard Python interface to the Tk GUI toolkit shipped with Python. Python with tkinter is the fastest and easiest way to create the GUI applications. Creating a GUI using tkinter is an easy task.
### To create a tkinter app:
- Importing the module – tkinter
- Create the main window (container)
- Add any number of widgets to the main window
- Apply the event Trigger on the widgets.
- Importing tkinter is same as importing any other module in the Python code. Note that the name of the module in Python 2.x is ‘Tkinter’ and in Python 3.x it is ‘tkinter’.
  - import tkinter
- There are two main methods used which the user needs to remember while creating the Python application with GUI.
   - Tk(screenName=None,  baseName=None,  className=’Tk’,  useTk=1): To create a main window, tkinter offers a method ‘Tk(screenName=None,  baseName=None,  className=’Tk’,     useTk=1)’. To change the name of the window, you can change the className to the desired one. The basic code used to create the main window of the application is:
       - m=tkinter.Tk() where m is the name of the main window object
   - mainloop(): There is a method known by the name mainloop() is used when your application is ready to run. mainloop() is an infinite loop used to run the application, wait for an event to occur and process the event as long as the window is not closed.
       - m.mainloop()   
- tkinter also offers access to the geometric configuration of the widgets which can organize the widgets in the parent windows. There are mainly three geometry manager classes class.
   - **pack()** method:It organizes the widgets in blocks before placing in the parent widget.
   - **grid()** method:It organizes the widgets in grid (table-like structure) before placing in the parent widget.
   - **place()** method:It organizes the widgets by placing them on specific positions directed by the programmer.
 - There are a number of widgets which you can put in your tkinter application. Some of the major widgets are listed below
  - button
  - activebackground
  - activeforeground
  - bg
  - command
  - font
  - image
  - width
  - height 
- All the details of creating a GUI using tkinter can be learned here [tkinter](https://www.geeksforgeeks.org/python-gui-tkinter/)

## Setting up path:
### How to install and write python codes?
- Go to www.python.org
- Choose the latest python version suitable for your user interface  machine (mac,windows,liinux etc).
- It will be installed and in your machines as either terminal or command line or python.
- To check python is installed or not , Type print command in command line & check the output. While other easier way of checking is using anaconda as described below.
- Other way of using python is using google colab (Go to Google colab in google) and run python using your machine (including mobile phones).

### Anaconda:-  
- Go to  www.anacond.com  & download.
- It is like a  bundle that is downloaded with python and along with famous libraries. It is preferred by most data scientists.
- Find anaconda navigator in your machine and open it. You will find different visualizing tools like jupyter lab, jupyter notebook, spyder, orange3, vs code, rstudio, vs code. We need this bundle spyder.

### Spyder IDE:- 
- Spyder is an open-source cross-platform IDE. The Python Spyder IDE is written completely in Python. It is designed by scientists and is exclusively for scientists, data analysts, and engineers. It is also known as the Scientific Python Development IDE and has a huge set of remarkable features.
- How to start programming in Spyder IDE:-
   - Step1: Open Anaconda navigator and select spyder & click launch.
   - Step2: Create a new folder and rename it.
   - Step3: Go inside the folder and go into new options and select python 3.
   - Step4: Name the python file.
   - Step5: Type the code in the cell. And to run the code run arrow in above tool bar.
 
 ## Modules & Packages:- 
- Modules are nothing but a file (with .py extension) which we can import into a particular program
- Group of modules(python files) is known as package 
### Pypi.org :
- pypi.org is a website where we all can get different libraries which we can use for a different purpose.
- How to install a library from pypi.org
   - Go to pypi.org.
   - Search for a library according to your need.
   - Copy the text which says “pip install library name”.
   - In Jupyter notebook type “!” and paste the content and run the cell.
   - The library is installed on the local machine
### How to create our module:
   - Modules are created using a special keyword which is only for Jupyter notebook and Google Colab.
   - Create a module by
       - %%writefile ModuleName.py
       - #And write a python code
   - Import the module in another program and use the functions inside the module
      - import ModuleName
      - ModuleName.FunctionName()
### How to create Package:-
- Make a folder and rename it(That is your package name)
- Now we can import a module through the package, like
   - from packageName import moduleName

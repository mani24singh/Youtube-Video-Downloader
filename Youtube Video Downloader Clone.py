## Python program for downloading youtube videos

# importing required Dependencies
import pytube
from pytube import YouTube

# using python tkinter GUI
from tkinter import *
root = Tk()

root.geometry("300x400")  # gometry size for GUI
root.title("Youtube Video Downloader")  # title for our GUI

# Define background image
bkg = PhotoImage(file = r"C:\Users\Admin\Documents\Learning Programming\Youtube Video Downloader\image\youtube.png")

# define a function for the downloading task
def youtube():
    a = var.get()   # example link to paste in gui box: https://www.youtube.com/watch?v=bFPDaDoruTY #https://www.youtube.com/watch?v=mxYNdy-0CEs
    ytvideo = YouTube(a).streams.filter(progressive=True,file_extension="mp4").order_by('resolution').desc().first()
    ytvideo.download(r"C:\Users\Admin\Documents\Projects")   # folder to save downloaded videos
      
    print("Entry box",a)

def Close():
    root.destroy()
    
# Create a background label for image
l1 = Label(root,image = bkg)
l1.place(x=0, y=0, relwidth=1, relheight=1)

# Add a text label to the top of our background image
my_text = Label(root, text= "Welcome to Downloader!!", font=("Helvetica",30), fg="Red", bg= '#e1e1e1')
my_text.pack(pady=70)

# Create a frame to add a text label and user input box
my_frame  = Frame(root, bg= '#e1e1e1')
my_frame.pack(pady=5)

# Create a label for user input
l2 = Label(my_frame, text="Paste Youtube Video Link in the Box",fg= "black",font=("bold",20), bg= '#e1e1e1')
l2.grid(row=0,column=0, padx=20)

# Add a user's link input box
var = StringVar()
e1 = Entry(my_frame,textvariable=var,width=80)
e1.grid(row=1,column=0, padx=20)

# Create another frame to add multiple buttons in a line
my_frame1  = Frame(root, bg= '#e1e1e1')
my_frame1.pack(pady=200)

# create a download button 
b1 = Button(my_frame1,text="Download",command=youtube,bg="green",width=20,fg="white")
b1.grid(row=0,column=0, padx=50)

# create a exit button to close the GUI
b2 = Button(my_frame1,text="Exit",command=Close,bg="black",width=10,fg="white")
b2.grid(row=0,column=2, padx=50)
         
root.mainloop()
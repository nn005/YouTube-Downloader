from tkinter import*
from pytube import YouTube

# Configuration and creation of the gui window
root = Tk()
root.geometry('800x500')
root.resizable(0,0)
root.title("Python Stock Quote")
root.configure(bg='#FFDEDE')

# Title of the title of the gui
title_label = Label(root,text = 'Youtube Video/Audio Downloader', font ='arial 20 bold', bg='#FFDEDE')
title_label.pack( anchor="center")

# linkGui is a StringVar() variable to receive the youtube video link from the entry widget
linkGui = StringVar()

# Label to direct where to input the link
entry_label = Label(root, text = 'Input Youtube Video Link Below', font = 'arial 15 bold', bg='#FFDEDE')
entry_label.pack( anchor="center", pady=30)

# Entry widget which receives the input from the user and passes it to the linkGui variable
linkGui_enter = Entry(root, width = 45, textvariable = linkGui, justify = 'center')
linkGui_enter.pack(anchor="center")


# The Download function receives the inputted link and uses the pytube library fucntions to download the video in an mp4 format
def Download():

    # Uses the get method and stores the value of the link entered in the entry widget as a string in the variable Video
    Video = str(linkGui.get())

    # The Video variable is passed to the pytube Youtube() function and stored as yt
    yt = YouTube(Video)

    # mp4 is a filtered version of ryt to only include data (streams) of versions of the linked video in mp4 format
    mp4 = yt.streams.filter(file_extension='mp4')

    # Sets the stream variable equal to the first version in the available mp4 versions/streams
    stream = mp4.first()

    # This downloads the video
    stream.download()

    # Label to display completion
    entry_label = Label(root, text = 'MP4 Download complete! Go to same folder where this program is located to access your video.', font = 'arial 15 bold', bg='#FFDEDE')
    entry_label.pack( anchor="center", pady=10)


# The Download function receives the inputted link and uses the pytube library fucntions to download the video in an mp4 format in 720p HD quality
def Download_HD():

    Video = str(linkGui.get())
    
    yt = YouTube(Video)

    # res is a filtered version of yt to only include data (streams) of versions of the linked video in 720p quality
    res = yt.streams.filter(res="720p")

    # mp4 is a filtered version of res to only include data (streams) of versions of the linked video in mp4 format
    mp4 = res.filter(file_extension='mp4')

    stream = mp4.first()

    stream.download()

    entry_label = Label(root, text = 'HD Download complete! Go to same folder where this program is located to access your video.', font = 'arial 15 bold', bg='#FFDEDE')
    entry_label.pack( anchor="center", pady=10)

def Download_Audio():

    Video = str(linkGui.get())
    
    yt = YouTube(Video)

    # audio is a filtered version of yt to only include data (streams) of versions of the linked video that only contain audio
    audio = yt.streams.filter(only_audio=True)

    # mp4 is a filtered version of res to only include data (streams) of versions of the linked video in mp4 format
    mp4 = audio.filter(file_extension='mp4')

    stream = mp4.first()

    stream.download()

    entry_label = Label(root, text = 'Audio Download complete! Go to same folder where this program is located to access your video.', font = 'arial 15 bold', bg='#FFDEDE')
    entry_label.pack( anchor="center", pady=10)


    
# "Download As MP4" button calls the Download() function when clicked
search_button = Button(root,text = 'Download As MP4', font = 'arial 15 bold', padx = 2, command = Download)
search_button.pack(anchor="center", pady=3)

# "Download In HD" button calls the Download_HD() function when clicked
search_button = Button(root,text = 'Download In HD', font = 'arial 15 bold', padx = 2, command = Download_HD)
search_button.pack(anchor="center", pady=3)

# "Download Audio" button calls the Download_Audio() function when clicked
search_button = Button(root,text = 'Download Audio', font = 'arial 15 bold', padx = 2, command = Download_Audio)
search_button.pack(anchor="center", pady=3)





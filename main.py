from apiclient.discovery import build #Google API KEY For GOOGLE CUSTOM SEARCH
import tkinter as tk
import webbrowser
import random
import wget #Used For Downloading Images
from tkinter import messagebox
from faker import Faker
fake = Faker()

my_word_list = [
'Python','Hacking','hacker',
'Java','college','PROJECT',
'bug','Tejas','Attendandce',
'Security','Sarthak','Iceream','Buy A New Phone' ]

resultImage=[]
search_title=[]
search_urls=[] # All The Url's Fetched Will Be Stored Here
gsearch_images=[] #Global Image Links Storing List
small_font=("Courier", 20) # Setting Universal Small Size For GUI

api_key = "AIzaSyApHwy2t9VooegRr5AdlAOVoJKDJ7gASD4" # Secret Api Key

resource = build("customsearch", 'v1', developerKey=api_key).cse() # Creating Searchable Object

'''
Searching The Links Function is Listed Below 
'''
def SearchItems(search_keyword):
    global search_title # it stores the title of all search results during the program execution

    search_images=[]# it stores the links of images of search result

    search_links=[] # it stores the links of all search results during the program execution

    result = resource.list(q=search_keyword, cx='012710808344381167897:glmyjwcjw2t').execute()  # Fetching All The Results & Links Of Website

    for i in range(1, 30, 10):
        resultImageUrl = resource.list(q=search_keyword, cx='012710808344381167897:glmyjwcjw2t', searchType='image', start=i).execute()
        global resultImage
        resultImage += resultImageUrl['items']
        ext = []

       # print(result['items'][0]['pagemap']['cse_thumbnail'][0]['src'])P


    '''
    Saving All The Images Urls In search_image list
    '''
    for item in resultImage:
        search_images.append(item['link'])
    for i in search_images:
        if(i[-3:]=='png'):
            print(i)
            ext.append(i)
    global gsearch_images
    gsearch_images= ext
    '''
      Saving All The Sites  Urls In search_links list & Title in search_titles
    '''

    for item in result['items']:
        search_title.append(item['title'])
        search_links.append(item['link'])


    for i in range(7):
        ResultLabel=tk.Button(root,text=str(search_title[i]),font=small_font,bg='black',fg='white',activebackground='green',activeforeground='white',width=300)
        ResultLabel.pack()
        global search_urls
        search_urls.append(search_links[i])
        print(search_title[i],search_links[i])
    CreateAnalayzeButton()
    print(search_urls)
# SearchItems()
def Savetext():
    for i in range(40):
        data=fake.sentence(ext_word_list=my_word_list)+'\n'
        f=open('data.txt','a')
        f.write(str(data))
        f.close()
    messagebox.showinfo('Success','File Named Data Has Been Saved Successfully')
    messagebox.pack()

def GetData():
    print('Will Get The Data When Sarthak Will Set Me Up')
def CreateAnalayzeButton():
    AnalayzeButton = tk.Button(BottomFrame, text="Analayze Results Now", font=large_font, fg='black', bg='yellow',command=lambda:ScrapedWindow(int(random.randrange(0,10)),gsearch_images))
    AnalayzeButton.pack(padx=10, pady=30)
def ImageData(image_urls):
    local_files=[]
    for i in image_urls:
        if "*" in i:
            print('Match Occured Sorry you Are Out')
            continue
        else:
            local_files.append(wget.download(i))
    print(local_files)
    msg=str(len(local_files))+" Files Has Been Downloaded"
    messagebox.showinfo("Success",msg)
def callbackurl(y):
    print(y)
    webbrowser.open_new(y)
def UrlWindow():
    UrlWindow = tk.Tk()
    UrlWindow.title('Data Analyst Urls')
    Heading = tk.Label(UrlWindow, text="Open Url By Clicking On Buttons Below", bg='Blue', fg='White', font=large_font)
    Heading.pack(fill='x', padx=10, pady=10)
    UrlWindow.geometry("1920x1080")
    for i in range(len(search_urls)):
        UrlLabel = tk.Button(UrlWindow, text=str(search_title[i]), font=small_font, bg='black', fg='white',activebackground='green', activeforeground='white', width=300,command=lambda:callbackurl(str(search_urls[i])))
        UrlLabel.pack()
    UrlWindow.mainloop()
def ScrapedWindow(x,images_links):
     print(images_links)
     ScrapedWindow=tk.Tk()
     ScrapedWindow.title('Data Analyst Started')
     Heading=tk.Label(ScrapedWindow,text="Choose An Option",bg='Blue',fg='White',font=large_font)
     Heading.pack(fill='x',padx=10, pady=10)
     ScrapedWindow.geometry("1920x1080")
     GetTextData=tk.Button(ScrapedWindow, text =" Display Text Data" ,font=large_font,fg='black',bg='yellow',command=Savetext,width=60) # Get Data Function Should Be Created
     GetTextData.pack(padx=10, pady=10)
     GetImageData = tk.Button(ScrapedWindow, text="Download Images", font=large_font, fg='black', bg='yellow', command=lambda:ImageData(images_links),width=60)  # Get Data Function Should Be Created
     GetImageData.pack(padx=10, pady=10)
     GetUrlsData = tk.Button(ScrapedWindow, text="Display Url", font=large_font, fg='black', bg='yellow',command=UrlWindow,width=60)  # Get Data Function Should Be Created
     GetUrlsData.pack(padx=10, pady=10)
     GetBack = tk.Button(ScrapedWindow, text="Get Back", font=large_font, fg='black', bg='yellow',command=ScrapedWindow.destroy,width=60)  # Get Data Function Should Be Created
     GetBack.pack(padx=10, pady=10)
     ScrapedWindow.mainloop()
'''
The Main Project Is Started From This Line 
'''
root=tk.Tk() # Creating GUI Window
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side='right', fill='y')
root.title("Data Collector - Efficent Search Results & Data") # Giving Title To Window
root.geometry("1920x1080") # Giving Dimensions To Window
large_font = ("Courier", 44)
TopFrame=tk.Frame(root,bg='yellow') # Creating Top Frame
TopFrame.pack(side="top") # Packing It In Top Side
BottomFrame=tk.Frame(root,bg='black') # Creating Bottom Frame
BottomFrame.pack(side="bottom") # Packing It In Bottom Side
SearchLabel= tk.Label (TopFrame,text='Enter Search Query ',bg='yellow',fg='black') # Created Search Label
SearchLabel.config(font=("Courier", 44)) # Changing Font Size of Label
SearchLabel.pack(side="left",padx=10)  # Packing Search Label On  Left Side
SearchEntryBox = tk.Entry(TopFrame,width=25, font=large_font ,bd=5)
SearchEntryBox.pack(side='left',padx=10)
SearchButton = tk.Button(TopFrame, text =" Search" ,font=large_font,fg='black',bg='yellow',command=lambda:SearchItems(SearchEntryBox.get()))
SearchButton.pack(side='left',padx=10,pady=30)
root.mainloop()  # Running Until Cross Button Presses
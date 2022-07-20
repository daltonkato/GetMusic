# importing the module 
from pytube import YouTube 

output_path = 'C:/Python_Projects/Youtube'

try:
    url = "https://www.youtube.com/watch?v=P-FG_ULHNfc"
    video = YouTube(url)
except:
    print ("Error on URL")

try:
    stream = video.streams.get_audio_only()
except:
    print ("Error getting audio")

try:
    stream.download(output_path)
except:
    print ("Error Downloading")



'''
# where to save 
SAVE_PATH = "C:/Python_Projects" #to_do 
  
# link of the video to be downloaded 
link="https://www.youtube.com/watch?v=hSEMmZI7cz8"
  
try: 
    # object creation using YouTube
    # which was imported in the beginning 
    yt = YouTube(link) 
except: 
    print("Connection Error") #to handle exception 
  
# filters out all the files with "mp4" extension 
mp4files = yt.filter('mp4') 
  
#to set the name of the file
yt.set_filename('teste_video.mp4')  

# get the video with the extension and
# resolution passed in the get() function 
d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution) 
try: 
    # downloading the video 
    d_video.download(SAVE_PATH) 
except: 
    print("Some Error!") 
print('Task Completed!') 
'''
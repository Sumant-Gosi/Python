import os


def CreateIfNotExists(folder):
    if not os.path.exists(folder): #Checking if the folder exists
        os.makedirs(folder)        #If the folder does not exists, then create that folder


files = os.listdir()                #Reading all the files in the folder
files.remove("main.py")
print(files)

CreateIfNotExists('Images') 
CreateIfNotExists('Docs')
CreateIfNotExists('Media')
CreateIfNotExists('Zips')
CreateIfNotExists('Others')

#Second argument of splittext() returns the extension of the files

imgExts = [".jpg", ".jpeg", ".png", ".gif"]
images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]  
print(images)


docExts = [".txt", ".doc", ".ppt", ".docx", ".pdf"]
docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts] 
print(docs)

mediaExts = [".mp4", ".mp3"]
medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts] 
print(medias) 

zipExts = [".rar", ".zip"]
zips = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]  
print(zips)


 #if file is of a different ext, putting it in other folder
others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in imgExts) and (ext not in docExts) and (ext not in mediaExts) and (ext not in zipExts) and os.path.isfile(file): 
        others.append(file)

print(others)

#Moving  files to their respective folder folder

for media in medias:
    os.replace(media, f"Media/{media}")   

for image in images:
    os.replace(image, f"Images/{image}")

for doc in docs:
    os.replace(doc, f"Docs/{doc}")

for other in others:
    os.replace(other, f"Others/{other}")

for zip in zips:
    os.replace(zip, f"Zips/{zip}")  


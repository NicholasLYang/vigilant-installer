import urllib2, json
from sys import exit

ip = raw_input("Please enter the ip address ")
key = "nyang"

def start():
    print "If at any time you wish to leave, type 'exit'"
    print "\nWelcome Mr. DW!"
    print "What would you like to do today?\n"
    main()

#Doesn't have greetings so that it can call itself
def main():    
    functions = [
        "Delete Image",
        "List Galleries",
        "Create Gallery",
        "Delete Gallery",
        "List Years",
        "Archive Year",
        "Unarchive Year"
    ]
    
    print "Choose the number of the option you'd like to select:"
    goal = userInput(functions)
    
    if goal == 0: #delete image
        print "\nWhich gallery is the image in?"
        gallery = askGallery()
        print "\nWhich image would you like to delete?"
        images = getImages(gallery)
        image = images[ userInput(images) ]
        confirm = raw_input("\nAre you sure want to delete %s in %s? (y/n) "%(image,gallery))

        if isY(confirm):
            print #empty line
            print "Deleting . . ."
            print deleteImage(image, gallery)
        else:
            print "Deletion canceled"

    elif goal == 1: #list galleries
        galleries = getGalleries()
        print "\nHere is a list of galleries:"
        printList(galleries)

    elif goal == 2: #add gallery
        print "\nWhat would you like to name your new gallery?"
        name = raw_input()
        print createGallery(name)
        
    elif goal == 3: #delete gallery
        print "\nWhich gallery would you like to delete?"
        gallery = askGallery()
        print "\nAre you sure you want to delete %s? (y/n)"%(gallery)
        confirm = raw_input()

        if isY(confirm):
            print #empty line
            print "Deleting . . ."
            print deleteGallery(gallery)
        else:
            print "Deletion canceled"
        
    elif goal == 4: #list years 
        print "Archived year:"
        print printList(getArchivedYears())
        print "Unarchived years:"
        print printList(getUnarchivedYears())
        
    elif goal == 5: #archive year 
        print "Which year would you like to archive?" 
        years = getArchivedYears()
        year = userInput(years)
        print archiveGalleries(year)
        
    elif goal == 6: #unarchives year
        print "Which year would you like to unarchive?"
        years = getUnarchivedYears()
        year = userInput(years)
        print unarchiveGalleries(year)
        
    #Asks at the end if user would like to continue or exit
    print #empty line
    print "Continue? (y/n) "
    confirm = raw_input()
    if isY(confirm):
        print #new line
        main()        
    

def printList(coll):
    for index, item in enumerate(coll):
        print str(index) + " " + item
    print

#sendingData is supposed to determine whether the
#api is sending json data or not
def callAPI(url,sendingData):
   # print url
    request = urllib2.urlopen(url)
    result = request.read()
    if result == "Error":
        print "Error, invalid key"
        exit()
    if (sendingData):
        return  json.loads(result)
    return result

def getImages(gallery):
    uri = "http://" + ip + "/getimagename/%s/%s"
    url = uri%(key, gallery)
    return callAPI(url, True)

def getGalleries():
    uri = "http://" + ip + "/getgalleries/%s"
    url = uri%(key)
    return callAPI(url, True)
    
def deleteImage(img, gallery):
    uri = "http://" + ip + "/deleteimage/%s/%s/%s"
    url = uri%(key, gallery, img)
    out = callAPI(url, False)
    if out == "success":
        return "%s in %s has been deleted"%(img, gallery)
    print out
    return "Error, image not deleted"

def deleteGallery(gallery):
    uri = "http://" + ip + "/deletegallery/%s/%s"
    url = uri%(key, gallery)
    out = callAPI(url, False)
    if out == "success":
        return gallery + " has been deleted"
    print out
    return "Error, gallery not deleted"

def createGallery(gallery):
    uri = "http://" + ip + "/creategallery/%s/%s"
    url = uri%(key, gallery)
    out = callAPI(url, False)
    if out == "success":
        return "\n" + gallery + " has been created"
    print out
    return "Error, gallery not created"

def archiveGalleries(year):
    uri = "http://" + ip + "/archivegalleries/%s/%s"
    url = uri%(key, year) 
    out = callAPI(url, False)
    print out
    if out == "success":
        return "\nThe galleries from " + year +" have been archived"
    print out
    return "Error, galleries not archived"

def unarchiveGalleries(year):
    uri = "http://" + ip + "/unarchivegalleries/%s/%s"
    url = uri%(key, year) 
    out = callAPI(url, False)
    print out
    if out == "success":
        return "\nThe galleries from " + year +" have been unarchived"
    print out
    return "Error, galleries not unarchived"

def getUarchivedYears():
    uri = "http://" + ip + "/getVisibleGalleries/%s"
    url = uri%(key) 
    return callAPI(url, True)

def getArchivedYears():
    uri = "http://" + ip + "/getInvisibleGalleries/%s"
    url = uri%(key) 
    return callAPI(url, True)
    
def askGallery():
    galleries = getGalleries()
    galNum = userInput(galleries)
    return galleries[galNum]

#checks answer to (y/n) questions
def isY(inpt):
    inpt = inpt.lower()
    if inpt == "y" or inpt == "yes":
        return True
    return False

#like range except numbers are strings
def strRange(num):
    lst = range(num)
    return [ format(x,'') for x in lst ]

#makes sure user input is a valid choice
#Otherwise asks again
def userInput(options):
    printList(options)
    inpt = raw_input()
    if inpt == "exit":
        exit()
    validVals = strRange(len(options))
    while( inpt not in validVals ):
        print "\nI'm sorry, DW. I'm afraid I can't do that."
        print "Please submit a number " + validVals[0] + "-" + validVals[-1]
        printList(options)
        inpt = raw_input()
        if inpt == "exit":
            exit()
    return int(inpt)

        
start()



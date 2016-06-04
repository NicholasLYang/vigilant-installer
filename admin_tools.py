import urllib2, json
ip = raw_input("Please enter the ip address ")
key = "nyang"

def start():
    print "\nWelcome Mr. DW!"
    print "What would you like to do today?\n"
    main()

#Doesn't have greetings so that it can call itself
def main():    
    functions = [
        "Delete Image",
        "List Galleries",
        "Add Gallery",
        "Delete Gallery",
        "List Years",
        "Archive Year"]
    
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
            print "Deleting . . ."
            print deleteImage(image, gallery)
        else:
            print "Deletion canceled"
        print #empty line

    elif goal == 1: #list galleries
        galleries = getGalleries()
        print "\nHere is a list of galleries:"
        printList(galleries)

    elif goal == 2: #add gallery #work in progress
        """
        print "\nWhat would you like to name your new gallery?"
        name = raw_input()
        #addGallery(name)
        print "The " + name + " gallery has been created"
        """
        print "Feature coming soon"
        
    elif goal == 3: #delete gallery
        print "\nWhich gallery would you like to delete?"
        gallery = askGallery()
        print "\nAre you sure you want to delete %s? (y/n)"%(gallery)
        confirm = raw_input()

        if isY(confirm):
            print "Deleting . . ."
            print deleteGallery(gallery)
        else:
            print "Deletion canceled"
        print #empty line        
        
    elif goal == 4: #list years #work in progress
        """
        years = getYears()
        print "Here is a list of all the years archived:"
        print years
        """
        print "Feature coming soon"
        
    elif goal == 5: #archive year #work in progress
        """
        print "Are you sure would like to archive this year(%s)'s galleries? (y/n)"%(year)
        confirm = raw_input()

        if isY(confirm):
            archiveYear()
        else:
            print "Archive canceled"
        """
        print "Feature coming soon"
        
    #Asks at the end if user would like to continue or exit
    print "Continue? (y/n) "
    confirm = raw_input()
    if isY(confirm):
        print #new line
        main()        
    

def printList(coll):
    for index, item in enumerate(coll):
        print str(index) + " " + item
    print
   
def callAPI(url):
   # print url
    request = urllib2.urlopen(url)
    result = request.read()
    return  json.loads(result)

def getImages(gallery):
    uri = "http://" + ip + "/getimagename/%s/%s"
    url = uri%(key, gallery)
    return callAPI(url)

def getGalleries():
    uri = "http://" + ip + "/getgalleries/%s"
    url = uri%(key)
    return callAPI(url)
    
def deleteImage(img, gallery):
    uri = "http://" + ip + "/deleteimage/%s/%s/%s"
    url = uri%(key, gallery, img)
    out = callAPI(url)
    if out == "Error":
        return out
    return "%s in %s has been deleted"%(img, gallery)

def deleteGallery(gallery):
    uri = "http://" + ip + "/deletegallery/%s/%s"
    url = uri%(key, gallery)
    out = callAPI(url)
    if out == "Error":
        return out
    return gallery + " has been deleted"

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
    validVals = strRange(len(options))
    while( inpt not in validVals ):
        print "\nI'm sorry, DW. I'm afraid I can't do that."
        print "Please submit a number " + validVals[0] + "-" + validVals[-1]
        printList(options)
        inpt = raw_input()
    return int(inpt)

        
start()



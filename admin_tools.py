import urllib2, json, urllib
from sys import exit
from datetime import datetime

ip = raw_input("Please enter the ip address ")
key = "mrdwisawesome"

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
        "Visibility Options",
    ]

    print "Choose the number of the option you'd like to select:"
    goal = userInput(functions)

    if goal == 0: #delete image
        year = askYear()
        print "\nWhich gallery is the image in?"
        gallery = askGallery(year)
        print "\nWhich image would you like to delete?"
        images = getImages(year, gallery)
        image = images[ userInput(images) ]
        confirm = raw_input("\nAre you sure want to delete %s in %s? (y/n) "%(image,gallery))

        if isY(confirm):
            print #empty line
            print "Deleting . . ."
            print deleteImage(year, image, gallery)
        else:
            print "Deletion canceled"

    elif goal == 1: #list galleries
        year = askYear()
        galleries = getGalleries(year)
        print "\nHere is a list of galleries:"
        printList(galleries)

    elif goal == 2: #add gallery
        print "\nWhat YEAR would like to add your gallery to?"
        year = raw_input()
        #year = str(datetime.today().year) #uncomment this to always add to current year
        print "\nWhat would you like to NAME your new gallery?"
        name = raw_input()
        print createGallery(year,name)

    elif goal == 3: #delete gallery
        year = askYear()
        print "\nWhich gallery would you like to delete?"
        gallery = askGallery(year)
        print "\nAre you sure you want to delete %s? (y/n)"%(gallery)
        confirm = raw_input()

        if isY(confirm):
            print #empty line
            print "Deleting . . ."
            print deleteGallery(year, gallery)
        else:
            print "Deletion canceled"

    elif goal == 4: #list
        print printList(getYears())

    elif goal == 5: #Visibility options
        options = [
            "List Visible Galleries",
            "List Invisible Galleries",
            "Make Gallery Invisible",
            "Make Gallery Visible",
            "Make Entire Year Invisible",
            "Make Entire Year Visible"
            ]
        print "Choose the number of the option you'd like to select:"
        choice = userInput(options)
        if choice == 0: #list visible
            years = getVisYears()
            if len(years) != 0:
                print "\nWhich year do you want to see the galleries from?"
                year = years[userInput(years)]
                print "\nVisible galleries from " + str(year)
                printList(getVisible(year))
            else:
                print "There are no visible galleries" 
        elif choice == 1: #list invisible
            years = getInvisYears()
            if len(years) != 0:
                print "\nWhich year do you want to see the galleries from?"
                year = years[userInput(years)]
                print "\nInvisible galleries from " + str(year)
                printList(getInvisible(year))
            else:
                print "There are no invisible galleries at the moment"
        elif choice == 2: #make gal invis
            years = getVisYears()
            if len(years) != 0:
                print "\nWhich year is the gallery you want to make invisible from?"
                year = years[userInput(years)]
                gals = getVisible(year)
                if len(gals) != 0:
                    print "\nWhich gallery would you like to make invisible?"
                    gallery = userInput(gals)
                    print "Invisilizing . . ."
                    print makeGalInvisible(year, gals[gallery])
                else:
                    print "There are no visible galleries from " + str(year)
            else:
                print "There are no visible galleries to make invisible"
        elif choice == 3: #make gal vis
            years = getInvisYears()
            if len(years) != 0:
                print "\nWhich year is the gallery you want to make visible from?"
                year = years[userInput(years)]
                gals = getInvisible(year)
                if len(gals) != 0:
                    print "\nWhich gallery would you like to make visible?"
                    gallery = userInput(gals)
                    print "Visilizing . . ."
                    print makeGalVisible(year, gals[gallery])
                else:
                    print "There are no invisible galleries from " + str(year)
            else:
                print "There are no invisible galleries to make visible"
        elif choice == 4: #year invis
            years = getVisYears()
            if len(years) != 0:
                print "\nWhich year do you want to make visible?"
                year = years[userInput(years)]
                print "\nAre you sure you want to make all the galleries from %s invisible? (y/n)"%(year)
                confirm = raw_input()
    
                if isY(confirm):
                    print #empty line
                    print makeYrInvis(year) 
                else:
                    print "Deletion canceled"
            else:
                print "There are no visible years to make invisible"
        elif choice == 5: #year vis
            years = getInvisYears()
            if len(years) != 0:
                print "\nWhich year do you want to make visible?"
                year = years[userInput(years)]
                print "\nAre you sure you want to make all the galleries from %s visible? (y/n)"%(year)
                confirm = raw_input()
    
                if isY(confirm):
                    print #empty line
                    print makeYrVis(year) 
                else:
                    print "Deletion canceled"
            else:
                print "There are no invisible years to make visible"

    #Asks at the end if user would like to continue or exit
    print #empty line
    print "Would you like to do anything else? (y/n) "
    confirm = raw_input()
    if isY(confirm):
        print #new line
        main()


def printList(coll):
    for index, item in enumerate(coll):
        print str(index) + " " + str(item)
    print

#sendingData is supposed to determine whether the
#api is sending json data or not
def callAPI(url,sendingData):
   # print url
    request = urllib2.urlopen(url)
    result = request.read()
    if result == "Error, invalid key":
        print result
        exit()
    if (sendingData):
        return  json.loads(result)
    return result

def getCurrentGalleries():
    uri = "http://" + ip + "/getgalleries/%s"
    url = uri%(key)
    return callAPI(url, True)

def getGalleries(year):
    uri = "http://" + ip + "/getGalleriesInYear/%s/%s"
    url = uri%(key, year)
    return callAPI(url, True)

def getImages(year, gallery):
    uri = "http://" + ip + "/getimagename/%s/%s/%s"
    url = uri%(key, year, gallery)
    return callAPI(url, True) 

def deleteImage(year, img, gallery):
    img = urllib.quote_plus(img)
    uri = "http://" + ip + "/deleteimage/%s/%s/%s/%s"
    url = uri%(key, year, gallery, img)
    out = callAPI(url, False)
    if out == "success":
        return "%s in %s has been deleted"%(img, gallery)
    print out
    return "Error, image not deleted"

def deleteGallery(year, gallery):
    uri = "http://" + ip + "/deletegallery/%s/%s/%s"
    url = uri%(key, year, gallery)
    out = callAPI(url, False)
    if out == "success":
        return gallery + " has been deleted"
    print out
    return "Error, gallery not deleted"

def createGallery(year, gallery):
    uri = "http://" + ip + "/creategallery/%s/%s/%s"
    url = uri%(key, year, gallery)
    out = callAPI(url, False)
    if out == "success":
        return "\n" + gallery + " has been created"
    print out
    return "Error, gallery not created"

def makeGalInvisible(year, gallery):
    uri = "http://" + ip + "/setVisibility/%s/%s/%s/%s"
    url = uri%(key, 0, gallery, year)
    out = callAPI(url, False)
    if out == "success":
        return "\n" + gallery + " is now invisible"
    print out
    return "Error, gallery not created"

def makeGalVisible(year, gallery):
    uri = "http://" + ip + "/setVisibility/%s/%s/%s/%s"
    url = uri%(key, 1, gallery, year)
    out = callAPI(url, False)
    if out == "success":
        return "\n" + gallery + " is now visible"
    print out
    return "Error, gallery not created"

def makeYrInvis(year):
    uri = "http://" + ip + "/setVisibilityByYear/%s/%s/%s"
    url = uri%(key, 0, year)
    out = callAPI(url, False)
    if out == "success":
        return "\nAll galleries from " + str(year)  + " are now invisible"
    print out
    return "Error, gallery not created"

def makeYrVis(year):
    uri = "http://" + ip + "/setVisibilityByYear/%s/%s/%s"
    url = uri%(key, 1, year)
    out = callAPI(url, False)
    if out == "success":
        return "\nAll galleries from " + str(year) + " are now visible"
    print out
    return "Error, gallery not created"

def getVisible(year):
    uri = "http://" + ip + "/getVisibleGalleries/%s/%s"
    url = uri%(key,year)
    return callAPI(url, True)

def getInvisible(year):
    uri = "http://" + ip + "/getInvisibleGalleries/%s/%s"
    url = uri%(key,year)
    return callAPI(url, True)

def getYears():
    uri = "http://" + ip + "/getYears/%s"
    url = uri%(key)
    return callAPI(url, True)

def getVisYears():
    uri = "http://" + ip + "/getVisibleYears/%s"
    url = uri%(key)
    return callAPI(url, True)

def getInvisYears():
    uri = "http://" + ip + "/getInvisibleYears/%s"
    url = uri%(key)
    return callAPI(url, True)

def askYear():
    print "\nWhat year is this from?"
    years = getYears()
    year = userInput(years)
    return years[year]

def askPrevYears():
    print "\nWhat year are you interested in?"
    years = getYears()
    current = datetime.now().year
    years.remove(current)
    year = userInput(years)
    return years[year]

def askGallery(year):
    galleries = getGalleries(year)
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



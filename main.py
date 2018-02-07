
def addArtist():
   print "im"

def addCustomer():
   print "im"


def addArtwork():
   print "im"


def addLikeGroup():
   print "im"


def addLikeArtist():
   print "im"


def updateArtist():
   print "im"


def getAritsts():
   print "im"


def getCustomers():
   print "im"


def getArtworks():
   print "im"


def getGroups():
   print "im"


def getClassifies():
   print "im"


def getLikeGroups():
   print "im"


def getLikeArtists():
   print "im"

def promptUserInput():
   print "\nWELCOME to ArtBase by hype@2018\n"
   while True:
      print "\tEnter 1 to add an Artist"
      print "\tEnter 2 to add Customer"
      print "\tEnter 3 to add Work"
      print "\tEnter 4 to add Group Like"
      print "\tEnter 5 to update style of an artist"
      print "\tEnter 6 to retrieve records"
      print "\tEnter 7 to exit"
      user_inp = raw_input()
      if (user_inp == str(7)):
         exit()



def main():
   promptUserInput()


if __name__ == "__main__": main()

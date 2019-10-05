# object representation of a single event from an .ics file
# all variables hold solely the content of the properties
# Eg.: The line DTSTAMP:20191005T134238Z would be stored into the dtsmap variable with the value 20191005T134238Z


class Event:
    dtsamp = ""
    uid = ""
    dtstart = ""
    dtend = ""
    location = ""
    summary = ""
    url = ""

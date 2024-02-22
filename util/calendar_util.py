from gcsa.google_calendar import GoogleCalendar 
from gcsa.event import Event
import datetime
from beautiful_date import days
calendar = GoogleCalendar('carson.chan2007@gmail.com')
now = datetime.datetime.now()


def printEvents():
    print(f"At {now}, these are the active events: \n")
    for event in calendar:
        print(event)


def calList():
    for ca in calendar.get_calendar_list():
        print(ca)


def getEventCount():
    count = 0
    for event in calendar:
        count+=1
    return count
def addEvents(array):
    print(f"Adding {len(array)} events to calendar now...")
    for i in range(len(array)):
        name = array[i][0]
        coursename = array[i][2]
        end = array[i][1]
        description = array[i][3]
        event = Event(
                    start=end - 1*days,
                    summary=name,
                    end=end,
                    description=f"{description} \n\n Uploaded by Calendar API!",
                    color_id=str(array[i][4])
                    )
        # print(description)
        calendar.add_event(event)
        # stored.append(array[i])   
                
def deleteEvents():
    final = []
    for event in calendar.get_events(query="Uploaded by Calendar API!"):
        print(f"Deleting {event.summary} now!")
        calendar.delete_event(event)
        final.append(event)
    print("Deleting events done!")

# def testEvent():
#     # event = Event(start=datetime.datetime.now(), end=datetime.datetime.now()+1*days,name="test",summary="test",description="hi")
#     # calendar.add_event(event)
#      print()
        

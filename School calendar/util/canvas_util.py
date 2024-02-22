from canvasapi import Canvas, requester, user, assignment
from .config_util import *
import datetime
token = get_config_item("canvas_id")
canvas = Canvas("https://dexterschools.instructure.com/",token)

user = canvas.get_user(3233)
# tempcourse = canvas.get_course(12105)

# print(list(tempcourse.get_users()))
def getUser():
    
    return user
def getCourses():
    
    for course in user.get_courses(enrollment_state="active"):
            if course.id != 1422:
                try:
                    print(course)
                except:
                    pass
    return

def getAssignments():
    count=0
    assignmentArray = []
    print(f"Fetching all active assignments for {user.name} now...")
    for course in user.get_courses(enrollment_state="active"):
        count+=1    
        for assignment in user.get_assignments(course):
            if assignment.due_at != None:
                dt = datetime.datetime.fromisoformat(assignment.due_at)
                if dt.timestamp() >= datetime.datetime.now().timestamp():
                    assignmentArray.append([assignment.name,dt,course.name,assignment.description,str(count)])
                    # print("{} is due on {}".format(assignment.name,dt.strftime('%a %d %b %Y, %I:%M%p')))
    return assignmentArray                
    

def getCalendar():
    calendar = user.get_calendar_events_for_user()
    for event in calendar:
          print(event)
    return


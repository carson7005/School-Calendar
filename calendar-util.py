from gcsa.google_calendar import GoogleCalendar

calendar = GoogleCalendar('carson.chan2007@gmail.com')
for event in calendar:
    print(event)
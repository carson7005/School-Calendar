from util import calendar_util as cutil
from util import canvas_util as canvutil
from util import config_util as confutil
import datetime 

confutil.get_config()

def main():
        print("\n")
        print("Active user: {} \n".format(canvutil.getUser()))
      
       
        cutil.addEvents(canvutil.getAssignments())
        
        
        # cutil.deleteEvents()
if __name__ == "__main__":
    main()

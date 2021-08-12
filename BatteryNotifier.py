#TAG OF CREATOR
print(r"""


______       _   _                                _   _  __          
| ___ \     | | | |                              | | (_)/ _|         
| |_/ / __ _| |_| |_ ___ _ __ _   _   _ __   ___ | |_ _| |_ ___ _ __ 
| ___ \/ _` | __| __/ _ \ '__| | | | | '_ \ / _ \| __| |  _/ _ \ '__|
| |_/ / (_| | |_| ||  __/ |  | |_| | | | | | (_) | |_| | ||  __/ |   
\____/ \__,_|\__|\__\___|_|   \__, | |_| |_|\___/ \__|_|_| \___|_|   
                               __/ |                                 
                              |___/                                  v0.1  
                              												-Ojaswa RHX













	""")





















#pip install psutil
#pip install plyer
import psutil
import datetime
import time
from plyer import notification


#MAIN PROGGRAM LOOP
while True:
    Battery=psutil.sensors_battery()
    Percent=Battery.percent
    if Battery.power_plugged == False :
        Power = "OFF"
    else:
        Power = "ON"
    Timeleft=str(datetime.timedelta(seconds=Battery.secsleft))
        
    notification.notify(
        title="Battery Level",
        message=str(Percent) + " % " + "Power :" + str(Power)+f"  Time left : {Timeleft}",
        app_name="Battery Notifier v0.1",
        app_icon=r'C:\Users\MR.SATAN\Desktop\BN\BN.ico',
        timeout=1,
        
    )
    if Battery.percent >=95 and Power=="ON" :
        notification.notify(
            title="ALERT",
            message="Battery Charged by"+ str(Percent) + " % " + "Power :" + str(Power),
            app_name="Battery Notifier v0.1",
            app_icon=r'C:\Users\MR.SATAN\Desktop\BN\BN.ico',
            timeout=3,
            
        
        
        
        )
    time.sleep(60*60)
        
        
    continue
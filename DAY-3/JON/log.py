#login configuration
import logging
#setup

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,  # we can use any thing in ulid in functions
    format="%(asctime)s - [%(levelname)s] - %(message)s"
)  
#s = string  asctime=capture the date and time  levelname=info,warning all are works here

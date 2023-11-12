import requests
from datetime import datetime
import smtplib
import time

my_email = "tenzinchoeyingofa@gmail.com"
password = "zxqp fezs vrdi ryhg"

MY_LAT = 20.593683  # Your latitude
MY_LONG = 78.962883  # Your longitude


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #checking if my postion is within +5 or -5 degree of iss position
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():
    # time.sleep(30)
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now>=sunset or time_now<=sunrise:
        return True


while True:
    time.sleep(3)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="tenzinchoeying91@gmail.com",
                            msg="subject:LOOK UP !!!\n\n ISIS is over your head, look up right now")
        connection.close()
    else:
        print("iss is not over head yet")

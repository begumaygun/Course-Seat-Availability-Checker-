# Course-Seat-Availability-Checker-

This is a **Python script** that automates checking course seat availability using **Selenium**. The script logs into the university's course registration system, navigates to the course selection page, and continuously monitors available seats for selected courses. If a seat becomes available, it triggers an alert sound to notify the user.  

## Features  
- **Automated Login**: Logs into the system using provided credentials.  
- **Seat Monitoring**: Continuously checks for available spots in selected courses.  
- **Real-Time Alerts**: Plays a notification sound when a seat is found.  
- **Web Scraping with Selenium**: Uses **Selenium WebDriver** to interact with the website dynamically.  

## How to Use  

### 1. Install Dependencies  
```bash
pip install selenium
```


### 2. Download Chrome WebDriver  
- Ensure you have **Google Chrome** installed.  
- Download **ChromeDriver** from [here](https://chromedriver.chromium.org/downloads).  
- Place the `chromedriver.exe` in your script directory or add it to your system path.  

### 3. Run the Script  
Save the script as `course_checker.py` and run it with:  

```bash
python course_checker.py
```

4. Leave it Running
The script will automatically refresh the course selection page every 30 seconds.
If a seat becomes available, you will hear a notification sound.

How It Works
Logs into the course registration system using Selenium WebDriver.
Navigates to the course selection page and retrieves seat availability data.
Monitors selected courses at fixed intervals (default: 30 seconds).
Triggers a notification sound when a seat is found.

If you want to change the refresh interval, edit this line in course_checker.py:
```bash
time.sleep(30)  # Change 30 to your preferred interval in seconds
```

To monitor different courses, update the XPath values inside this list:
```bash
seat_xpaths = [
    "//*[@id='some_xpath1']",
    "//*[@id='some_xpath2']",
    "//*[@id='some_xpath3']"
]
```
Future Enhancements
🔹 Telegram Bot Notifications – Get real-time alerts on your phone.
🔹 Cloud Deployment – Run the script on a remote server.
🔹 GUI Interface – Add a simple UI for ease of use.

If you have any ideas for improvements, feel free to contribute! 🚀

## License
The project also uses [Selenium](https://www.selenium.dev/documentation/en/) which is licensed under the Apache 2.0 License.



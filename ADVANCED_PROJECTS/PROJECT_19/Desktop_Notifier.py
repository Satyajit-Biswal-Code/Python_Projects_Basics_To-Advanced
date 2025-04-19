#DESKTOP NOTIFIER

from plyer import notification
import time

if __name__=="__main__":
    while True:
        notification.notify(
            title="check",
            message="check your email",
            app_icon="D:\React.png",
            timeout=5)
        time.sleep(5)

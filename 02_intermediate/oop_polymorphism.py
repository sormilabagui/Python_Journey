# demonstrating polymorphism in python

class EmailNotification:
    def send(self):
        print("Sending email notifcation")

class SMSNotification:
    def send(self):
        print("Sending sms notification")

class PushNoification:
    def send(self):
        print("sending push notification")

#polymorphism in action
def notify_user(notification):
    notification.send()

email = EmailNotification()
sms = SMSNotification()
push = PushNoification()

#same func, diff behavior
notify_user(email)
notify_user(sms)
notify_user(push)
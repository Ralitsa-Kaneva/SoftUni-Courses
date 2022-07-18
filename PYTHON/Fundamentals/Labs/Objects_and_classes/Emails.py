class Email:

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def sent(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
input_data = input()

while input_data != "Stop":
    information = input_data.split(" ")
    sender = information[0]
    receiver = information[1]
    content = information[2]
    current_email = Email(sender, receiver, content)
    emails.append(current_email)
    input_data = input()

indices = input().split(", ")
indices_int = list(map(int, indices))

sent_emails = [emails[x].sent() for x in indices_int]

for x in emails:
    print(x.get_info())

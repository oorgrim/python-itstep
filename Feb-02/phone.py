class Phone:
    def __init__(self, brand, model, weight, size_of_memory) -> None:
        self.brand = brand
        self.model = model
        self.weight = weight
        self.size_of_memory = size_of_memory

    def make_call(self, number, person): # person - человек которому звонят
        print(f'Calling to {person} from {number}')
    
    def post_photo(self, social_media, date, time):
        print(f'Photo was posted on {date}  at {time} on {social_media}')
    
    def send_sms(self, messenger, recipient, message):
        print(f'Sending `{message}` on {messenger} to {recipient}...')

phone1 = Phone('Android', 'A23', '200', '256')
phone2 = Phone('Apple', 'IPhone 13', '204', '128') 
phone3 = Phone('Xiaomi', 'Poco X3 PRO', '204', '512') 

phone1.make_call('+77777123743', 'Alan')
phone2.post_photo('Jan-11', '17:07', 'Instagram')
phone3.send_sms('Telegram', 'Alana', 'Hello!')
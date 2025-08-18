class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []

    def call(self, other_phone):
        call_string = f"{self.phone_number} a appelé {other_phone.phone_number}"
        print(call_string)
        self.call_history.append(call_string)
        other_phone.call_history.append(f"{other_phone.phone_number} a reçu un appel de {self.phone_number}")

    def show_call_history(self):
        print(f"\nHistorique des appels pour le numéro {self.phone_number}:")
        if not self.call_history:
            print("Aucun appel dans l'historique.")
        else:
            for call in self.call_history:
                print(f"- {call}")

    def send_message(self, other_phone, content):
        message = {
            "to": other_phone.phone_number,
            "from": self.phone_number,
            "content": content
        }
        self.messages.append(message)
        other_phone.messages.append(message)
        print(f"Message envoyé de {self.phone_number} à {other_phone.phone_number}: '{content}'")

    def show_outgoing_messages(self):
        print(f"\nMessages envoyés depuis {self.phone_number}:")
        outgoing_msgs = [msg for msg in self.messages if msg["from"] == self.phone_number]
        if not outgoing_msgs:
            print("Aucun message envoyé.")
        else:
            for msg in outgoing_msgs:
                print(f"-> À : {msg['to']}, Contenu : '{msg['content']}'")

    def show_incoming_messages(self):
        print(f"\nMessages reçus par {self.phone_number}:")
        incoming_msgs = [msg for msg in self.messages if msg["to"] == self.phone_number]
        if not incoming_msgs:
            print("Aucun message reçu.")
        else:
            for msg in incoming_msgs:
                print(f"<- De : {msg['from']}, Contenu : '{msg['content']}'")

    def show_messages_from(self, phone_number):
        print(f"\nMessages reçus de {phone_number} par {self.phone_number}:")
        filtered_msgs = [msg for msg in self.messages if msg["from"] == phone_number]
        if not filtered_msgs:
            print(f"Aucun message reçu de {phone_number}.")
        else:
            for msg in filtered_msgs:
                print(f"-> Contenu : '{msg['content']}'")

if __name__ == "__main__":
    phone1 = Phone("0123456789")
    phone2 = Phone("0987654321")

    print("### Test des appels ###")
    phone1.call(phone2)
    phone2.call(phone1)
    phone1.call(phone2)

    phone1.show_call_history()
    phone2.show_call_history()

    print("\n\n### Test des messages ###")
    phone1.send_message(phone2, "Salut, comment ça va ?")
    phone2.send_message(phone1, "Ça va bien, merci ! Et toi ?")
    phone1.send_message(phone2, "Je suis occupé, je te rappelle plus tard.")
    phone1.send_message(phone1, "Ceci est un test pour moi-même.")

    phone1.show_outgoing_messages()
    phone1.show_incoming_messages()

    phone2.show_outgoing_messages()
    phone2.show_incoming_messages()

    phone1.show_messages_from("0987654321")
    phone2.show_messages_from("0123456789")

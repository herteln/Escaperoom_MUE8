import random
import string
from EscapeRoom import EscapeRoom
import lib.creditcard as CC


class CreditCardRoom(EscapeRoom):

    def __init__(self):
        super().__init__()
        self.set_metadata("Dr. Markus Berg", __name__)
        self.add_level(self.create_level1())

    ### LEVELS ###

    def create_level1(self):
        secret = ""

        if random.getrandbits(1):
            secret = CC.create_number()
        else:
            secret = CC.create_random_number()

        task_messages = [
            "Ist das eine gueltige Kreditkartennummer:",
            "<b>"+secret+"</b>"
        ]

        hints = [
            "Siehe Erklaerung im 1.Webinar"
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": CC.verify_number, "data": secret}




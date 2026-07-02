import re


class MaskingService:

    @staticmethod
    def mask_email(email: str):

        username, domain = email.split("@")

        if len(username) <= 2:
            return "*" * len(username) + "@" + domain

        return username[:2] + "*" * (len(username)-2) + "@" + domain

    @staticmethod
    def mask_phone(phone):

        digits = re.sub(r"\D", "", phone)

        return "*" * 6 + digits[-4:]

    @staticmethod
    def mask_pan(pan):

        return pan[:3] + "****" + pan[-3:]

    @staticmethod
    def mask_aadhaar(aadhaar):

        digits = aadhaar.replace(" ", "")

        return "XXXX XXXX " + digits[-4:]

    @staticmethod
    def mask_card(card):

        digits = re.sub(r"\D", "", card)

        return "************" + digits[-4:]

    @staticmethod
    def default(value):

        if len(value) <= 4:
            return "*" * len(value)

        return value[:2] + "*"*(len(value)-4)+value[-2:]
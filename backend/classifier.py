class RiskClassifier:

    WEIGHTS = {

        "emails":2,

        "phones":2,

        "pan_numbers":5,

        "aadhaar_numbers":5,

        "credit_cards":6,

        "bank_accounts":5,

        "ifsc_codes":3,

        "employee_ids":2,

        "github_tokens":8,

        "openai_keys":8,

        "aws_keys":8,

        "passwords":8,

        "api_keys":8
    }

    @classmethod
    def calculate(cls,detections):

        total=0

        for entity,data in detections.items():

            total+=cls.WEIGHTS.get(entity,1)*data["count"]

        if total<5:

            risk="Low"

        elif total<15:

            risk="Medium"

        else:

            risk="High"

        return {

            "score":total,

            "risk":risk

        }
import re

from classifier import RiskClassifier
from services.masking_service import MaskingService


class SensitiveDataDetector:

    PATTERNS={

        "emails":r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",

        "phones":r"(?:\+91[- ]?)?[6-9]\d{9}",

        "pan_numbers":r"[A-Z]{5}[0-9]{4}[A-Z]",

        "aadhaar_numbers":r"\b\d{4}\s\d{4}\s\d{4}\b",

        "credit_cards":r"\b(?:\d[ -]*?){13,16}\b",

        "bank_accounts":r"\b\d{9,18}\b",

        "ifsc_codes":r"\b[A-Z]{4}0[A-Z0-9]{6}\b",

        "employee_ids":r"\bEMP[-_]?\d+\b",

        "github_tokens":r"ghp_[A-Za-z0-9]{36}",

        "openai_keys":r"sk-[A-Za-z0-9]{20,}",

        "aws_keys":r"AKIA[0-9A-Z]{16}",

        "passwords":r"(?i)(?:password|passwd|pwd)\s*[:=]\s*[^\s]+",

        "api_keys":r"(?i)(?:api[_-]?key)\s*[:=]\s*[A-Za-z0-9_\-]+"

    }

    @staticmethod
    def detect(text):

        detections=[]

        grouped={}

        for entity,pattern in SensitiveDataDetector.PATTERNS.items():

            matches=list(set(re.findall(pattern,text)))

            grouped[entity]={

                "count":len(matches),

                "matches":matches

            }

            for match in matches:

                if entity=="emails":

                    masked=MaskingService.mask_email(match)

                elif entity=="phones":

                    masked=MaskingService.mask_phone(match)

                elif entity=="pan_numbers":

                    masked=MaskingService.mask_pan(match)

                elif entity=="aadhaar_numbers":

                    masked=MaskingService.mask_aadhaar(match)

                elif entity=="credit_cards":

                    masked=MaskingService.mask_card(match)

                else:

                    masked=MaskingService.default(match)

                detections.append({

                    "entity":entity,

                    "value":match,

                    "masked":masked,

                    "confidence":1.0

                })

        risk=RiskClassifier.calculate(grouped)

        return{

            "summary":{

                "total_sensitive_items":len(detections),

                "risk_score":risk["score"],

                "overall_risk":risk["risk"]

            },

            "detections":detections

        }
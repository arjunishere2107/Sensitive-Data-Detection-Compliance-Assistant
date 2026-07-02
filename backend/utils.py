import os


def create_directories():

    folders = [
        "uploads",
        "reports",
        "vector_db",
        "logs"
    ]

    for folder in folders:
        os.makedirs(folder, exist_ok=True)
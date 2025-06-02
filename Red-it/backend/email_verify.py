import requests


def email_verifier(email):
    api_key = "<your api key>"
    url = f"https://api.hunter.io/v2/email-verifier?email={email}&api_key={api_key}"
    response = requests.get(url)
    data = response.json()
    if 'data' in data: #If the email is valid. The data will contain the email and the result that email is valid
        return True
    else:
        return False

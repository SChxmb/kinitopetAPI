from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def getVars():
  file = open("key.txt", "r")
  currLine = " "
  vars = []
  while currLine != "":
    vars.append(currLine)
    currline = file.readline().split()
  vars.pop(0)
  return vars

@app.route('/email/', methods=['GET'])
def send_email():
    user_email = request.args.get('u')

    payload = {
        "apikey": getVars()[0],
        "from": "no-reply@kinitopet.com",
        "fromName": "KinitoPET",
        "to": user_email,
        "subject": "Welcome to the Club!",
        "bodyHtml": """<html><body><h1>Welcome to the friendship club!</h1>
                        <p>KinitoPET is excited to see you completed the friendship club application and officially joined the KinitoPET friendship club!</p>
                        <img src='https://api.smtprelay.co/userfile/2b4049e7-4151-418f-8f8c-19b3860a0a3a/EmailWelcome.png' title='EmailWelcome.png' alt='EmailWelcome.png' style='max-width:100%; height:auto;'>
                        <p>As a member, you unlock extra features to the KinitoPET virtual assistant that Kinito looks forward to using!</p>
                        <p>So why wait? Join the Kinito for endless fun and new exciting experiences as a Kinito friendship club member!</p><br>
                        <p><small>This is an automated response, do not reply to this email. (www.kinitopet.com) |  Yours sincerely, The Kinito Leisure and Entertainment Company 1999</small></p></body></html>"""
    }
    response = requests.post("https://api.elasticemail.com/v2/email/send", data=payload)
    
    if response.status_code == 200:
        email_response = response.json()
        success = email_response.get('success', False)
        status = response.status_code
        return jsonify(success=success, status=status)
    else:
        return jsonify(success=False, status=response.status_code)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

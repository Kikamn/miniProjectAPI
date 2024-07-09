import json

import requests
from datetime import datetime
from endpoint import WEBHOOK, URL_NETLIFY


# jalanin pytest -v -s setting/slack_notif.py di def pake test_(namaclass)
# jalnin python setting/slack_notif.py tidak pake test diclass tapi pake nama classname di akhir
def notif_slack():
    jsonContent = open("report_API_all.json", "r").read()
    dataJSON = json.loads(jsonContent)
    datetime_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #print(dataJSON.get("summary")) #untuk nampilin hasil test berdasarkan summary
    #print(dataJSON.get("summary")["passed"]) #nambahin paramater utk passednya berapa

    #testPassed = dataJSON.get("summary")["passed"]
    #testFailed = dataJSON.get("summary")["failed"] #Dikoment dulukarena gk ada failed
    #testTotal = dataJSON.get("summary")["total"]

    #print(testPassed)
    #print(testFailed)
    #print(testTotal)
    #print(WEBHOOK)
    try:
        testPassed = dataJSON.get("summary")["passed"]
    except:
        testPassed = "0"
    try:
        testFailed = dataJSON.get("summary")["failed"]
    except:
        testFailed = "0"
    try:
        testTotal = dataJSON.get("summary")["total"]
    except:
        testTotal = "0"

    #testSuces = float(testPassed)/float(testTotal) * 100 #untuk munculin jumlah pass dan faild
    testSuces = round(float(testPassed) / float(testTotal) * 100)

    if float(testFailed) >= 1: # jika test failed lebih dari 1
        color = "FF1E00" # Akan muncul Warna Merah
    else: #Maka klw tidak akan muncul
        color = "3CFF29" # Warna Hijau

    payload = {
        #"text": "Hello, Pytest!" # hrus bikin ini
        #"text": f"Test Passed: {testPassed}\n Test Total: {testTotal}" #dengan massage ini
        "attachments": [
        {
            "color": f"{color}",
            "blocks": [
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text",
                        "text": "API AUTOMATION",
                        "emoji": True
                    }
                },
                {
                    "type": "divider"
                },
                {
                    "type": "section",
                    "fields": [
                        {
                            "type": "mrkdwn",
                            "text": f"*Success Test:*\n {testPassed}"
                        },
                        {
                            "type": "mrkdwn",
                            "text": f"*Failed Test:*\n {testFailed}"
                        }
                    ]
                },
                {
                    "type": "section",
                    "fields": [
                        {
                            "type": "mrkdwn",
                            "text": "*Skipped Test:*\n0"
                        },
                        {
                            "type": "mrkdwn",
                            "text": f"*Total Test:*\n {testTotal}"
                        }
                    ]
                },
                {
                    "type": "section",
                    "fields": [
                        {
                            "type": "mrkdwn",
                            "text": f"*Success Rate:*\n {testSuces}%"
                        }
                    ]
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"<{URL_NETLIFY}/report_API.html|Link Report Test>"
                    }
                },
                {
                    "type": "divider"
                },
                {
                    "type": "rich_text",
                    "elements": [
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {
                                    "type": "text",
                                    "text": "tested by : Rizkika Mulya Ningsih",
                                    "style": {
                                        "italic": True
                                    }
                                }
                            ]
                        }
                    ]
                },
                {
                    "type": "rich_text",
                    "elements": [
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {
                                    "type": "text",
                                    "text": f"created at : {datetime_now}",  # untuk memuncul tangal hari ini
                                    "style": {
                                        "italic": True
                                    }
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    ]
    }

    req = requests.post(WEBHOOK, json=payload)  # untuk ngirim ke slack

notif_slack()
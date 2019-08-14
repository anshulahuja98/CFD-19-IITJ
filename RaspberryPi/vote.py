import RPi.GPIO as GPIO
import requests
import serial

ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)
headers = {
    'Content-Type': "application/json",
    'Authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6InU0T2ZORlBId0VCb3NIanRyYXVPYlY4NExuWSIsImtpZCI6InU0T2ZORlBId0VCb3NIanRyYXVPYlY4NExuWSJ9.eyJhdWQiOiI1MWMxODZkNy04ODViLTQxNDMtYWZhYS0yODc1OTZkNjg2OGUiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC8wODNiNmQ1Mi0zYzQ3LTRhMGYtOTg2ZC0zNmZkYjBkOWI0YWUvIiwiaWF0IjoxNTY1Nzc3MjQ0LCJuYmYiOjE1NjU3NzcyNDQsImV4cCI6MTU2NTc4MTE0NCwiYWlvIjoiQVNRQTIvOE1BQUFBL3Z0MjNLa2lUOHU2YS9ESDJYenpac3l0eTRWRmhoYXRlZThaWGR5L3VPaz0iLCJhbXIiOlsicHdkIl0sImNfaGFzaCI6ImpkRjY4a3B3RV9yYS1kUkRhVFdMMWciLCJpcGFkZHIiOiIxNC4xMzkuMzcuMTA4IiwibmFtZSI6IkNGRDIiLCJub25jZSI6ImIyOTA4OTRlLTlmYjMtNDk4Yy1iMDkzLTA4MTVlODE2ZDM0YSIsIm9pZCI6ImI5ZTVhNWMyLWNjZmYtNGQ0OS05M2NkLTM2YjU1NzgxZjIwYSIsInN1YiI6ImU4RnhoUllXWXhXVHItU09IVE45em9Nbzg4bkVfWXhXeFVHUE9rMjdweHMiLCJ0aWQiOiIwODNiNmQ1Mi0zYzQ3LTRhMGYtOTg2ZC0zNmZkYjBkOWI0YWUiLCJ1bmlxdWVfbmFtZSI6ImNmZDJAYWh1amEyaWl0amFjLm9ubWljcm9zb2Z0LmNvbSIsInVwbiI6ImNmZDJAYWh1amEyaWl0amFjLm9ubWljcm9zb2Z0LmNvbSIsInV0aSI6Inp2dDlHbnFlUFVXRXJEdHJqLUd4QUEiLCJ2ZXIiOiIxLjAifQ.RDPdyod1QnQSOBGVGrHdCefLoVwfyyn36qhtnyHT2UtWvEBmr4IvftrxMIxzP2-fw-yUZdFL0ZDSDlerwuRkNO6kZLSVjPZlUYnVwKYFUfdowlTdXzbfxvFQboedeykV-o6GfgoHf9E0Ph94LSlYFlxQ0Hba6SXYcJ0J24YubWpqcZx6qFL3Q7Q_ZgoWtD-PMgy0oqYX-QHDjZzNX2RubkB4xr0m1GG7q16dX-cQB-3_ubnE22tOk5XgTcKHK2imKbY3tZbjJIMomcS6WKw2rYbEdhMRBBuwTE400rZ39l3XgAOO3oOHIPdgH-2MA1FkberBoqrNkSndPr6HSEXI1A",
    'User-Agent': "PostmanRuntime/7.15.2",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "97798d86-a918-4f21-a284-8e69fd71e615,18983160-8229-46e0-960e-64cbe459ddf4",
    'Host': "cfd-7lizlp-api.azurewebsites.net",
    'Cookie': "ARRAffinity=ffc5a14e122a3e950d12cd97aa05445285bb2824918c5cf6531cdd92fea0dd08",
    'Accept-Encoding': "gzip, deflate",
    'Content-Length': "285",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
}

url = "https://cfd-7lizlp-api.azurewebsites.net/api/v1/contracts/8/actions"

while True:
    string = ser.read(12)
    if len(string) == 0:
        print("Please wave a tag")
    else:
        string = string[1:11]  # Strip header/trailer
        print("string", string)
        GPIO.setup(18, GPIO.OUT)
        GPIO.output(18, GPIO.HIGH)
        x = 10
        while x > 0:
            def button_11(channel):
                payload = "{\r\n  \"workflowFunctionID\": 23,\r\n  \"workflowActionParameters\": [\r\n    {\r\n      \"name\": \"CandidateID\",\r\n      \"value\": \"101\",\r\n      \"workflowFunctionParameterId\": 4\r\n    },\r\n    {\r\n      \"name\": \"finished\",\r\n      \"value\": \"False\",\r\n      \"workflowFunctionParameterId\": 4\r\n    }\r\n  ]\r\n}"
                response = requests.request("POST", url, data=payload, headers=headers)
                print(response.text)
                GPIO.output(18, GPIO.LOW)
                x = 1


            def button_12(channel):
                payload = "{\r\n  \"workflowFunctionID\": 23,\r\n  \"workflowActionParameters\": [\r\n    {\r\n      \"name\": \"CandidateID\",\r\n      \"value\": \"102\",\r\n      \"workflowFunctionParameterId\": 4\r\n    },\r\n    {\r\n      \"name\": \"finished\",\r\n      \"value\": \"False\",\r\n      \"workflowFunctionParameterId\": 4\r\n    }\r\n  ]\r\n}"
                response = requests.request("POST", url, data=payload, headers=headers)
                print(response.text)
                GPIO.output(18, GPIO.LOW)
                x = 2


            def button_13(channel):
                payload = "{\r\n  \"workflowFunctionID\": 23,\r\n  \"workflowActionParameters\": [\r\n    {\r\n      \"name\": \"CandidateID\",\r\n      \"value\": \"103\",\r\n      \"workflowFunctionParameterId\": 4\r\n    },\r\n    {\r\n      \"name\": \"finished\",\r\n      \"value\": \"False\",\r\n      \"workflowFunctionParameterId\": 4\r\n    }\r\n  ]\r\n}"
                response = requests.request("POST", url, data=payload, headers=headers)
                print(response.text)
                GPIO.output(18, GPIO.LOW)
                x = 3


            def button_15(channel):
                payload = "{\r\n  \"workflowFunctionID\": 23,\r\n  \"workflowActionParameters\": [\r\n    {\r\n      \"name\": \"CandidateID\",\r\n      \"value\": \"104\",\r\n      \"workflowFunctionParameterId\": 4\r\n    },\r\n    {\r\n      \"name\": \"finished\",\r\n      \"value\": \"False\",\r\n      \"workflowFunctionParameterId\": 4\r\n    }\r\n  ]\r\n}"
                response = requests.request("POST", url, data=payload, headers=headers)
                print(response.text)
                GPIO.output(18, GPIO.LOW)
                x = 4


            GPIO.setwarnings(False)
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
            GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
            GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
            GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

            GPIO.add_event_detect(11, GPIO.RISING, callback=button_12)
            GPIO.add_event_detect(12, GPIO.RISING, callback=button_12)
            GPIO.add_event_detect(13, GPIO.RISING, callback=button_13)
            GPIO.add_event_detect(15, GPIO.RISING, callback=button_15)
            message = input("Press enter to quit\n\n")

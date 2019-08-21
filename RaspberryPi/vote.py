import RPi.GPIO as GPIO
import requests
import serial
from subprocess import call

ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)

headers = {
    'Content-Type': "application/json",
    'Authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6ImllX3FXQ1hoWHh0MXpJRXN1NGM3YWNRVkduNCIsImtpZCI6ImllX3FXQ1hoWHh0MXpJRXN1NGM3YWNRVkduNCJ9.eyJhdWQiOiI1MWMxODZkNy04ODViLTQxNDMtYWZhYS0yODc1OTZkNjg2OGUiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC8wODNiNmQ1Mi0zYzQ3LTRhMGYtOTg2ZC0zNmZkYjBkOWI0YWUvIiwiaWF0IjoxNTY2MzI0NzIwLCJuYmYiOjE1NjYzMjQ3MjAsImV4cCI6MTU2NjMyODYyMCwiYWlvIjoiNDJGZ1lIaTRYSGRwdzliRjl6N3l0V2xjVlh5VW9jS2lFMTFab1NjUmFyNm1vV3VyZ1NBQSIsImFtciI6WyJwd2QiXSwiY19oYXNoIjoia3JWdlJUV21vX01yREJMalJoWDF0USIsImlwYWRkciI6IjE0LjEzOS4zNy4xMDgiLCJuYW1lIjoiQ0ZEMiIsIm5vbmNlIjoiZTg5MGU1MWMtMWFlMC00MGFiLWI2MTEtZTRlOGU5ZTY1N2UwIiwib2lkIjoiYjllNWE1YzItY2NmZi00ZDQ5LTkzY2QtMzZiNTU3ODFmMjBhIiwic3ViIjoiZThGeGhSWVdZeFdUci1TT0hUTjl6b01vODhuRV9ZeFd4VUdQT2syN3B4cyIsInRpZCI6IjA4M2I2ZDUyLTNjNDctNGEwZi05ODZkLTM2ZmRiMGQ5YjRhZSIsInVuaXF1ZV9uYW1lIjoiY2ZkMkBhaHVqYTJpaXRqYWMub25taWNyb3NvZnQuY29tIiwidXBuIjoiY2ZkMkBhaHVqYTJpaXRqYWMub25taWNyb3NvZnQuY29tIiwidXRpIjoiLVBNSkl5bUhkVXlMdTFfaGZscmhBQSIsInZlciI6IjEuMCJ9.rfFFCgTqv-yYD7yByioysJkhwBrojoxDFGOFpQPP_2I2yoQ1IRpie6XS-g1hjR0_teOd2MgIS8aUVlR7W7XmY1a5f8940sGxoeAsfzrFpIPTDeb9pXkSP1_TbU6j87WzQuc5EH_Lp4dSqJYSsCzY9gtprl4CvxNaS3qIiHZYWpeNfFlXHT2eIDtUqpfDcxMc26HqtachW9wkomSGMYSNV6NyJSQ25r9OsRBBFw6njHpWdzbzcvulrvpDLqMgNbV-YfHhzOhj3P-y14pkT8QmdaU5nyo8GP__OVd_xgznOhtn1MTFRzqjOOoxpB2R9D99cDtKXyg1Ye8ORXoRMxkonw",
    'User-Agent': "PostmanRuntime/7.15.2",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "15849eac-732a-4e5a-969c-1bc5a618766c,7f728c67-e402-44b9-9314-90b32951d22f",
    'Host': "cfd-7lizlp-api.azurewebsites.net",
    'Cookie': "ARRAffinity=ffc5a14e122a3e950d12cd97aa05445285bb2824918c5cf6531cdd92fea0dd08",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
}

url = "https://cfd-7lizlp-api.azurewebsites.net/api/v1/contracts/8/actions"
# string = ser.read(12)
# while True:
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)
GPIO.output(40, GPIO.HIGH)

def button_11(channel):
    payload = "{\r\n  \"workflowFunctionID\": 23,\r\n  \"workflowActionParameters\": [\r\n    {\r\n      \"name\": \"CandidateID\",\r\n      \"value\": \"101\",\r\n      \"workflowFunctionParameterId\": 4\r\n    },\r\n    {\r\n      \"name\": \"finished\",\r\n      \"value\": \"False\",\r\n      \"workflowFunctionParameterId\": 4\r\n    }\r\n  ]\r\n}"
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    print("Hi")
    GPIO.output(18, GPIO.LOW)
    call("sudo halt", shell=True)
    x = -1


def button_12(channel):
    payload = "{\r\n  \"workflowFunctionID\": 23,\r\n  \"workflowActionParameters\": [\r\n    {\r\n      \"name\": \"CandidateID\",\r\n      \"value\": \"102\",\r\n      \"workflowFunctionParameterId\": 4\r\n    },\r\n    {\r\n      \"name\": \"finished\",\r\n      \"value\": \"False\",\r\n      \"workflowFunctionParameterId\": 4\r\n    }\r\n  ]\r\n}"
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    GPIO.output(18, GPIO.LOW)
    call("sudo halt", shell=True)
    x = -2


def button_13(channel):
    payload = "{\r\n  \"workflowFunctionID\": 23,\r\n  \"workflowActionParameters\": [\r\n    {\r\n      \"name\": \"CandidateID\",\r\n      \"value\": \"103\",\r\n      \"workflowFunctionParameterId\": 4\r\n    },\r\n    {\r\n      \"name\": \"finished\",\r\n      \"value\": \"False\",\r\n      \"workflowFunctionParameterId\": 4\r\n    }\r\n  ]\r\n}"
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)

    GPIO.output(18, GPIO.LOW)
    call("sudo halt", shell=True)
    x = -3


def button_15(channel):
    payload = "{\r\n  \"workflowFunctionID\": 23,\r\n  \"workflowActionParameters\": [\r\n    {\r\n      \"name\": \"CandidateID\",\r\n      \"value\": \"104\",\r\n      \"workflowFunctionParameterId\": 4\r\n    },\r\n    {\r\n      \"name\": \"finished\",\r\n      \"value\": \"False\",\r\n      \"workflowFunctionParameterId\": 4\r\n    }\r\n  ]\r\n}"
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    GPIO.output(18, GPIO.LOW)
    call("sudo halt", shell=True)
    print("hello")
    x = -4


GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(11, GPIO.RISING, callback=button_11)
GPIO.add_event_detect(12, GPIO.RISING, callback=button_12)
GPIO.add_event_detect(13, GPIO.RISING, callback=button_13)
GPIO.add_event_detect(15, GPIO.RISING, callback=button_15)
# string = ser.read(12)

while True:
    string = ser.read(12)
    if len(string) == 0:
        print("Please wave a tag")

    else:
        x = 10
        # while x >=0:
        string = string[1:11]  # Strip header/trailer
        print("string", string)
        print("Light on")
        GPIO.setup(18, GPIO.OUT)
        GPIO.output(18, GPIO.HIGH)
        message = input("Press enter to quit\n\n")

    # string = ser.read(12)
#    print("11")

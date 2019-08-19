from flask import Flask, request, render_template
import sqlite3
import requests
app = Flask(__name__, static_url_path='', static_folder='static')


# with sqlite3.connect("earthquake_data.db") as con:


# cur = con.cursor()
# cur.execute("INSERT INTO Acceleration (X_dir,Y_dir,Z_dir)\
#           VALUES (?,?,?)", (1, 1, 1))
# con.commit()
# msg = "Record successfully added"


# @app.route('/post', methods=["POST"])
# def postJsonHandler():
#     data = request.get_json()
#     print(data)
#     latitude = data['latitude']
#     longitude = data['longitude']
#     ax = data['values'][0]
#     ay = data['values'][1]
#     az = data['values'][2]
#     print(ax, ay, az)
#     with sqlite3.connect("earthquake_data.db") as con:
#         print(ax, ay, az)
#         cur = con.cursor()
#         cur.execute("INSERT INTO Acceleration (X_dir,Y_dir,Z_dir)\
#                VALUES (?,?,?)", (ax, ay, az))
#         cur.execute("INSERT INTO Coordinates (latitude,longitude)\
#                    VALUES (?,?)", (latitude, longitude))

#         con.commit()
#         msg = "Record successfully added"
#     return ''


@app.route('/', methods=["GET"])
def get():
    return render_template('index.html')


# @app.route("/chart", methods=["GET"])
# def chart():
#     with sqlite3.connect("earthquake_data.db") as con:
#         cur = con.cursor()
#         cur.execute("SELECT * FROM Acceleration ")
#         rows = cur.fetchall()
#         print(rows)
#         labels = []
#         values = []
#         for row in rows:
#             values = values + [row[0], ]
#             labels = labels + [row[3], ]
#     return render_template('chart.html', values=values, labels=labels)

url = "https://cfd-7lizlp-api.azurewebsites.net/api/v1/contracts/8"

payload = ""
headers = {
    'Content-Type': "application/json",
    'Authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6ImllX3FXQ1hoWHh0MXpJRXN1NGM3YWNRVkduNCIsImtpZCI6ImllX3FXQ1hoWHh0MXpJRXN1NGM3YWNRVkduNCJ9.eyJhdWQiOiI1MWMxODZkNy04ODViLTQxNDMtYWZhYS0yODc1OTZkNjg2OGUiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC8wODNiNmQ1Mi0zYzQ3LTRhMGYtOTg2ZC0zNmZkYjBkOWI0YWUvIiwiaWF0IjoxNTY2MjQzMDY0LCJuYmYiOjE1NjYyNDMwNjQsImV4cCI6MTU2NjI0Njk2NCwiYWlvIjoiQVZRQXEvOE1BQUFBQTNnQ3ZpSmZ6dEdmbkc3M1JPcnpmU1BCelBQU0xiMjlTS0UzY3VqVTJMNWMzQjVGaUFLeThXKzI2eVpsbDZubnhQZm1MRHZ2OTl4U0dHVGVoaVh2Z3RvZmtwZFBIV0tCZmpLRTlKdm5QZU09IiwiYW1yIjpbInB3ZCJdLCJjX2hhc2giOiJPWXRNVzhobGpPUzNaQWpwdE5ieW1BIiwiZW1haWwiOiJhaHVqYS4yQGlpdGouYWMuaW4iLCJmYW1pbHlfbmFtZSI6ImU2YTkzODgxLWUzZTctNGVmOC05YTE2LWFiOTE3MjhiNTdmYiIsImdpdmVuX25hbWUiOiI5MjdhNjRlZS0wNDQ0LTQ2ODEtYWVjZC1hNGE0YjI3ZTc5ZTkiLCJpZHAiOiJsaXZlLmNvbSIsImlwYWRkciI6IjE0LjEzOS4zNy4xMDgiLCJuYW1lIjoiOTI3YTY0ZWUtMDQ0NC00NjgxLWFlY2QtYTRhNGIyN2U3OWU5IGU2YTkzODgxLWUzZTctNGVmOC05YTE2LWFiOTE3MjhiNTdmYiIsIm5vbmNlIjoiMDlhYjkxMGMtYjU2Yy00OGQ0LTliODgtYTI1NmRmYTFjY2M3Iiwib2lkIjoiZTQ1OWUzOTktNWVlZS00YTY3LTllZGMtZjY1MTIwMWRlYTc2Iiwicm9sZXMiOlsiQWRtaW5pc3RyYXRvciJdLCJzdWIiOiJkSmJOMWU1R1JhMzFiREpsT1dLT25vcUljV3dKUHVEYWdJMDFzWTRNR25vIiwidGlkIjoiMDgzYjZkNTItM2M0Ny00YTBmLTk4NmQtMzZmZGIwZDliNGFlIiwidW5pcXVlX25hbWUiOiJsaXZlLmNvbSNhaHVqYS4yQGlpdGouYWMuaW4iLCJ1dGkiOiIxTmx4ZWx6eE5FS0J5bzNKNDdUTUFBIiwidmVyIjoiMS4wIn0.pTr5BvsCtx_nN3QSbbukzoHvOx8tmlZKCqF7iOFE34SFS3ENC2TPOeGU-pTSlEs_3VvdWfVtUGGiVF_h4in8vh1gdxhlQPYojqSVjQjQTiXyVMubd9Xj_QmcpdAo5SvJMLUIZjKv8spLE4S1cY3vi1fVcDTrVExjcEBnw8K82x3Ap1T1LcaZmi88jgbNppIfaqI2Q_rRxnkgaMUanwSFk34vWn7psRX1Z5f5v0TXGwPzdz_yo0VFNXR1ip6XYRiPSWqOtxIVFo6awpKz7Kznb9q0wgwIlPwop-BSxYXSrTw8RZUZ-VQ5RXx3B0NmPHnFRM-HrYNwWLdBqRz2hoCTVg",
    'User-Agent': "PostmanRuntime/7.15.2",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "50eca28d-0379-4901-8780-4b3a29ed3010,d8a87e4d-a31b-49e9-9d39-fb65e2502353",
    'Host': "cfd-7lizlp-api.azurewebsites.net",
    'Cookie': "ARRAffinity=ffc5a14e122a3e950d12cd97aa05445285bb2824918c5cf6531cdd92fea0dd08",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
}


@app.route("/candidates", methods=["GET"])
def candidates():
    response = requests.request("GET", url, data=payload, headers=headers)
    response = response.json()
    x = response["contractActions"]
    candidateID = []
    for k in range(len(x)):
        z = x[k]
        if z['userId'] == 1:
            candidateID.append(z['parameters'][0]['value'])
    return render_template('candidate.html', candidateId=candidateID)

@app.route("/votes", methods=["GET"])
def votes():
    response = requests.request("GET", url, data=payload, headers=headers)
    response = response.json()
    x = response["contractActions"]
    candidateID = {}
    for k in range(len(x)):
        z = x[k]
        if z['userId'] == 1:
            candidateID[(z['parameters'][0]['value'])] = 0

    for kk in range(len(x)):
        if z['userId'] == 3:
            candidateID[(z['parameters'][0]['value'])] += 1
    return render_template('vote.html', candidateId=candidateID)


# @app.route("/maps", methods=["GET"])
# def maps():
#     with sqlite3.connect("earthquake_data.db") as con:
#         cur = con.cursor()
#         cur.execute("SELECT * FROM Acceleration ")
#         rows = cur.fetchall()
#         cur = con.cursor()
#         cur.execute("SELECT * FROM Coordinates ")
#         coord_rows = cur.fetchall()
#         print(rows)
#         print(coord_rows)
#         labels = []
#         values = []
#         for row in rows:
#             values = values + [row[0], ]
#             labels = labels + [row[3], ]
#         # for row in coord_rows:
#         # values = latitude + [coord_rows[0], ]
#         # labels = labels + [coord_rows[1], ]
#     return render_template('maps.html', values=values, labels=labels, coordinates=coord_rows)

app.run(host='0.0.0.0', port=9480, debug=True)

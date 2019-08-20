from flask import Flask, request, render_template
import sqlite3
import requests
import json
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
    'Authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6ImllX3FXQ1hoWHh0MXpJRXN1NGM3YWNRVkduNCIsImtpZCI6ImllX3FXQ1hoWHh0MXpJRXN1NGM3YWNRVkduNCJ9.eyJhdWQiOiI1MWMxODZkNy04ODViLTQxNDMtYWZhYS0yODc1OTZkNjg2OGUiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC8wODNiNmQ1Mi0zYzQ3LTRhMGYtOTg2ZC0zNmZkYjBkOWI0YWUvIiwiaWF0IjoxNTY2MzA1MjM0LCJuYmYiOjE1NjYzMDUyMzQsImV4cCI6MTU2NjMwOTEzNCwiYWlvIjoiQVZRQXEvOE1BQUFBeTQ0QzBkQXRBNmt0eGo4OXBYYUtNWGtHYVJaVE50c1BzdHVKWGhJaGFMdHFzcUF3TWhkRnp5RnM3YTNjUVlkQzduNDNDTVU0RmtyRk1saW90WGJpQXdaeDZ6Z0JnZDJ4dURZUDVFa1ZsbFk9IiwiYW1yIjpbInB3ZCJdLCJjX2hhc2giOiJNZXlQaGNmSGVrNTFTOUhyankyUjZ3IiwiZW1haWwiOiJhaHVqYS4yQGlpdGouYWMuaW4iLCJmYW1pbHlfbmFtZSI6ImU2YTkzODgxLWUzZTctNGVmOC05YTE2LWFiOTE3MjhiNTdmYiIsImdpdmVuX25hbWUiOiI5MjdhNjRlZS0wNDQ0LTQ2ODEtYWVjZC1hNGE0YjI3ZTc5ZTkiLCJpZHAiOiJsaXZlLmNvbSIsImlwYWRkciI6IjE0LjEzOS4zNy4xMDgiLCJuYW1lIjoiOTI3YTY0ZWUtMDQ0NC00NjgxLWFlY2QtYTRhNGIyN2U3OWU5IGU2YTkzODgxLWUzZTctNGVmOC05YTE2LWFiOTE3MjhiNTdmYiIsIm5vbmNlIjoiMjRhMTVmYmItMTMzNi00YWIyLTk1ODQtNzM4MGRhODIwOTJiIiwib2lkIjoiZTQ1OWUzOTktNWVlZS00YTY3LTllZGMtZjY1MTIwMWRlYTc2Iiwicm9sZXMiOlsiQWRtaW5pc3RyYXRvciJdLCJzdWIiOiJkSmJOMWU1R1JhMzFiREpsT1dLT25vcUljV3dKUHVEYWdJMDFzWTRNR25vIiwidGlkIjoiMDgzYjZkNTItM2M0Ny00YTBmLTk4NmQtMzZmZGIwZDliNGFlIiwidW5pcXVlX25hbWUiOiJsaXZlLmNvbSNhaHVqYS4yQGlpdGouYWMuaW4iLCJ1dGkiOiJrc2cwMzZTOTRFU044dGtDUENoSUFBIiwidmVyIjoiMS4wIn0.CJPIp8xDVlS2PoM-M14g4XfmdxoEC4OnHVerJzX8aw5U1YzAWeZepUJW8YeggFzwq-V2XLfeIM07AGJy-gdoS2ald88kFvLFFruJ78Thb9O16BQ3WMnr-3wCtwUe8dtfDCo6WhnRe5rN-ZAMzIYEutCuAL9y5EHw1PgRMeNsVleGkNH0JI-IrVJJl2aUteXH41MCkbc9w4E_3-J1tM1_LIaSZ6Kt6Ij08w1FMW8t26my_5vHLO8qj6duIgfnEleCmuvr-bwDGMJJa0kyGCRYSRTF0YpC-EBNiQbpJ3e7cjLObVDpCubXDm8M741VirizKSeq5M7bM62MFDEoMUnQoQ",
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
    return render_template('candidate.html', candidateID=candidateID)


@app.route("/votes", methods=["GET"])
def votes():
    response = requests.request("GET", url, data=payload, headers=headers)
    response = response.json()
    x = response["contractActions"]
    candidateID = {}
    total = 0
    for k in range(len(x)):
        z = x[k]
        if z['userId'] == 1:
            candidateID[(z['parameters'][0]['value'])] = 0

    for kk in range(len(x)):
        if z['userId'] == 3:
            candidateID[(z['parameters'][0]['value'])] += 1
            total += 1
    return render_template('vote.html', candidateID=candidateID, total=total)


@app.route("/info", methods=["GET"])
def info():
    with sqlite3.connect("candidateinfo.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Info")
        rows = cur.fetchall()

    return render_template('info.html', candidateInfo=rows)


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

app.run(host='0.0.0.0', port=9681, debug=True)

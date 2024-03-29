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


@app.route("/chart", methods=["GET"])
def chart():
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
    return render_template('chart.html', )


url = "https://cfd-7lizlp-api.azurewebsites.net/api/v1/contracts/8"

payload = ""
headers = {
    'Content-Type': "application/json",
    'Authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6ImllX3FXQ1hoWHh0MXpJRXN1NGM3YWNRVkduNCIsImtpZCI6ImllX3FXQ1hoWHh0MXpJRXN1NGM3YWNRVkduNCJ9.eyJhdWQiOiI1MWMxODZkNy04ODViLTQxNDMtYWZhYS0yODc1OTZkNjg2OGUiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC8wODNiNmQ1Mi0zYzQ3LTRhMGYtOTg2ZC0zNmZkYjBkOWI0YWUvIiwiaWF0IjoxNTY2MzgyNzc2LCJuYmYiOjE1NjYzODI3NzYsImV4cCI6MTU2NjM4NjY3NiwiYWlvIjoiQVZRQXEvOE1BQUFBSDh1U2JrSkVEVExPTy9yUGVsbnQ0ek5HbHRyUHJ6dUc3QnBaMFhtdUpHS3hZZ01zS2NwRlpNd2V2WjNJd3FMVjFkWUtwSS9WTG83c2xJcGRTZHJXUGVVVmJublJpc3p2TWI3aUZjbjlIaGc9IiwiYW1yIjpbInB3ZCJdLCJjX2hhc2giOiJPZGtPNTJoMEFxOHdXdUhoMUdFLVhRIiwiZW1haWwiOiJhaHVqYS4yQGlpdGouYWMuaW4iLCJmYW1pbHlfbmFtZSI6ImU2YTkzODgxLWUzZTctNGVmOC05YTE2LWFiOTE3MjhiNTdmYiIsImdpdmVuX25hbWUiOiI5MjdhNjRlZS0wNDQ0LTQ2ODEtYWVjZC1hNGE0YjI3ZTc5ZTkiLCJpZHAiOiJsaXZlLmNvbSIsImlwYWRkciI6IjE0LjEzOS4zNy4xMDgiLCJuYW1lIjoiOTI3YTY0ZWUtMDQ0NC00NjgxLWFlY2QtYTRhNGIyN2U3OWU5IGU2YTkzODgxLWUzZTctNGVmOC05YTE2LWFiOTE3MjhiNTdmYiIsIm5vbmNlIjoiZDYzNjE2OGEtZDFlYi00YmNhLTgzNGEtM2ExMmJkNzU3OGE0Iiwib2lkIjoiZTQ1OWUzOTktNWVlZS00YTY3LTllZGMtZjY1MTIwMWRlYTc2Iiwicm9sZXMiOlsiQWRtaW5pc3RyYXRvciJdLCJzdWIiOiJkSmJOMWU1R1JhMzFiREpsT1dLT25vcUljV3dKUHVEYWdJMDFzWTRNR25vIiwidGlkIjoiMDgzYjZkNTItM2M0Ny00YTBmLTk4NmQtMzZmZGIwZDliNGFlIiwidW5pcXVlX25hbWUiOiJsaXZlLmNvbSNhaHVqYS4yQGlpdGouYWMuaW4iLCJ1dGkiOiJIVnNYRVlBUEQwdUxZN2lUQklzbUFRIiwidmVyIjoiMS4wIn0.lPxTxjYEmT866eeo8Q1kmzElqpy5FnkFztMFwPBAPUgGeJpDd5fiNbf0mze7PfzuEMqyrzGnhFui82jPsoAIEOHFgauY5A_NSgQts6jOPXeFRzK2T8DDIsgszVWmtTSuxIP0LcRaapMVNj798PavO9-0F4CcrJnUOeJ0NqU-k1MrRxNJE8rJR2a2mKkWl0iexbrQCAKu5_ozE3Ul49PIcYxOERgGtuoYcNrwYMqlCbyUccHabS1ne3oE2mHtpmRFAa8hI3bRZAjVX4r8BzyvsUA3qxXkP4PTAo-Xm8SHT3yJ5KEzIcmli0GF99CBqMdmJFxMpxLvgrEW1a7wf_tEQA",
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


# @app.route("/candidates", methods=["GET"])
# def candidates():
#     response = requests.request("GET", url, data=payload, headers=headers)
#     response = response.json()
#     x = response["contractActions"]
#     candidateID = []
#     for k in range(len(x)):
#         z = x[k]
#         if z['userId'] == 1:
#             candidateID.append(z['parameters'][0]['value'])
#     return render_template('candidate.html', candidateID=candidateID)


@app.route("/votes", methods=["GET"])
def votes():
    response = requests.request("GET", url, data=payload, headers=headers)
    response = response.json()
    x = response["contractActions"]
    candidate_id = {}
    total_votes = 0
    for k in range(len(x)):
        z = x[k]
        if z['userId'] == 1:
            if len(z['parameters'][0]['value']) < 32:
                candidate_id[(z['parameters'][0]['value'])] = 0

    for kk in range(len(x)):
        z = x[kk]
        if z['userId'] == 3:
            if len(z['parameters'][0]['value']) < 32:
                candidate_id[(z['parameters'][0]['value'])] += 1
                total_votes += 1

    with sqlite3.connect("candidateinfo.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Info")
        rows = cur.fetchall()

    return render_template('votes.html', candidateID=candidate_id, total=total_votes, candidateInfo=rows)

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

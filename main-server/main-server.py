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

url = "https://cfd-7lizlp-api.azurewebsites.net/api/v1/contracts/8"


@app.route("/votes", methods=["GET"])
def votes():
    response = requests.request("GET", url, headers=headers)

    return render_template('chart.html', values=values, labels=labels)

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

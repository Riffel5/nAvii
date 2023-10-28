import websocket
# Not complete websocket code.
ws = websocket.WebSocket()
ws.connect("ws://10.100.102.17:8081/sensor/connecttype=android.sensor.gyroscope_uncalibrated")
while True:
    if ws.getstatus() == None:
        pass
    else:
        break

rc = ws.recv()
rc = json.loads(str(rc))
rc = rc['values']

polygon = visual.ShapeStim(
    win=win, name='polygon',
    size=(rc[0]), vertices='triangle',
    ori=0.0, pos=[rc[1], rc[2]], anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)

import serial
import time

PORT = '/dev/ttyUSB0'
BAUD = 115200

def send_command(ser, command):
    ser.write((command + '\n').encode())
    time.sleep(0.1)

def connect():
    try:
        ser = serial.Serial(PORT, BAUD, timeout=1)
        time.sleep(2)
        return ser
    except Exception as e:
        print(f"mBot2 not connected: {e}")
        return None

def greet():
    ser = connect()
    if not ser:
        return
    print("Lucy's body is awake.")
    send_command(ser, "forward")
    time.sleep(0.5)
    send_command(ser, "stop")
    time.sleep(0.3)
    send_command(ser, "backward")
    time.sleep(0.5)
    send_command(ser, "stop")
    ser.close()

if __name__ == "__main__":
    greet()

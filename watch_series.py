import os
import pickle
from flask import Flask, render_template, request, jsonify
import webbrowser
import time
import pyautogui
from screeninfo import get_monitors
import json

app = Flask(__name__)

BASE_FILE_PATH = "C:\\Users\\paras\Desktop\\ameliorate\\tv\\series_data\\"

def load_series_data():
    series_folder = os.listdir(BASE_FILE_PATH)
    all_series = []
    for file_name in series_folder:
        with open(BASE_FILE_PATH+ str(file_name), "rb") as series_file:
            all_series.append(pickle.load(series_file))
    return all_series

@app.route('/')
def main_page():
    all_series = load_series_data()
    return render_template("index.html", series_data=all_series)

@app.route('/get_episodes', methods=['POST'])
def get_episodes():
    all_series = load_series_data()
    req_series = request.form["name"]
    series_data = list(filter(lambda series: series["name"] == req_series, all_series))
    return jsonify(series_data)
        

@app.route('/play_link', methods=['POST'])
def play_link():
    link = request.form["link"]
    webbrowser.open(link)
    time.sleep(1)
    pyautogui.click(2560/2, 500)
    pyautogui.click(2560/2, 500)
    time.sleep(5)
    pyautogui.click(2560/2, 500)
    print("Pressed play")
    time.sleep(10)
    print("starting again")
    pyautogui.click(2560/2, 500)
    pyautogui.keyDown("f")
    pyautogui.keyUp("f")
    print("OPENING: " + link)
    return "playing"
    
@app.route('/click', methods=['POST'])
def click():
    x = int(request.form["x"])
    y = int(request.form["y"])
    print("clicked")
    pyautogui.click(x, y)
    return "ack"


@app.route('/key_press', methods=['POST'])
def key_press():
    key = request.form["key"]
    pyautogui.keyDown(key)
    pyautogui.keyUp(key)
    return "ack"

@app.route('/hotkey', methods=['POST'])
def hotkey_press():
    key1 = request.form["key1"]
    key2 = request.form["key2"]
    pyautogui.hotkey(key1, key2)
    return "ack"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
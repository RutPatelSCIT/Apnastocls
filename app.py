from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

# Path to the Excel file
EXCEL_FILE = "data.xlsx"

def read_excel():
    if os.path.exists(EXCEL_FILE):
        df = pd.read_excel(EXCEL_FILE)
        return df.to_dict(orient='records')
    return []

@app.route('/')
def index():
    data = read_excel()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)

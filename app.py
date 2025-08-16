from flask import Flask, render_template
import os
import pandas as pd

# サーバーでの画像出力用（GUI不要のバックエンド）
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt

app = Flask(__name__)

@app.route("/")
def hello():
    return "Flask is running on EC2!"

@app.route("/report")
def report():
    # CSV読み込み
    csv_path = os.path.join(os.path.dirname(__file__), "data", "report_sample.csv")
    df = pd.read_csv(csv_path, encoding="utf-8-sig", parse_dates=["date"])

    # 集計
    by_status = df["status"].value_counts().to_dict()
    by_tag = df["tag"].value_counts().to_dict()

    # グラフ生成（static/へ保存）
    os.makedirs("static", exist_ok=True)
    fig = plt.figure()
    plt.bar(list(by_status.keys()), list(by_status.values()))
    plt.title("Tasks by Status")
    plt.xlabel("status")
    plt.ylabel("count")
    out_path = os.path.join("static", "report_status.png")
    fig.savefig(out_path, bbox_inches="tight")
    plt.close(fig)

    return render_template(
        "report.html",
        by_status=by_status,
        by_tag=by_tag,
        chart_url="/static/report_status.png",
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

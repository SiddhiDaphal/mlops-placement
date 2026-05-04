import pandas as pd
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

def generate_report():
    df = pd.read_csv("data/placement.csv")

    ref = df.sample(frac=0.5, random_state=1)
    curr = df.drop(ref.index)

    report = Report(metrics=[DataDriftPreset()])
    report.run(reference_data=ref, current_data=curr)

    report.save_html("report.html")

if __name__ == "__main__":
    generate_report()
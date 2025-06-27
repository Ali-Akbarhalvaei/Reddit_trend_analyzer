# Orchestrate the Project
import json
from datetime import datetime
from src.trend_discovery.reddit_trends import get_reddit_trends
from src.Analysis.llm import analyze_trend


def run_workflow():

    try:
        trends = get_reddit_trends(limit=3)
        if not trends:
            print(" - Workflow failed: Could not fetch trends from Reddit. Exiting.")
            return
    except Exception as e:
        print(f"An Error Occured during the Process {e}")
        return

    print(f"Successfully {len(trends)}  trends title have been found")
    print("-" * 15)
    print("\n Analyzing started.....")

    all_analyses = []

    for i, trend in enumerate(trends, 1):
        title = trend["title"]
        print(f"analysing trend {i}/{len(trends)}, Title: {title}....\n")

        analysis = analyze_trend(title)
        if analysis:
            combined_result = {"source_data": trend, "analysis": analysis}
            all_analyses.append(combined_result)
        else:
            print(f"could not analyse the trend : {title}")

    if not all_analyses:
        print("   - Workflow failed: No trends were successfully analyzed. Exiting.")
        return

    print("-" * 15)
    print("\n Saving the final report.......\n")

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_filename = f"trend_report{timestamp}.json"

    try:
        with open(report_filename, "w", encoding="utf-8") as f:
            json.dump(all_analyses, f, indent=2, ensure_ascii=False)
        print(f" report {report_filename} has been successfully saved")
    except Exception as e:
        print(f"   - Error: Failed to save the report. Reason: {e}")

    print("\n✅ Workflow Complete!")


if __name__ == "__main__":
    run_workflow()

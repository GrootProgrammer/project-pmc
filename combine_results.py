import json
import os

results = {}

print(os.listdir("results"))

for file in os.listdir("results"):
    if file.endswith(".json") and file != "time_results.json":
        with open(f"results/{file}", "r") as f:
            results[file] = json.load(f)

time_results = {}

for file in results:
    for model in results[file]:
        if model not in time_results:
            time_results[model] = {}
        for algorithm in results[file][model]:
            if algorithm == "exact":
                continue
            try:
                if any([results[file][model][algorithm][r]["result_type"] == "timeout" or results[file][model][algorithm][r]["result_type"] == "error" for r in results[file][model][algorithm] if r != "total_time"]):
                    time_results[model][algorithm] = 600
                    continue
                time_results[model][algorithm] = results[file][model][algorithm]["total_time"]
            except Exception as e:
                print(f"Error: {e}")
                print(f"File: {file}")
                print(f"Model: {model}")
                print(f"Algorithm: {algorithm}")
                print(f"Results: {results[file][model][algorithm]}")
                continue

time_results = {k: v for k, v in time_results.items() if len(v) > 0}
print(time_results)
json.dump(time_results, open("results/time_results.json", "w"), indent=4)
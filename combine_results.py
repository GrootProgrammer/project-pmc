import json
import os

results = {}

print(os.listdir("results"))

for file in os.listdir("results"):
    if file.endswith(".json") and file != "time_results.json" and file != "good_results.json":
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
                bad = ["timeout", "error", "not_supported"]
                if any([results[file][model][algorithm][r]["result_type"] in bad for r in results[file][model][algorithm] if r != "total_time"]):
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

good_results = {}

for file in results:
    for model in results[file]:
        if model not in good_results:
            good_results[model] = {}
        for algorithm in results[file][model]:
            if algorithm == "exact":
                continue
            try:
                if any([results[file][model][algorithm][r]["result_type"] in ["not_supported"] for r in results[file][model][algorithm] if r != "total_time"]):
                    good_results[model][algorithm] = "not supported"
                    continue
                if any([results[file][model][algorithm][r]["result_type"] in ["error"] for r in results[file][model][algorithm] if r != "total_time"]):
                    good_results[model][algorithm] = "error"
                    continue
                if any([results[file][model][algorithm][r]["result_type"] in ["timeout"] for r in results[file][model][algorithm] if r != "total_time"]):
                    good_results[model][algorithm] = "timeout"
                    continue
                good_results[model][algorithm] = results[file][model][algorithm]["total_time"]
            except Exception as e:
                print(f"Error: {e}")
                print(f"File: {file}")
                print(f"Model: {model}")
                print(f"Algorithm: {algorithm}")
                print(f"Results: {results[file][model][algorithm]}")
                continue

good_results = [{"model": k} | v for k, v in good_results.items()]

print(time_results)
json.dump(time_results, open("results/time_results.json", "w"), indent=4)
json.dump(good_results, open("results/good_results.json", "w"), indent=4)
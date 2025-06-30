import json
import matplotlib.pyplot as plt

time_results = json.load(open("results/time_results.json", "r"))

model_averages = {}

for model in time_results:
    average_time = sum(time_results[model].values()) / len(time_results[model])
    model_averages[model] = average_time

results = []
for model in sorted(model_averages, key=lambda x: model_averages[x]):
    results_t = []
    for algorithm in time_results[model]:
        results_t.append(time_results[model][algorithm])
    results.append(results_t)

def plot_specific_results(index, label):
    plt.clf()
    plt.plot(sorted(model_averages, key=lambda x: model_averages[x]), [results[index] for results in results], marker="o", label=label)
    plt.yscale("log")
    plt.xlabel("Model")
    plt.ylabel("Time")
    plt.title("Time taken to check models")

    plt.legend()
    plt.xticks(rotation=90)
    plt.savefig(f"results/time_results_{label}.png")

for i, algorithm in enumerate(time_results["beb"].keys()):
    plot_specific_results(i, algorithm)

def plot_all_results():
    plt.clf()
    plt.plot(sorted(model_averages, key=lambda x: model_averages[x]), results, marker="o", label=time_results["beb"].keys())
    plt.yscale("log")
    plt.xlabel("Model")
    plt.ylabel("Time")
    plt.title("Time taken to check models")

    plt.legend()
    plt.xticks(rotation=90)
    plt.savefig(f"results/time_results_all.png")

plot_all_results()
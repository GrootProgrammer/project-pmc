import json
import matplotlib.pyplot as plt
import numpy as np

time_results = json.load(open("results/time_results.json", "r"))

# Get all unique algorithms from all models
all_algorithms = set()
for model in time_results:
    all_algorithms.update(time_results[model].keys())
algorithms = sorted(list(all_algorithms))

# Sort models by their average time
model_averages = {}
for model in time_results:
    valid_times = [v for v in time_results[model].values() if isinstance(v, (int, float)) and v != 600]
    if valid_times:
        average_time = sum(valid_times) / len(valid_times)
    else:
        average_time = 600  # Default for models with no valid times
    model_averages[model] = average_time

sorted_models = sorted(model_averages, key=lambda x: model_averages[x])

# Prepare data for plotting
plot_data = {}
for alg in algorithms:
    plot_data[alg] = []
    for model in sorted_models:
        if alg in time_results[model]:
            value = time_results[model][alg]
            # Handle timeout values (600 seconds)
            if value == 600:
                plot_data[alg].append(600)
            else:
                plot_data[alg].append(value)
        else:
            plot_data[alg].append(None)

def plot_specific_results(algorithm):
    plt.clf()
    values = plot_data[algorithm]
    valid_indices = [i for i, v in enumerate(values) if v is not None]
    valid_values = [v for v in values if v is not None]
    
    plt.plot([sorted_models[i] for i in valid_indices], valid_values, marker="o", label=algorithm)
    plt.yscale("log")
    plt.xlabel("Model")
    plt.ylabel("Time (seconds)")
    plt.title(f"Time taken to check models - {algorithm}")
    
    plt.legend()
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(f"results/time_results_{algorithm}.png", bbox_inches='tight', dpi=200)
    plt.close()

# Plot individual algorithm results
for algorithm in algorithms:
    plot_specific_results(algorithm)

def plot_all_results():
    plt.clf()
    
    for algorithm in algorithms:
        values = plot_data[algorithm]
        valid_indices = [i for i, v in enumerate(values) if v is not None]
        valid_values = [v for v in values if v is not None]
        
        if valid_values:  # Only plot if there are valid values
            plt.plot([sorted_models[i] for i in valid_indices], valid_values, 
                    marker="o", label=algorithm, linewidth=2, markersize=6, alpha=0.75)
    
    plt.yscale("log")
    plt.xlabel("Model")
    plt.ylabel("Time (seconds)")
    plt.title("Time taken to check models - All algorithms")
    
    plt.legend()
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig("results/time_results_all.png", bbox_inches='tight', dpi=200)
    plt.close()

plot_all_results()
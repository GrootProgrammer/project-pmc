import json
import sys
import os
import subprocess

import argparse

from program import PropertyResult, PropertyResultType

def test():
    info = {
        "beb": {
            "args": {
                "H": "3",
                "K": "4",
                "N": "3"
            },
            "results": {
                "LineSeized": "0.9166259765625",
                "GaveUp": "0.0833740234375"
            }
        },
        "blocksworld": {
            "args": {
                "n": "5"
            },
            "results": {
                "goal": "1"
            }
        },
        "cdrive": {
            "args": {
                "c": "6"
            },
            "results": {
                "goal": "0.6070826102773691"
            }
        },
        "consensus": {
           "args": {
                "N": "4",
                "K": "2"
            },
            "results": {
                "c1": "1.0",
                "c2": "0.3173828125",
                "disagree": "0.29443185428958624",
                "steps_max": "363",
                "steps_min": "192"
            }
        },
        "csma": {
            "args": {
                "N": "2",
                "K": "2"
            },
            "results": {
                "all_before_max": "0.875",
                "all_before_min": "0.875",
                "some_before": "0.5",
                "time_max": "70.66575976616393",
                "time_min": "66.99932286267479"
            }
        },
        "eajs": {
            "args": {
                "N": "2",
                "energy_capacity": "100",
                "B": "5"
            },
            "results": {
                "ExpUtil": "4.028044505410761"
            }
        },
        "echoring": {
            "args": {
                "ITERATIONS": "2"
            },
            "results": {
                "MinFailed": "2.9528259735546e-7",
                "MinOffline1": "2.4103690055658e-7",
                "MaxOffline1": "2.4103690055658e-7",
                "MinOffline2": "2.785589832249e-8",
                "MaxOffline2": "2.785589832249e-8",
                "MinOffline3": "2.638979847639e-8",
                "MaxOffline3": "2.638979847639e-8",
            }
        },
        "elevators": {
            "args": {
                "variant": "a",
                "p": "3",
                "c": "3"
            },
            "results": {
                "goal": "1"
            }
        },
        "exploding-blocksworld": {
            "args": {
                "N": "5",
            },
            "results": {
                "goal": "0.9"
            }
        },
        "firewire": {
            "args": {
                "explicit_timer": "false",
                "delay": "3",
                "deadline": "200"
            },
            "results": {
                "elected": "1.0",
                "time_max": "299",
                "time_min": "138.25",
                "time_sending": "18"
                # "deadline": "0.5"
            }
        },
        "firewire_abst": {
            "args": {
                "delay": "36",
            },
            "results": {
                "rounds": "1.0",
                "time_max": "365",
                "time_min": "102.25"
            }
        },
        "firewire_dl": {
            "args": {
                "delay": "3",
                "deadline": "200"
            },
            "results": {
                "deadline": "0.5"
            }
        },
        # TODO: this model gives 0.5 rather than 1.0 on all implementations
        # "ij": {
        #     "args": {
        #         "num_tokens_var": "10"
        #     },
        #     "results": {
        #         "stable": "1"
        #     }
        # },
        "pacman": {
            "args": {
                "MAXSTEPS": "5"
            },
            "results": {
                "crash": "0.5511"
            }
        },
        "philosophers-mdp": {
            "args": {
                "N": "3"
            },
            "results": {
                "eat": "1"
            }
        },
        "pnueli-zuck": {
            "args": {
                "N": "3"
            },
            "results": {
                "live": "1"
            }
        },
        "rabin": {
            "args": {
                "N": "3"
            },
            "results": {
                "live": "1"
            }
        },
        "rectangle-tireworld": {
            "args": {
                "xy": "5"
            },
            "results": {
                "goal": "1"
            }
        },
        # NOTE: this model fails parsing by modest
        # "resource-gathering": {
        #     "args": {
        #         "B": "200",
        #         "GOLD_TO_COLLECT": "15",
        #         "GEM_TO_COLLECT": "15"
        #     },
        #     "results": {
        #         "expgold": "22.07144159280847",
        #         "expsteps": "193.88888888888889",
        #         "prgoldgem":"0.8080456033115208"
        #     }
        # },
        "tireworld": {
            "args": {
                "n": "17"
            },
            "results": {
                "goal": "0.23328"
            }
        },
        "triangle-tireworld": {
            "args": {
                "l": "9"
            },
            "results": {
                "goal": "1"
            }
        },
        "wlan": {
            "args": {
                "MAX_BACKOFF": "0",
                "COL": "0"
            },
            "results": {
                "collisions": "1",
                "cost_max": "28000.956937799045",
                "cost_min": "7625",
                "num_collisions": "1.2248803827751196",
                "time_max": "3791.904761904762",
                "time_min": "1325"
            }
        },
        "wlan_dl": {
            "args": {
                "MAX_BACKOFF": "0",
                "deadline": "80",
            },
            "results": {
                "deadline": "0.81640625"
            }
        },
        "zenotravel": {
            "args": {
                "c": "4",
                "p": "2",
                "a": "2"
            },
            "results": {
                "goal": "1.0",
            }
        },
        "zeroconf": {
            "args": {
                "N": "20",
                "K": "2",
                "reset": "true"
            },
            "results": {
                "correct_max": "0.000020103281776956928",
                "correct_min": "0.000002110327218406747"
            }
        },
        "zeroconf_dl": {
            "args": {
                "N": "1000",
                "K": "1",
                "reset": "true",
                "deadline": "10"
            },
            "results": {
                "deadline_max": "0.015378937007874016",
                "deadline_min": "0.001424816450729849"
            }
        }
    }

    parser = argparse.ArgumentParser()
    parser.add_argument("--modest-path", type=str, default="modest")
    parser.add_argument("--algorithms", type=str, default="vi,smt")
    parser.add_argument("--timeout", type=int, default=600)
    parser.add_argument("--parallel", action="store_true")
    parser.add_argument("--only", type=str, default=None)
    parser.add_argument("--output", type=str, default=None)
    args = parser.parse_args()

    output_info = {}

    def download_model(k, v):
        if not os.path.exists(f"test-files/{k}.py"):
            args_text = ",".join([f"{k}={v}" for k, v in v["args"].items()])
            cmd = [args.modest_path, "export-to-python", "qcomp://" + k, "-E", args_text, "--output", f"test-files/{k}.py"]
            env = os.environ.copy()
            output = subprocess.run(cmd, capture_output=True, text=True, check=True,env=env)
            for line in output.stdout.splitlines():
                print("\t" + line)
            for line in output.stderr.splitlines():
                print("\t" + line)

    for k, v in info.items():
        if args.only and k != args.only:
            continue
        download_model(k, v)

    def run_model(k,v,algorithm):
        import time
        timer = time.time()
        cmd = ["python3", "src/model_checker/main.py", "--python-model", f"test-files/{k}.py", "check", "--json-output", "--algorithm", algorithm, "--smt-timeout", str(int(args.timeout/len(v["results"])))]
        try:
            output = subprocess.run(cmd, capture_output=True, text=True, timeout=args.timeout)
        except subprocess.TimeoutExpired:
            print(f"\t\ttimeout running {cmd}")
            for result in v["results"]:
                output_info[k][algorithm][result] = PropertyResult(PropertyResultType.TIMEOUT, None, args.timeout)
            output_info[k][algorithm]["total_time"] = args.timeout
            return
        if output.returncode != 0:
            print(f"\t\terror running {cmd}:")
            for line in output.stdout.splitlines():
                print("\t\t\t" + line)
            for line in output.stderr.splitlines():
                print("\t\t\t" + line)
            for r in v["results"]:
                output_info[k][algorithm][r] = PropertyResult(PropertyResultType.ERROR, None, args.timeout)
            output_info[k][algorithm]["total_time"] = args.timeout
            return
        import json
        results = json.loads(output.stdout)
        results = {prop: PropertyResult.from_dict(r) for prop, r in results.items()}
        output_info[k][algorithm] = results
        output_info[k][algorithm]["total_time"] = time.time() - timer

    def run_models():
        if args.parallel:
            threads = {}
        for k, v in info.items():
            if args.only and k != args.only:
                continue
            output_info[k] = {}
            if args.parallel:
                import threading
                for algorithm in args.algorithms.split(","):
                    output_info[k][algorithm] = {}
                    threads[k] = (threading.Thread(target=run_model, args=(k,v,algorithm)))
                    threads[k].start()
            else:
                print(f"testing {k}", flush=True)
                print("\tanswer:")
                output_info[k]["exact"] = {}
                for result in v["results"]:
                    print(f"\t\t{result}: {v['results'][result]}")
                    output_info[k]["exact"][result] = v["results"][result]
                for algorithm in args.algorithms.split(","):
                    output_info[k][algorithm] = {}
                    print(f"\t{algorithm}:")
                    run_model(k,v,algorithm)
                    for result in v["results"]:
                        if result not in output_info[k][algorithm]:
                            # this happens if modest does not support the property
                            output_info[k][algorithm][result] = PropertyResult(PropertyResultType.NOT_SUPPORTED, None, 0)
                        print(f"\t\t{result}: {output_info[k][algorithm][result]} (time: {output_info[k][algorithm][result].time:.2f}s)")
    
        if args.parallel:
            for k, v in info.items():
                if args.only and k != args.only:
                    continue
                threads[k].join()
                print(f"testing {k}", flush=True)
                print("\tanswer:")
                output_info[k]["exact"] = {}
                for result in v["results"]:
                    print(f"\t\t{result}: {v['results'][result]}")
                    output_info[k]["exact"][result] = v["results"][result]
                for algorithm in args.algorithms.split(","):
                    print(f"\t{algorithm}:")
                    for result in v["results"]:
                        if result not in output_info[k][algorithm]:
                            # this happens if modest does not support the property
                            output_info[k][algorithm][result] = PropertyResult(PropertyResultType.NOT_SUPPORTED, None, 0)
                        print(f"\t\t{result}: {output_info[k][algorithm][result]} (time: {output_info[k][algorithm][result].time:.2f}s)")

    run_models()
    # print(output_info)
    # success = True
    for k, v in output_info.items():
        for algorithm in v:
            if algorithm == "exact":
                continue
            for result in v[algorithm]:
                if result == "total_time":
                    continue
                result_value = v[algorithm][result]
                if result_value.result_type != PropertyResultType.FLOAT:
                    continue
                result_value = result_value.result
                exact_value = float(v["exact"][result])
                if abs(exact_value - result_value) > 0.001:
                    output_info[k][algorithm][result] = PropertyResult(PropertyResultType.INCORRECT_FLOAT, result_value, v[algorithm][result].time)
                    print(f"incorrect on {k} with {algorithm} with property {result}: {result_value} instead of {exact_value}")
                    # success = False
    # if not success:
    #     exit(1)
    if args.output:
        with open(args.output, "w") as f:
            # Convert PropertyResult objects to dictionaries for JSON serialization
            serializable_output = {}
            for model_key, model_data in output_info.items():
                serializable_output[model_key] = {}
                for algorithm_key, algorithm_data in model_data.items():
                    serializable_output[model_key][algorithm_key] = {}
                    for result_key, result_value in algorithm_data.items():
                        if result_key not in output_info[model_key]["exact"]:
                            continue
                        if isinstance(result_value, PropertyResult):
                            serializable_output[model_key][algorithm_key][result_key] = result_value.to_dict()
                        else:
                            serializable_output[model_key][algorithm_key][result_key] = result_value
            
            json.dump(serializable_output, f, indent=4)

if __name__ == "__main__":
    test()
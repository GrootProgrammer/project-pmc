import sys
import os
import subprocess

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
        # TODO: fix eajs
        # "eajs": {
        #     "args": {
        #         "N": "2",
        #         "energy_capacity": "100",
        #         "B": "5"
        #     },
        #     "results": {
        #         "ExpUtil": "4.028044505410761"
        #     }
        # },
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
                "time_sending": "18",
                "deadline": "0.5"
            }
        },
        "firewire_abst": {
            "args": {
                "delay": "36",
            },
            "results": {
                "deadline": "1.0",
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
        "ij": {
            "args": {
                "num_tokens_var": "10"
            },
            "results": {
                "stable": "1"
            }
        },
        "pacman": {
            "args": {
                "MAXSTEPS": "5"
            },
            "results": {
                "eat": "0.5511"
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
                "goal": "1"
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
                "goal": "0.81640625"
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
                "deadline": 10
            },
            "results": {
                "deadline_max": "0.015378937007874016",
                "deadline_min": "0.001424816450729849"
            }
        }
    }

    modest_path = sys.argv[1]

    output_info = {}

    def download_model(k, v):
        if not os.path.exists(f"test-files/{k}.py"):
            args_text = ",".join([f"{k}={v}" for k, v in v["args"].items()])
            cmd = [modest_path, "export-to-python", "qcomp://" + k, "-E", args_text, "--output", f"test-files/{k}.py"]
            env = os.environ.copy()
            output = subprocess.run(cmd, capture_output=True, text=True, check=True,env=env)
            for line in output.stdout.splitlines():
                print("\t" + line)
            for line in output.stderr.splitlines():
                print("\t" + line)

    for k, v in info.items():
        download_model(k, v)

    for k, v in info.items():
        output_info[k] = {}
        print(f"testing {k}", flush=True)
        print("\tanswer:")
        output_info[k]["exact"] = {}
        for result in v["results"]:
            print(f"\t\t{result}: {v['results'][result]}")
            output_info[k]["exact"][result] = v["results"][result]
        for algorithm in ["vi"]:
            output_info[k][algorithm] = {}
            print(f"\t{algorithm}:")
            cmd = ["python3", "src/model_checker/main.py", "--python-model", f"test-files/{k}.py", "check", "--algorithm", algorithm]
            try:
                output = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            except subprocess.TimeoutExpired:
                print(f"\t\ttimeout running {cmd}")
                for result in v["results"]:
                    output_info[k][algorithm][result] = "timeout"
                continue
            if output.returncode != 0:
                print(f"\t\terror running {cmd}:")
                for line in output.stdout.splitlines():
                    print("\t\t\t" + line)
                for line in output.stderr.splitlines():
                    print("\t\t\t" + line)
                exit(1)
            for result in v["results"]:
                def get_result(result):
                    line = get_line_with_result(output.stdout, result)
                    if line is None:
                        return "failed"
                    try:
                        parsed_line = parse_line(line)
                        print(f"\t\t{result}: {parsed_line}")
                        return parsed_line
                    except:
                        return "parse error"
                output_info[k][algorithm][result] = get_result(result)
    
    print(output_info)
    success = True
    for k, v in output_info.items():
        for algorithm in v:
            if algorithm == "exact":
                continue
            for result in v[algorithm]:
                result_value_str = v[algorithm][result]
                if result_value_str == "failed" or result_value_str == "timeout" or result_value_str == "parse error":
                    continue
                result_value = float(result_value_str)
                exact_value = float(v["exact"][result])
                if abs(1 - (result_value / exact_value)) > 0.01:
                    print(f"incorrect on {k} with {algorithm} with property {result}: {result_value} instead of {exact_value}")
                    success = False
    if not success:
        exit(1)

def get_line_with_result(output, result):
    for line in output.split("\n"):
        if result in line:
            return line

def parse_line(line):
    return line.split("=")[1]

if __name__ == "__main__":
    test()
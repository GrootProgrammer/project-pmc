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

    for k, v in info.items():
        output_info[k] = {}
        print(f"testing {k}", flush=True)

        if not os.path.exists(f"test-files/{k}.py"):
            args_text = ",".join([f"{k}={v}" for k, v in v["args"].items()])
            cmd = [modest_path, "export-to-python", "qcomp://" + k, "-E", args_text, "--output", f"test-files/{k}.py"]
            env = os.environ.copy()
            output = subprocess.run(cmd, capture_output=True, text=True, check=True,env=env)
            for line in output.stdout.splitlines():
                print("\t" + line)
        
        print("\tanswer:")
        for result in v["results"]:
            print(f"\t\t{result}: {v['results'][result]}")
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
                output_info[k][algorithm]["exact"] = v["results"][result]
    print(output_info)

def get_line_with_result(output, result):
    for line in output.split("\n"):
        if result in line:
            return line

def parse_line(line):
    return line.split("=")[1]

if __name__ == "__main__":
    test()
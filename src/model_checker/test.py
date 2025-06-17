import sys
import os
import subprocess

def test():
    sucess = True
    info = {
        "blocksworld": {
            "args": {
                "n": "5"
            },
            "results": {
                "goal": "1"
            }
        },
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
        "breakdown-queues": {
            "args": {
                "K": "8"
            },
            "results": {
                "Min": "0.02800482792035489",
                "Max": "0.23177396051702714"
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
        }
    }

    modest_path = sys.argv[1]

    for k, v in info.items():
        print(f"testing {k}")

        if not os.path.exists(f"examples/{k}.py"):
            args_text = ",".join([f"{k}={v}" for k, v in v["args"].items()])
            cmd = [modest_path, "export-to-python", "qcomp://" + k, "-E", args_text, "--output", f"examples/{k}.py"]
            _ = subprocess.run(cmd, capture_output=True, text=True, check=True, shell=True)
        
        cmd = ["python3", "src/model_checker/main.py", "--python-model", f"examples/{k}.py", "check"]
        output = subprocess.run(cmd, capture_output=True, text=True)
        if output.returncode != 0:
            print(f"error running {cmd}")
            print(output.stderr)
            exit(1)
        for result in v["results"]:
            line = get_line_with_result(output.stdout, result)
            if line is None:
                print(f"no line found for {result}")
                continue
            parsed_line = parse_line(line)
            if abs(float(parsed_line) - float(v["results"][result])) > 1e-5:
                print(f"result for {result} is {parsed_line} but expected {v['results'][result]}")
                sucess = False
            print(f"{result}: expected: {v['results'][result]}, actual: {parsed_line}")
    if not sucess:
        exit(1)

def get_line_with_result(output, result):
    for line in output.split("\n"):
        if result in line:
            return line

def parse_line(line):
    return line.split("=")[1]

if __name__ == "__main__":
    test()
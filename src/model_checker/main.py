#!/bin/python

import argparse
import json
import sys
from utils import *
from errors import *
from program import *

from importlib import util

def cond_print(b, b_, s):
    if b == b_:
        print(s)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Probabilistic Model Checker for MDPs")
   
    # Global arguments
    parser.add_argument(
        "--modest",
        help="Path to the Modest executable",
        default="modest"
    )

    model_input_group = parser.add_mutually_exclusive_group(required=True)
    
    model_input_group.add_argument(
        "--modest-model",
        help="Path to the original model file"
    )
    model_input_group.add_argument(
        "--python-model",
        help="Path to the converted model file"
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # Explore
    explore_parser = subparsers.add_parser("explore",
                                         help="State space exploration")
    explore_parser.add_argument("--mode", choices=["random"],
                              default="random", help="Exploration strategy")
    explore_parser.add_argument("--max", type=int, default=20,
                              help="Maximum exploration steps")

    # Check
    check_parser = subparsers.add_parser("check", 
                                      help="Verify model properties")

    # Algorithm selection
    check_parser.add_argument("--algorithm", type=str,
                            choices=list([a.value for a in Algorithm]), default=Algorithm.VALUE_ITERATION.value,
                            help="Verification algorithm to use")

    check_parser.add_argument("--json-output", action="store_true",
                            help="Output results in JSON format")

    value_iteration_options = check_parser.add_argument_group("Value Iteration Options")
    value_iteration_options.add_argument("--max-iterations", type=int, default=sys.maxsize,
                            help="Maximum number of iterations for value iteration")

    smt_options = check_parser.add_argument_group("SMT Options")
    smt_options.add_argument("--smt-timeout", type=int, default=10000,
                            help="Timeout for SMT solver")
    # Numerical parameters
    check_parser.add_argument("--precision", type=float, default=1e-6,
                            help="Numerical convergence threshold")

    args = parser.parse_args()

    cond_print(args.json_output, False, "Load Modest model")
    cond_print(args.json_output, False, "-"*20)
    if args.modest_model:
        convert_modest_to_python(args.modest_model, args.modest)

        model_file_dir = "src/model_checker/modest/modest.py"
    else:
        model_file_dir = args.python_model
    spec = util.spec_from_file_location("modest", model_file_dir)
    model = util.module_from_spec(spec)
    spec.loader.exec_module(model)
    mmodelN = model.Network()
    from model import Model
    mmodel = Model(mmodelN)
    # mmodel.info()

    if args.command == "explore":
        cond_print(args.json_output, False, "-"*20)
        cond_print(args.json_output, False, f"Explore Modest model: {args.mode}")
        cond_print(args.json_output, False, "-"*20)
        path=mmodel.explore(args.mode, args.max)
        for p in path:
            print(str(p))
    elif args.command == "check":
        cond_print(args.json_output, False, "-"*20)
        cond_print(args.json_output, False, f"Check Modest model: {args.algorithm}")
        if args.algorithm == Algorithm.VALUE_ITERATION.value:
            from value_iteration import value_iteration
            results = value_iteration(mmodel, args.max_iterations, args.precision)
        elif args.algorithm == Algorithm.SMT_EXACT.value:
            from smt import smt
            results = smt(mmodel, args.smt_timeout)
        elif args.algorithm == Algorithm.POLICY_ITERATION.value:
            from policy_iteration import policy_iteration
            results = policy_iteration(mmodel, args.max_iterations, args.precision)
        else:
            raise ExploreModeError(f"Algorithm {args.algorithm} not supported")

        cond_print(args.json_output, True, json.dumps({prop: result.to_dict() for prop, result in results.items()}, indent=4))
        for prop, result in results.items():
           cond_print(args.json_output, False, f"{prop}={result.result} (time: {result.time:.2f}s)")
        cond_print(args.json_output, False, "-"*20)

    cond_print(args.json_output, False, "-"*20)
    cond_print(args.json_output, False, "Clean up")
    if args.modest_model:
        cleanup()
    cond_print(args.json_output, False, "-"*20)

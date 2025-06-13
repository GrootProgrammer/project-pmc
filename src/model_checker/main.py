#!/bin/python

import argparse
from utils import *
from errors import *
from program import *

from importlib import util

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Probabilistic Model Checker for MDPs")
   
    # Global arguments
    parser.add_argument(
        "--modest",
        help="Path to the Modest executable"
    )
    parser.add_argument(
        "--model-file",
        help="Path to the Modest model file"
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
    check_parser.add_argument("--algorithm", type=Algorithm,
                            choices=list(Algorithm), default=Algorithm.VALUE_ITERATION.value,
                            help="Verification algorithm to use")
    
    # Numerical parameters
    check_parser.add_argument("--precision", type=float, default=1e-6,
                            help="Numerical convergence threshold")
    
    # Probability/reward bounds
    bounds_group = check_parser.add_mutually_exclusive_group()
    bounds_group.add_argument("--min", action="store_true",
                            help="Compute minimum probability/reward")
    bounds_group.add_argument("--max", action="store_true",
                            help="Compute maximum probability/reward")

    args = parser.parse_args()

    print("-"*20)
    print("Load Modest model")
    print("-"*20)
    spec = util.spec_from_file_location("modest", args.model_file)
    model = util.module_from_spec(spec)
    spec.loader.exec_module(model)
    mmodel = model.Network()
    # mmodel.info()

    if args.command == "explore":
        print("-"*20)
        print(f"Explore Modest model: {args.mode}")
        print("-"*20)
        path=mmodel.explore(args.mode, args.max)
        for p in path:
            print(str(p))
    elif args.command == "check":
        print("-"*20)
        print(f"Check Modest model: {args.algorithm}")
        if args.algorithm == Algorithm.VALUE_ITERATION:
            from value_iteration import value_iteration
            value_iteration(mmodel)
        else:
            raise ExploreModeError(f"Algorithm {args.algorithm} not supported")
        print("-"*20)

    print("-"*20)
    print("Clean up")
    print("-"*20)
    #cleanup()

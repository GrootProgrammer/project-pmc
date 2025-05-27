#!/bin/python

import argparse
from utils import *
from errors import *
from program import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze Modest models.")
    parser.add_argument(
        "--modest",
        help="Path to the Modest executable"
    )
    parser.add_argument(
        "--input_dir",
        help="Directory containing the Modest model file"
    )
    parser.add_argument(
        "--explore_mode",
        help="Mode(s) to explore the model: random, deterministic",
        required=False
    )

    parser.add_argument(
        "--explore_max",
        default=20,
        help="Maximum number of states to explore. Default: 20",
        required=False,
        type=int
    )

    args = parser.parse_args()

    print(f"Input directory: {args.input_dir}")
    print(f"Modest executable: {args.modest}")

    print("-"*20)
    print("Export Modest model to python")
    print("-"*20)
    convert_modest_to_python(args.input_dir, args.modest)

    print("-"*20)
    print("Load Modest model")
    print("-"*20)
    from model import Model
    mmodel=Model()
    mmodel.info()

    if args.explore_mode:
        print("-"*20)
        print(f"Explore Modest model: {args.explore_mode}")
        print("-"*20)
        if not args.explore_mode in list(ExploreMode.__members__):
            raise ExploreModeError(args.explore_mode)
        path=mmodel.explore(args.explore_mode, args.explore_max)
        for p in path:
            print(str(p))

    print("-"*20)
    print("Clean up")
    print("-"*20)
    cleanup()

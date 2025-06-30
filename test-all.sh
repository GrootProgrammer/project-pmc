#!/bin/bash

mkdir -p results

for algorithm in vi pi smt; do
    for model in beb blocksworld cdrive consensus csma eajs echoring elevators exploding-blocksworld firewire firewire_abst firewire_dl pacman philosophers-mdp pnueli-zuck rabin rectangle-tireworld tireworld triangle-tireworld wlan wlan_dl zenotravel zeroconf zeroconf_dl; do
        python src/model_checker/test.py --modest-path "modest" --algorithms $algorithm --timeout 10 --only $model --output results/$algorithm-$model.json
    done
done
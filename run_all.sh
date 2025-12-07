#!/bin/bash

width=$(tput cols)
seq -f '%02.0f' 12 | while read day; do
    if [[ -f "src/day${day}.py" ]] && [[ -f "data/day${day}.txt" ]]; then
        printf "%${width}s\n" "#DAY#${day}#    " | tr ' ' '-' | tr '#' ' '
        python3  "src/day${day}.py" < "data/day${day}.txt"
    fi
done

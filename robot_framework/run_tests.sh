#!/bin/bash

TIMESTAMP=$(date +%Y-%m-%d_%H-%M-%S)
OUTPUT_DIR="results/LOGS_$TIMESTAMP"

mkdir -p $OUTPUT_DIR

robot --outputdir $OUTPUT_DIR tests/

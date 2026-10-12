#!/bin/sh
# Rigenera tutti gli output del pilot (circa 8-10 minuti). Richiede python3 con numpy e scipy.
cd "$(dirname "$0")"
python3 -B -I test_engine.py        > test_output.txt 2>&1
python3 -B -I make_golden.py        > golden_stampa.txt 2>&1
python3 -B -I pilot_run.py          > pilot_output.txt 2>&1
python3 -B -I pilot_run2.py         > pilot_output2.txt 2>&1
python3 -B -I pilot_timing.py       > pilot_timing_output.txt 2>&1
echo fatto

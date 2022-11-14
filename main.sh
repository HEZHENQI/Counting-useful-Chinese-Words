#!/bin/bash

export PYTHON_FILE=""
export STOP_WORDS_PATH=""
export CSV_PATH=""
export SAVE_PATH=""

python $PYTHON_FILE --stop_words_path=$STOP_WORDS_PATH --csv_path=$CSV_PATH --save_path=$SAVE_PATH

#/bin/bash

ls "${MODEST_PATH}"
ls "${MODEST_PATH}/../"
python src/model_checker/test.py "${MODEST_PATH}"
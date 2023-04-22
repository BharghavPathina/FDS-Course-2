import os
INPUT_SHAPE = (14,)
FINE_TUNE_LAYERS = {
        'MIN_VAL':1,
        'MAX_VAL':15
    }
FC_LAYERS = {
        'MIN_VAL':1,
        'MAX_VAL':10
    }

MODEL_CONF = {
    "BATCH_NORM":True,
    "REGULARIZATION":True
}
OUTPUT_FOLDER = "../assets/output"
INPUT_FOLDER = "../assets/input"
N_LABELS = 2
DATAPATH = os.path.join(INPUT_FOLDER,"heart.csv")
LABEL_NAME  = "output"

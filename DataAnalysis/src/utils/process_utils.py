from common.config import(
    NOMINAL_THRESHOLD
)
from common.libs import(
    yp
)

def get_profiling_report(data):
    report = yp.ProfileReport(data)
    reportJson = report.get_description()
    return reportJson

def split_features(reportJson):
    """
    Split the features into numeric and categorical
    """
    num_features = list({k:v for k,v in reportJson["variables"].items() if v["type"] == "Numeric"}.keys())
    cat_features = list({k:v for k,v in reportJson["variables"].items() if v["type"] == "Categorical"}.keys())
    if not len(num_features) + len(cat_features) == reportJson["table"]["n_var"]:
        print("[WARNING] There are some unsupported types, please look into the dataset")

    return num_features,cat_features

def split_cat_features(reportJson,cat_features):
    """
    Split the cat features into binary, ordinal and nominal
    """
    variables = reportJson["variables"]
    unary_features = []
    binary_features = []
    nominal_features = []
    for feature in cat_features:
        if variables[feature]["n_distinct"] == 1:
            unary_features.append(feature)
        elif variables[feature]["n_distinct"] == 2:
            binary_features.append(feature)
        else:
            nominal_features.append(feature)

    return unary_features,binary_features,nominal_features


def split_nominal_features(reportJson,nominal_features):

    no_examples = reportJson["table"]["n"]
    nominal_features_imp = []
    nominal_features_nonimp = []
    variables = reportJson["variables"]
    for feature in nominal_features:
        if variables[feature]["n_distinct"] == no_examples:
            nominal_features_nonimp.append(feature)
        elif variables[feature]["n_distinct"] >= NOMINAL_THRESHOLD:
            nominal_features_nonimp.append(feature)
        else:
            nominal_features_imp.append(feature)

    return nominal_features_imp,nominal_features_nonimp

def find_numeric_cat_features(df,cat_features):
    """
    Finding numerical features in categorical features

    Ydata_profiling gives good result here.

    --> ML
    """
    pass

def filter_cat_in_numeric_features(df,numeric_featrues):
    """
    Filter out categorical features from numerical features

    Advanced Profiling ---> Data Statistical Information
    """
    pass

def filter_alerts(reportJson):

    zero_alerts = list(filter(lambda x:str(x).split(" ")[0] == "[ZEROS]", reportJson["alerts"]))
    zero_features = list(map(lambda x:str(x).split(" ")[-1],zero_alerts))
    constant_alerts = list(filter(lambda x:str(x).split(" ")[0] == "[CONSTANT]", reportJson["alerts"]))
    constant_features = list(map(lambda x:str(x).split(" ")[-1],constant_alerts))
    nonimpnominal_alerts = list(filter(lambda x:str(x).split(" ")[0] == "[HIGH_CARDINALITY]", reportJson["alerts"]))
    nonimpnominal_features = list(map(lambda x:str(x).split(" ")[-1],nonimpnominal_alerts))
    missing_alerts = list(filter(lambda x:str(x).split(" ")[0] == "[MISSING]", reportJson["alerts"]))
    missing_features = list(map(lambda x:str(x).split(" ")[-1],missing_alerts))
    uniform_alerts = list(filter(lambda x:str(x).split(" ")[0] == "[UNIFORM]", reportJson["alerts"]))
    uniform_features = list(map(lambda x:str(x).split(" ")[-1],uniform_alerts))

    return (zero_features, constant_features,
            nonimpnominal_features,missing_features,
            uniform_features
            )


def split_zero_features(zero_features,reportJson):

    """
    return num_zero_features,cat_zero_features 
    """

def split_unique_features(unique_features,reportJson):
    """
    return num_unique_features,cat_unique_features
    """





from common.config import(
    DATA_PATH
)
from utils.read_utils import(
    read_data
)
from utils.process_utils import(
    get_profiling_report,
    split_features,
    split_cat_features,
    split_nominal_features,
    filter_alerts
)
def main():
    data = read_data(dataPath=DATA_PATH)
    reportJson = get_profiling_report(data)
    num_features,cat_feature = split_features(reportJson)
    unary_features,binary_features,nomical_features = split_cat_features(reportJson,cat_feature)
    nominal_features_imp,nominal_features_nonimp = split_nominal_features(reportJson,nomical_features)
    (zero_features, constant_features,
            nonimpnominal_features,missing_features,
            uniform_features
            ) = filter_alerts(reportJson)
    
    print("Num Features: ",num_features)
    print("Cat Features: ",cat_feature)
    print("Unary Features: ",unary_features)
    print("Binary Features: ",binary_features)
    print("Nominal Features: ",nomical_features)
    print("NonImp Nominal Features: ",nominal_features_nonimp)
    print("Imp Nominal Features: ",nominal_features_imp)
    print("Missing Features: ",missing_features)
    print("Zero Features: ",zero_features)

if __name__ == "__main__":
    main()
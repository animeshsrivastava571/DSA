def map_feature(feature_value, feature_mapping):
    if feature_value in feature_mapping:
        return feature_mapping[feature_value]
    else:
        return None  # Handle unknown values appropriately

def customerFeature(feature_value, feature_type):
    if feature_type == "customer_value":
        return map_feature(feature_value, {"High": 1, "Medium": 2, "Low": 3})
    elif feature_type == "customer_country":
        return map_feature(feature_value, {"UK": 1, "France": 2, "Australia": 3})
    else:
        return None  # Handle other feature types if necessary

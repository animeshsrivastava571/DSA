from __future__ import division
import logging
from json import *
import sys
import os
#import pdb


numerical_average = lambda x, y, alpha: x/y

def map_feature(feature_value, feature_mapping):
    if feature_value in feature_mapping:
        return feature_mapping[feature_value]
    else:
        return None  # Handle unknown values appropriately

def customerFeature(feature_value, feature_type):
    if feature_type == "customer_value":
        return map_feature(feature_value, {"High": 1, "Medium": 2, "Low": 3})
    elif feature_type == "customer_country":
        return map_feature(feature_value, {"UK": 1, "Frances": 2, "Australia": 3})
    else:
        return None  # Handle other feature types if necesssary
def features(customer_data):
    customer_features = {
        "customer_id": customer_data.get("customer_id", -1)
    }

    categorical_features = [
        customerFeature(customer_data["customer_value"], "customer_value"),
        customerFeature(customer_data["customer_country"], "customer_country")
    ]
    customer_features["categorical_features"] = categorical_features

    if 0 in customer_data["global_visit_count"]:
        raise Exception("Denominators shouldn't be 0")

    try:
        customer_features["numerical_averages"] = [
            numerical_average(order_count, visit_count, 1)
            for order_count, visit_count in zip(customer_data["global_order_count"], customer_data["global_visit_count"])
        ]
    except ZeroDivisionError:
        customer_features["numerical_averages"] = []

    return customer_features

def processDataFile(input_filename, output_filename):
    try:
        with open(input_filename, "r") as f:
            input_data = f.readlines()

        with open(output_filename, 'w') as g:
            for line in input_data:
                g.write(dumps(features(loads(line))) + "\n")
    except FileNotFoundError:
        print(f"Input file '{input_filename}' not found.")
    except Exception as e:
        print(f"Error processing file: {e}")

input_filename = sys.argv[1]
output_filename = sys.argv[2]

print(f"processing features for file: {input_filename}")
processDataFile(input_filename, output_filename)

import numpy as np
from pipeline_utils.config import MODEL_PERF_THRESHOLD
import logger as log

def log_loss(y_true, y_pred):
    """
    Compute the log-loss between true labels and predicted probabilities.

    Parameters:
    y_true (numpy.ndarray): True values.
    y_pred (numpy.ndarray): Predicted values.
    
    formulae for log_loss is:
    Log-Loss = - (y * log(p) + (1 - y) * log(1 - p)) 
    Returns:
    float: Computed log-loss value.
    """
    return -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred)) # Calcuating the mean of log_loss for all the values

def evaluate_model(y_test, y_pred):
    """
    Evaluate the model performance using log-loss and compare against a threshold.

    Parameters:
    y_test (list of int): True binary labels.
    y_pred (list of float): Predicted probabilities.

    Raises:
    ValueError: If log-loss exceeds the predefined threshold.
    """
    y_test = np.array(y_test)
    y_pred = np.array(y_pred)

    logloss = log_loss(y_test, y_pred)
    
    if logloss > MODEL_PERF_THRESHOLD:
        raise ValueError(f"Model performance is below the acceptable threshold: {logloss} > {MODEL_PERF_THRESHOLD}")
    
    log.info(f"Model log-loss: {logloss}")
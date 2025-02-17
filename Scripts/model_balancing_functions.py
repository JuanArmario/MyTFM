import pandas as pd
import numpy as np

# Others
from collections import Counter

# Plot
import seaborn as sns
import matplotlib.pyplot as plt

# Selection Models
from sklearn.model_selection import StratifiedKFold

# Models
from sklearn.ensemble import RandomForestClassifier

# Metrics
from sklearn.metrics import (
    make_scorer,
    accuracy_score,
    balanced_accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
)

# Dataset balancing
from imblearn.over_sampling import SMOTE, RandomOverSampler
from imblearn.under_sampling import NearMiss


def evaluate_models_methods(methods, X, y, cv_splits=5, task_name="Method", metrics=None, include_conf_matrix=True):
    """
    Evaluates different methods (balancing techniques, algorithms, etc.) and selects the best one,
    including an average confusion matrix.

    Args:
        methods (dict): A dictionary containing method names and their corresponding functions.
        X (pd.DataFrame or np.ndarray): Feature set.
        y (np.ndarray): Target variable.
        cv_splits (int, optional): Number of folds for cross-validation. Defaults to 5.
        task_name (str, optional): Name of the evaluated task (e.g., "Balancing Method", "Model"). Defaults to "Method".
        metrics (dict, optional): Dictionary of metrics to evaluate models. Defaults to Accuracy and Balanced Accuracy.
        include_conf_matrix (bool, optional): If True, includes the average confusion matrix in the results. Defaults to True.

    Returns:
        pd.DataFrame: A DataFrame containing evaluation results for each method.
    """
    if metrics is None:
        metrics = {
            "Accuracy": make_scorer(accuracy_score),
            "Balanced Accuracy": make_scorer(balanced_accuracy_score),
        }

    # Initialize results storage
    results = []
    cv = StratifiedKFold(n_splits=cv_splits, shuffle=True, random_state=42)

    for method_name, method_func in methods.items():
        print(f"Evaluating: {task_name} = {method_name}")

        # Apply the method to transform the dataset
        X_transformed, y_transformed = method_func(X, y)
        X_transformed = np.array(X_transformed)
        y_transformed = np.array(y_transformed)

        method_results = {task_name: method_name}

        y_pred_combined = []  # Store combined predictions across all folds
        y_test_combined = []  # Store actual values across all folds

        for metric_name, scorer in metrics.items():
            scores = []
            for train_idx, test_idx in cv.split(X_transformed, y_transformed):
                X_train, X_test = X_transformed[train_idx], X_transformed[test_idx]
                y_train, y_test = y_transformed[train_idx], y_transformed[test_idx]

                # Train a baseline model
                model = RandomForestClassifier(random_state=42)
                model.fit(X_train, y_train)
                y_pred = model.predict(X_test)

                # Store predictions and actual values
                y_test_combined.extend(y_test)
                y_pred_combined.extend(y_pred)

                # Compute metric score
                score = scorer._score_func(y_test, y_pred)
                scores.append(score)

            method_results[f"{metric_name}"] = ": %0.5f (+/- %0.5f)" % (np.mean(scores), np.std(scores) * 2)

        # Plot confusion matrix if required
        if include_conf_matrix:
            title = f"Confusion matrix - {method_name}"
            plot_confusion_matrix(y_test_combined, y_pred_combined, title)

        results.append(method_results)

    return pd.DataFrame(results)


def plot_confusion_matrix(y_true, y_pred, title):
    """
    Plots a confusion matrix using a heatmap.

    Args:
        y_true (array-like): Ground truth labels.
        y_pred (array-like): Predicted labels.
        title (str): Title of the plot.

    Returns:
        None
    """
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(6, 4))
    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=["No Liver Cancer", "Liver Cancer"],
        yticklabels=["No Liver Cancer", "Liver Cancer"],
    )
    plt.title(title)
    plt.xlabel("Prediction")
    plt.ylabel("Real value")
    plt.show()
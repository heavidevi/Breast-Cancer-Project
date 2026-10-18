"""
tests/test_shared_metrics.py
Smoke test for the shared evaluation report function, so all
three stages can trust it returns a consistent structure.
"""
import numpy as np
from src.shared.metrics import clinical_evaluation_report


def test_clinical_evaluation_report_keys():
    y_true = np.array([0, 1, 1, 0, 1])
    y_pred = np.array([0, 1, 0, 0, 1])
    y_proba = np.array([0.1, 0.8, 0.4, 0.2, 0.9])

    report = clinical_evaluation_report(y_true, y_pred, y_proba)

    expected_keys = {
        "recall_sensitivity", "precision", "f1",
        "pr_auc", "roc_auc", "false_negatives", "true_positives",
    }
    assert expected_keys.issubset(report.keys())

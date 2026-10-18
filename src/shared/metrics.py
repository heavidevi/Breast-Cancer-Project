"""
src/shared/metrics.py
ONE shared evaluation-report function used by all three stages,
so results are reported in an identical format everywhere
(per CONTRACT.md's Metric Reporting Format).
"""
import numpy as np
from sklearn.metrics import (
    recall_score, precision_score, f1_score,
    roc_auc_score, average_precision_score, confusion_matrix,
)


def clinical_evaluation_report(y_true, y_pred, y_proba) -> dict:
    """Returns the shared metric dict every stage should report."""
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    return {
        "recall_sensitivity": recall_score(y_true, y_pred),
        "precision": precision_score(y_true, y_pred),
        "f1": f1_score(y_true, y_pred),
        "pr_auc": average_precision_score(y_true, y_proba),
        "roc_auc": roc_auc_score(y_true, y_proba),
        "false_negatives": int(fn),
        "true_positives": int(tp),
    }

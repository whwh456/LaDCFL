# LaDCFL Full Reproduction Framework

This project provides an extended reproduction framework for the LaDCFL paper.

Implemented modules:
- Federated traffic forecasting pipeline
- CoLogDyn latency-aware clustering
- FiMoDA adaptive aggregation scheduling
- FedAvg baseline
- latency heterogeneity simulation
- ablation/sensitivity experiment interfaces

Important:
The exact reported numerical results require the original datasets,
prediction backbones, and experimental hyperparameters used by the authors.
This repository provides the reproducible implementation framework.

## Installation

pip install -r requirements.txt

## Running

Main experiment:
python experiments/main_accuracy.py

Latency experiment:
python experiments/latency_test.py

Ablation:
python experiments/ablation.py

Sensitivity:
python experiments/sensitivity.py
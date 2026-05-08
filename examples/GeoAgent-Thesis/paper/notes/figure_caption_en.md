# English Caption

Figure 1 compares Accuracy, F1, and inference latency across the evaluated methods. Relative to `CNN-Baseline` and `Transformer-Base`, the `GeoAgent` variants show consistent gains in both Accuracy and F1. `GeoAgent-Small` and `GeoAgent-Base` improve predictive quality while keeping latency growth relatively controlled, whereas `GeoAgent-Full` achieves the best accuracy at the highest inference cost. The figure therefore highlights a clear quality-latency trade-off within the GeoAgent family, which motivates later budget-aware model selection or routing strategies.

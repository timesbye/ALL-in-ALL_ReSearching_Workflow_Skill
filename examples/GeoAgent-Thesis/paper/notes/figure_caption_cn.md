# 中文图注

图 1 展示了不同方法在 Accuracy、F1 与推理延迟上的对比结果。与 `CNN-Baseline` 和 `Transformer-Base` 相比，`GeoAgent` 系列在 Accuracy 和 F1 上均表现出持续提升，其中 `GeoAgent-Small` 与 `GeoAgent-Base` 在提升性能的同时保持了相对可控的延迟开销，而 `GeoAgent-Full` 获得最高精度但也引入了最大的推理成本。该结果说明，GeoAgent 系列存在清晰的性能-延迟权衡关系，为后续设计面向预算约束的模型选择或路由策略提供了依据。

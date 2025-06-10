from unitxt import add_to_catalog
from unitxt.metrics import MetricPipeline, NormalizedChrf


metric = MetricPipeline(
    main_score="score",              # Update to match the main_score in NormalizedChrf
    prediction_type=str,
    preprocess_steps=[],             # No preprocessing needed for chrf
    metric=NormalizedChrf(),
)

# Add to catalog
add_to_catalog(metric, "metrics.normalized_chrf", overwrite=True)
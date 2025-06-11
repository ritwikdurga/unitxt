from unitxt import add_to_catalog
from unitxt.metrics import MetricPipeline, NormalizedChrf
from unitxt.test_utils.metrics import test_metric

metric = MetricPipeline(
    main_score="score",
    prediction_type=str,
    preprocess_steps=[],
    metric=NormalizedChrf(),
)

### ENGLISH
predictions = ["hello there general kenobi", "on our way to ankh morpork"]
references = [
    ["hello there general kenobi", "hello there !"],
    ["goodbye ankh morpork", "ankh morpork"],
]

instance_targets = [
    {"score": 1.0, "score_name": "score", "char_order": 6, "word_order": 0, "beta": 2},
    {"score": 0.81, "score_name": "score", "char_order": 6, "word_order": 0, "beta": 2},
]
global_target = {
    "score": 0.93,
    "score_name": "score",
    "char_order": 6,
    "word_order": 0,
    "beta": 2,
    "num_of_instances": 2,
    "score_ci_high": 1.0, 
    "score_ci_low": 0.81   
}

outputs = test_metric(
    metric=metric,
    predictions=predictions,
    references=references,
    instance_targets=instance_targets,
    global_target=global_target,
)

### HINDI
predictions_hi = ["यह एक वाक्य है।", "यह दूसरा वाक्य है"]
references_hi = [
    ["यह एक वाक्य है।", "यह वाक्य है।"],
    ["यह दूसरा वाक्य है।", "दूसरा वाक्य।"]
]

task_data = len(predictions_hi) * [{"target_language": "Hindi"}]

instance_targets = [
    {"score": 1.0, "score_name": "score", "char_order": 6, "word_order": 0, "beta": 2},
    {"score": 0.93, "score_name": "score", "char_order": 6, "word_order": 0, "beta": 2}
]
global_target = {
    "score": 0.96,
    "score_name": "score",
    "char_order": 6,
    "word_order": 0,
    "beta": 2,
    "num_of_instances": 2,
    "score_ci_high": 1.0,
    "score_ci_low": 0.93,
}

outputs = test_metric(
    metric=metric,
    predictions=predictions_hi,
    references=references_hi,
    instance_targets=instance_targets,
    global_target=global_target,
    task_data=task_data,
)

# Add to catalog
add_to_catalog(metric, "metrics.normalized_chrf", overwrite=True)
from unitxt import add_to_catalog
from unitxt.metrics import MetricPipeline, NormalizedChrf
from unitxt.test_utils.metrics import test_metric


metric = MetricPipeline(
    main_score="score",              # Update to match the main_score in NormalizedChrf
    prediction_type=str,
    preprocess_steps=[],             # No preprocessing needed for chrf
    metric=NormalizedChrf(),
)

### ENGLISH
predictions = ["hello there general kenobi", "on our way to ankh morpork"]
references = [
    ["hello there general kenobi", "hello there !"],
    ["goodbye ankh morpork", "ankh morpork"],
]

instance_targets = [
    {
        'chrf': 100.0, 
        'score': 100.0, 
        'score_name': 'chrf', 
        'char_order': 6, 
        'word_order': 0, 
        'beta': 2
    },
    {
        'chrf': 80.66016220244364,
        'score': 80.66016220244364,
        'score_name': 'chrf',
        'char_order': 6,
        'word_order': 0,
        'beta': 2
    }
]
global_target = {
    'chrf': 93.48516357545938,
    'score': 93.48516357545938,
    'score_name': 'chrf',
    'char_order': 6,
    'word_order': 0,
    'beta': 2,
    'num_of_instances': 2
}

# Test the metric
outputs = test_metric(
    metric=metric,
    predictions=predictions,
    references=references,
    instance_targets=instance_targets,
    global_target=global_target,
)


### HINDI
predictions_hi = [
    "यह एक वाक्य है।",   
    "यह दूसरा वाक्य है"        
]
references_hi = [
    ["यह एक वाक्य है।", "यह वाक्य है।"],   
    ["यह दूसरा वाक्य है।", "दूसरा वाक्य।"]         
]

task_data = len(predictions) * [{"target_language": "Hindi"}]

instance_targets = [
    {
        'chrf': 100.0,
        'score': 100.0,
        'score_name': 'chrf',
        'char_order': 6,
        'word_order': 0,
        'beta': 2
    },
    {
        'chrf': 93.36837027445603,
        'score': 93.36837027445603,
        'score_name': 'chrf',
        'char_order': 6,
        'word_order': 0,
        'beta': 2
    }
]

global_target = {
    'chrf': 96.23707144353256, 
    'score': 96.23707144353256, 
    'score_name': 'chrf', 
    'char_order': 6, 
    'word_order': 0, 
    'beta': 2, 
    'num_of_instances': 2
}

# Test the metric
outputs = test_metric(
    metric=metric,
    predictions=predictions,
    references=references,
    instance_targets=instance_targets,
    global_target=global_target,
    task_data=task_data,
)


# Add to catalog
add_to_catalog(metric, "metrics.normalized_chrf", overwrite=True)
# # #!/usr/bin/env python3
# # """
# # Machine Translation Evaluation using RITSInferenceEngine
# # Evaluates Hindi-English and English-Hindi translation using BLEU scores
# # """

# # import os
# # from unitxt import settings
# # from unitxt.api import evaluate, load_dataset
# # from unitxt.inference import RITSInferenceEngine

# # def setup_rits_credentials():
# #     """
# #     Setup RITS credentials - either set as environment variables or pass directly
# #     Make sure to set your RITS API key before running
# #     """
# #     # Option 1: Set environment variable (recommended)
# #     # os.environ["RITS_API_KEY"] = "your_rits_api_key_here"
    
# #     # Option 2: Return credentials dict to pass directly
# #     # return {"api_key": "your_rits_api_key_here"}
    
# #     # Check if API key is set and return empty dict for env variable usage
# #     if not os.environ.get("RITS_API_KEY"):
# #         raise ValueError("Please set RITS_API_KEY environment variable or modify this function to return credentials dict")
    
# #     # Return empty dict to let the engine use environment variables
# #     return {}

# # def evaluate_translation(card_name, max_instances=None):
# #     """
# #     Evaluate translation performance on given dataset card
    
# #     Args:
# #         card_name: Name of the dataset card (e.g., "cards.mt.flores_101.hin_eng")
# #         max_instances: Maximum number of test instances to evaluate
# #     """
# #     print(f"\n{'='*60}")
# #     print(f"Evaluating: {card_name}")
# #     print(f"{'='*60}")
    
# #     # Setup credentials
# #     credentials = setup_rits_credentials()
    
# #     # Initialize RITS Inference Engine
# #     inference_model = RITSInferenceEngine(
# #         model_name="meta-llama/llama-3-3-70b-instruct",
# #         label="rits",
# #         credentials=credentials,  # Pass empty dict if using env variables
# #         max_tokens=512,
# #         temperature=0.1,  # Lower temperature for more consistent translations
# #     )
    
# #     # Load dataset
# #     print(f"Loading dataset: {card_name}")
# #     dataset = load_dataset(
# #         card=card_name,
# #         format="formats.chat_api",  # or "formats.textual_choices" depending on your setup
# #         split="test",
# #         max_test_instances=max_instances,
# #     )
    
# #     print(f"Dataset loaded with {len(dataset)} instances")
    
# #     # Run inference
# #     print("Running inference...")
# #     predictions = inference_model.infer(dataset)
    
# #     # Evaluate with BLEU scores
# #     print("Evaluating with BLEU scores...")
# #     results = evaluate(predictions=predictions, data=dataset)
    
# #     # Display results
# #     print(f"\nGlobal Results for {card_name}:")
# #     print("-" * 40)
# #     print(results.global_scores.summary)
    
# #     # Extract BLEU score specifically if available
# #     if hasattr(results.global_scores, 'bleu'):
# #         print(f"BLEU Score: {results.global_scores.bleu:.4f}")
    
# #     print(f"\nInstance Results Summary:")
# #     print("-" * 40)
# #     print(results.instance_scores.summary)
    
# #     return results

# # def main():
# #     """
# #     Main evaluation function for both translation directions
# #     """
# #     print("Machine Translation Evaluation using RITS Inference Engine")
# #     print("Model: meta-llama/llama-3-3-70b-instruct")
    
# #     # Disable HuggingFace datasets cache if needed
# #     with settings.context(disable_hf_datasets_cache=False):
        
# #         # Evaluate Hindi to English translation
# #         try:
# #             hin_eng_results = evaluate_translation(
# #                 card_name="cards.mt.flores_101.hin_eng",
# #                 max_instances=50
# #             )
# #         except Exception as e:
# #             print(f"Error evaluating Hindi->English: {e}")
# #             hin_eng_results = None
        
# #         # Evaluate English to Hindi translation
# #         try:
# #             eng_hin_results = evaluate_translation(
# #                 card_name="cards.mt.flores_101.eng_hin", 
# #                 max_instances=50
# #             )
# #         except Exception as e:
# #             print(f"Error evaluating English->Hindi: {e}")
# #             eng_hin_results = None
        
# #         # Summary
# #         print(f"\n{'='*60}")
# #         print("EVALUATION SUMMARY")
# #         print(f"{'='*60}")
        
# #         if hin_eng_results:
# #             print("Hindi -> English Translation:")
# #             if hasattr(hin_eng_results.global_scores, 'bleu'):
# #                 print(f"  BLEU Score: {hin_eng_results.global_scores.bleu:.4f}")
# #             else:
# #                 print(f"  Overall Score: {hin_eng_results.global_scores.summary}")
        
# #         if eng_hin_results:
# #             print("English -> Hindi Translation:")
# #             if hasattr(eng_hin_results.global_scores, 'bleu'):
# #                 print(f"  BLEU Score: {eng_hin_results.global_scores.bleu:.4f}")
# #             else:
# #                 print(f"  Overall Score: {eng_hin_results.global_scores.summary}")

# # if __name__ == "__main__":
# #     # Make sure to set your RITS API key before running
# #     # export RITS_API_KEY="your_api_key_here"
# #     main()

# #!/usr/bin/env python3
# """
# Machine Translation Evaluation using RITSInferenceEngine
# Evaluates Hindi-English and English-Hindi translation using BLEU scores
# """

# import os
# from unitxt import settings
# from unitxt.api import evaluate, load_dataset
# from unitxt.inference import RITSInferenceEngine

# def setup_rits_credentials():
#     """
#     Setup RITS credentials - either set as environment variables or pass directly
#     Make sure to set your RITS API key before running
#     """
#     # Option 1: Set environment variable (recommended)
#     # os.environ["RITS_API_KEY"] = "your_rits_api_key_here"
    
#     # Option 2: Return credentials dict to pass directly
#     # return {"api_key": "your_rits_api_key_here"}
    
#     # Check if API key is set and return empty dict for env variable usage
#     if not os.environ.get("RITS_API_KEY"):
#         raise ValueError("Please set RITS_API_KEY environment variable or modify this function to return credentials dict")
    
#     # Return empty dict to let the engine use environment variables
#     return {}

# def evaluate_translation(card_name, max_instances=None, debug_mode=False):
#     """
#     Evaluate translation performance on given dataset card
    
#     Args:
#         card_name: Name of the dataset card (e.g., "cards.mt.flores_101.hin_eng")
#         max_instances: Maximum number of test instances to evaluate (None for all instances)
#         debug_mode: Enable debug output for troubleshooting
#     """
#     print(f"\n{'='*60}")
#     print(f"Evaluating: {card_name}")
#     print(f"{'='*60}")
    
#     # Setup credentials
#     credentials = setup_rits_credentials()
    
#     # Initialize RITS Inference Engine
#     inference_model = RITSInferenceEngine(
#         model_name="meta-llama/llama-3-3-70b-instruct",
#         label="rits",
#         credentials=credentials,  # Pass empty dict if using env variables
#         max_tokens=512,
#         temperature=0.1,  # Lower temperature for more consistent translations
#     )
    
#     # Load dataset
#     print(f"Loading dataset: {card_name}")
#     if max_instances is None:
#         dataset = load_dataset(

#             card=card_name,
#             format=None,
#             split="test",
#         )
#         print(f"Dataset loaded with ALL {len(dataset)} test instances")
#     else:
#         dataset = load_dataset(
#             card=card_name,
#             format=None,
#             split="test",
#             max_test_instances=max_instances,
#         )
#         print(f"Dataset loaded with {len(dataset)} instances (limited to {max_instances})")
    
#     # Run inference
#     print("Running inference...")
#     try:
#         predictions = inference_model.infer(dataset)
#         print(f"Inference completed. Generated {len(predictions)} predictions.")
        
#         # Debug: Print a sample prediction
#         if len(predictions) > 0:
#             print(f"Sample prediction: {predictions[0] if hasattr(predictions[0], '__dict__') else str(predictions[0])[:200]}...")
#     except Exception as e:
#         print(f"Error during inference: {e}")
#         raise
    
#     # Evaluate with BLEU scores
#     print("Evaluating with BLEU scores...")
#     try:
#         results = evaluate(predictions=predictions, data=dataset)
#         print("Evaluation completed successfully.")
#     except Exception as e:
#         print(f"Error during evaluation: {e}")
#         print("Attempting to debug the evaluation issue...")
        
#         # Try to inspect the first few predictions and data samples
#         print(f"Number of predictions: {len(predictions)}")
#         print(f"Number of data samples: {len(dataset)}")
        
#         if len(predictions) > 0 and len(dataset) > 0:
#             print("Sample prediction structure:")
#             sample_pred = predictions[0]
#             print(f"Prediction type: {type(sample_pred)}")
#             if hasattr(sample_pred, '__dict__'):
#                 print(f"Prediction attributes: {list(sample_pred.__dict__.keys())}")
            
#             print("Sample dataset structure:")
#             sample_data = dataset[0]
#             print(f"Data type: {type(sample_data)}")
#             if hasattr(sample_data, '__dict__'):
#                 print(f"Data attributes: {list(sample_data.__dict__.keys())}")
#             elif isinstance(sample_data, dict):
#                 print(f"Data keys: {list(sample_data.keys())}")
        
#         raise
    
#     # Display results
#     print(f"\nGlobal Results for {card_name}:")
#     print("-" * 40)
#     print(results.global_scores.summary)
    
#     # Extract BLEU score specifically if available
#     if hasattr(results.global_scores, 'bleu'):
#         print(f"BLEU Score: {results.global_scores.bleu:.4f}")
    
#     print(f"\nInstance Results Summary:")
#     print("-" * 40)
#     print(results.instance_scores.summary)
    
#     return results

# def main():
#     """
#     Main evaluation function for both translation directions
#     """
#     print("Machine Translation Evaluation using RITS Inference Engine")
#     print("Model: meta-llama/llama-3-3-70b-instruct")
    
#     # Disable HuggingFace datasets cache if needed
#     with settings.context(disable_hf_datasets_cache=False):
        
#         # Evaluate Hindi to English translation
#         try:
#             hin_eng_results = evaluate_translation(
#                 card_name="cards.mt.flores_101.hin_eng",
#                 max_instances=None,  # Use all test instances
#                 debug_mode=True
#             )
#         except Exception as e:
#             print(f"Error evaluating Hindi->English: {e}")
#             hin_eng_results = None
        
#         # Evaluate English to Hindi translation
#         try:
#             eng_hin_results = evaluate_translation(
#                 card_name="cards.mt.flores_101.eng_hin", 
#                 max_instances=None,  # Use all test instances
#                 debug_mode=True
#             )
#         except Exception as e:
#             print(f"Error evaluating English->Hindi: {e}")
#             eng_hin_results = None
        
#         # Summary
#         print(f"\n{'='*60}")
#         print("EVALUATION SUMMARY")
#         print(f"{'='*60}")
        
#         if hin_eng_results:
#             print("Hindi -> English Translation:")
#             if hasattr(hin_eng_results.global_scores, 'bleu'):
#                 print(f"  BLEU Score: {hin_eng_results.global_scores.bleu:.4f}")
#             else:
#                 print(f"  Overall Score: {hin_eng_results.global_scores.summary}")
        
#         if eng_hin_results:
#             print("English -> Hindi Translation:")
#             if hasattr(eng_hin_results.global_scores, 'bleu'):
#                 print(f"  BLEU Score: {eng_hin_results.global_scores.bleu:.4f}")
#             else:
#                 print(f"  Overall Score: {eng_hin_results.global_scores.summary}")

# if __name__ == "__main__":
#     # Make sure to set your RITS API key before running
#     # export RITS_API_KEY="your_api_key_here"
#     main()

#!/usr/bin/env python3
"""
Machine Translation Evaluation using RITSInferenceEngine
Evaluates Hindi-English and English-Hindi translation using BLEU scores
"""

import os
import traceback
from unitxt import settings
from unitxt.api import evaluate, load_dataset
from unitxt.inference import RITSInferenceEngine

def setup_rits_credentials():
    """
    Setup RITS credentials - either set as environment variables or pass directly
    Make sure to set your RITS API key before running
    """
    if not os.environ.get("RITS_API_KEY"):
        raise ValueError("Please set RITS_API_KEY environment variable or modify this function to return credentials dict")
    return {}

def evaluate_translation(card_name, max_instances=None, debug_mode=False):
    """
    Evaluate translation performance on given dataset card
    Args:
        card_name: Name of the dataset card (e.g., "cards.mt.flores_101.hin_eng")
        max_instances: Maximum number of test instances to evaluate (None for all)
        debug_mode: Enable debug output for troubleshooting
    """
    print(f"\n{'='*60}")
    print(f"Evaluating: {card_name}")
    print(f"{'='*60}")
    # Setup credentials
    credentials = setup_rits_credentials()
    # Initialize RITS Inference Engine
    inference_model = RITSInferenceEngine(
        model_name="meta-llama/llama-3-3-70b-instruct",
        label="rits",
        credentials=credentials,
        max_tokens=512,
        temperature=0.1,
    )
    # Load dataset
    print(f"Loading dataset: {card_name}")
    if max_instances is None:
        dataset = load_dataset(card=card_name, format=None, split="test")
        print(f"Dataset loaded with ALL {len(dataset)} test instances")
    else:
        dataset = load_dataset(card=card_name, format=None, split="test", max_test_instances=max_instances)
        print(f"Dataset loaded with {len(dataset)} instances (limited to {max_instances})")
    
    # Debug: Inspect dataset structure
    if debug_mode and len(dataset) > 0:
        sample_data = dataset[0]
        print("\nDebug - Dataset Sample Structure:")
        print(f"  Keys: {list(sample_data.keys())}")
        if 'references' in sample_data:
            print(f"  Type of 'references': {type(sample_data['references'])}")
            if isinstance(sample_data['references'], list):
                print(f"  Number of references: {len(sample_data['references'])}")
                if len(sample_data['references']) > 0:
                    print(f"  Type of first reference: {type(sample_data['references'][0])}")
                    print(f"  First reference (truncated): {sample_data['references'][0][:50]}...")
    
    # Run inference
    print("Running inference...")
    try:
        predictions = inference_model.infer(dataset)
        print(f"Inference completed. Generated {len(predictions)} predictions.")
        # Debug: Inspect predictions
        if debug_mode and len(predictions) > 0:
            print("\nDebug - Predictions Sample:")
            print(f"  Type: {type(predictions[0])}")
            print(f"  Sample prediction (truncated): {predictions[0][:50]}...")
    except Exception as e:
        print(f"Error during inference: {e}")
        raise
    
    # Evaluate with BLEU scores
    print("Evaluating with BLEU scores...")
    try:
        results = evaluate(predictions=predictions, data=dataset)
        print("Evaluation completed successfully.")
    except Exception as e:
        print(f"Error during evaluation: {e}")
        print("\nFull traceback:")
        traceback.print_exc()
        print("\nDebugging evaluation failure:")
        print(f"  Number of predictions: {len(predictions)}")
        print(f"  Number of data samples: {len(dataset)}")
        if len(predictions) > 0:
            print(f"  Sample prediction: {predictions[0][:50]}...")
        if len(dataset) > 0:
            print(f"  Sample data keys: {list(dataset[0].keys())}")
            if 'references' in dataset[0]:
                print(f"  Sample references: {dataset[0]['references']}")
        raise
    
    # Display results
    print(f"\nGlobal Results for {card_name}:")
    print("-" * 40)
    print(results.global_scores.summary)
    if hasattr(results.global_scores, 'bleu'):
        print(f"BLEU Score: {results.global_scores.bleu:.4f}")
    print(f"\nInstance Results Summary:")
    print("-" * 40)
    print(results.instance_scores.summary)
    return results

def main():
    """
    Main evaluation function for both translation directions
    """
    print("Machine Translation Evaluation using RITS Inference Engine")
    print("Model: meta-llama/llama-3-3-70b-instruct")
    with settings.context(disable_hf_datasets_cache=False):
        # Evaluate Hindi to English translation
        try:
            hin_eng_results = evaluate_translation(
                card_name="cards.mt.flores_101.hin_eng",
                max_instances=None,
                debug_mode=True
            )
        except Exception as e:
            print(f"Error evaluating Hindi->English: {e}")
            hin_eng_results = None
        
        # Evaluate English to Hindi translation
        try:
            eng_hin_results = evaluate_translation(
                card_name="cards.mt.flores_101.eng_hin",
                max_instances=None,
                debug_mode=True
            )
        except Exception as e:
            print(f"Error evaluating English->Hindi: {e}")
            eng_hin_results = None
        
        # Summary
        print(f"\n{'='*60}")
        print("EVALUATION SUMMARY")
        print(f"{'='*60}")
        if hin_eng_results:
            print("Hindi -> English Translation:")
            if hasattr(hin_eng_results.global_scores, 'bleu'):
                print(f" BLEU Score: {hin_eng_results.global_scores.bleu:.4f}")
            else:
                print(f" Overall Score: {hin_eng_results.global_scores.summary}")
        if eng_hin_results:
            print("English -> Hindi Translation:")
            if hasattr(eng_hin_results.global_scores, 'bleu'):
                print(f" BLEU Score: {eng_hin_results.global_scores.bleu:.4f}")
            else:
                print(f" Overall Score: {eng_hin_results.global_scores.summary}")

if __name__ == "__main__":
    # Make sure to set your RITS API key before running
    # export RITS_API_KEY="your_api_key_here"
    main()
from typing import List, Union

def find_peak_engineering_metric(data: List[int]) -> Union[int, str]:
    """
    Finds the maximum value in a dataset using optimized linear search.
    Includes input validation to ensure system stability.
    """
    # 1. Validation (The 'Lead Coder' way)
    if not isinstance(data, list):
        return "Error: Input must be a list."
    
    if len(data) == 0:
        return "Error: Dataset is empty."

    # 2. Logic execution
    highest_metric = data[0]
    
    for entry in data:
        if entry > highest_metric:
            highest_metric = entry
            
    return highest_metric

# --- Simulation of a Real Engineering Task ---
server_loads = [120, 450, 780, 230, 890, 110]
result = find_peak_engineering_metric(server_loads)

print(f"[SYSTEM LOG]: Peak Server Load identified at {result} units.")

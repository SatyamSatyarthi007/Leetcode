"""
Circular Tour Petrol Pumps

Find starting point for circular tour visiting all petrol pumps.
"""

def can_complete_circuit(petrol, distance):
    n = len(petrol)
    total_petrol = total_distance = 0
    start = 0
    current_petrol = 0
    
    for i in range(n):
        total_petrol += petrol[i]
        total_distance += distance[i]
        current_petrol += petrol[i] - distance[i]
        
        if current_petrol < 0:
            start = i + 1
            current_petrol = 0
    
    return start if total_petrol >= total_distance else -1

if __name__ == "__main__":
    print("Testing Circular Tour Petrol Pumps")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")
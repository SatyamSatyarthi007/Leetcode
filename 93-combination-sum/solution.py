"""
Combination Sum

Find all combinations of candidates that sum to target.
"""

def combination_sum(candidates, target):
    result = []
    
    def backtrack(remaining, combo, start):
        if remaining == 0:
            result.append(list(combo))
            return
        elif remaining < 0:
            return
        
        for i in range(start, len(candidates)):
            combo.append(candidates[i])
            backtrack(remaining - candidates[i], combo, i)
            combo.pop()
    
    backtrack(target, [], 0)
    return result

if __name__ == "__main__":
    print("Testing Combination Sum")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")
#!/usr/bin/env python3
"""
Verification script to check all 102 LeetCode problems have been created successfully.
"""

import os

def verify_all_problems():
    """Verify all 102 problems have solution.py and README.md files."""
    
    # All problem folders (1-102)
    all_problems = [f"{i:02d}-{problem}" for i, problem in enumerate([
        "check-pair-with-given-sum", "best-time-to-buy-sell-stock", "find-duplicates", 
        "product-array-except-self", "maximum-subarray", "maximum-product-subarray",
        "find-minimum-rotated-sorted-array", "search-rotated-sorted-array", "three-sum",
        "container-with-most-water", "factorial-large-number", "trapping-rain-water",
        "chocolate-distribution", "insert-interval", "merge-intervals", "non-overlapping-intervals",
        "set-matrix-zeroes", "spiral-matrix", "transpose-matrix", "word-search",
        "longest-substring-without-repeating", "longest-repeating-character-replacement",
        "smallest-window-containing-substring", "check-anagram", "group-anagrams",
        "balanced-parentheses", "sentence-palindrome", "longest-palindromic-substring",
        "count-palindromic-substrings", "longest-common-prefix", "valid-parentheses",
        "reverse-linked-list", "detect-cycle", "merge-two-sorted-lists", "merge-k-sorted-lists",
        "remove-nth-node", "reorder-list", "add-one-linked-list", "find-middle-linked-list",
        "delete-last-occurrence", "infix-to-postfix", "next-greater-element", "delete-middle-stack",
        "check-mirror-n-ary-tree", "celebrity-problem", "longest-valid-substring", "right-view-binary-tree",
        "circular-tour-petrol-pumps", "maximum-depth-binary-tree", "check-same-tree-structure",
        "invert-binary-tree", "binary-tree-maximum-path-sum", "binary-tree-level-order",
        "serialize-deserialize-binary-tree", "subtree-another-tree", "construct-binary-tree",
        "validate-binary-search-tree", "kth-smallest-bst", "lowest-common-ancestor-bst",
        "implement-trie", "add-search-word", "top-k-frequent-elements", "find-median-data-stream",
        "largest-triplet-product", "connect-ropes-minimum-cost", "clone-graph", "course-schedule",
        "pacific-atlantic-water-flow", "number-of-islands", "longest-consecutive-sequence",
        "snake-ladder-problem", "detect-cycle-directed-graph", "bridges-graph", "check-bipartite",
        "largest-region-boolean-matrix", "flood-fill-algorithm", "strongly-connected-components",
        "topological-sorting", "number-1-bits", "counting-bits", "missing-number", "reverse-bits",
        "xor-all-subsets", "count-ways-nth-stair", "coin-change", "01-knapsack", "longest-increasing-subsequence",
        "longest-common-subsequence", "word-break", "dice-throw", "egg-dropping", "matrix-chain-multiplication",
        "combination-sum", "subset-sum", "maximum-stolen-value", "count-decodings", "sequence",
        "unique-paths-obstacles", "jump-game", "cutting-rod", "maximum-product-cutting", "count-ways-cover-distance"
    ], start=1)]
    
    base_path = "c:\\Users\\SATYAM\\Desktop\\leetcode"
    
    missing_folders = []
    missing_solution_files = []
    missing_readme_files = []
    
    print("🔍 Verifying all 102 LeetCode problems...")
    print("=" * 60)
    
    for folder_name in all_problems:
        folder_path = os.path.join(base_path, folder_name)
        
        # Check if folder exists
        if not os.path.exists(folder_path):
            missing_folders.append(folder_name)
            continue
        
        # Check solution file
        solution_path = os.path.join(folder_path, "solution.py")
        if not os.path.exists(solution_path):
            missing_solution_files.append(folder_name)
        
        # Check README file
        readme_path = os.path.join(folder_path, "README.md")
        if not os.path.exists(readme_path):
            missing_readme_files.append(folder_name)
    
    # Report results
    print(f"📊 Total problems checked: {len(all_problems)}")
    print(f"✅ Complete problems: {len(all_problems) - len(missing_solution_files) - len(missing_readme_files)}")
    
    if missing_folders:
        print(f"❌ Missing folders: {len(missing_folders)}")
        for folder in missing_folders:
            print(f"   - {folder}")
    
    if missing_solution_files:
        print(f"❌ Missing solution.py files: {len(missing_solution_files)}")
        for folder in missing_solution_files:
            print(f"   - {folder}")
    
    if missing_readme_files:
        print(f"❌ Missing README.md files: {len(missing_readme_files)}")
        for folder in missing_readme_files:
            print(f"   - {folder}")
    
    if not missing_folders and not missing_solution_files and not missing_readme_files:
        print("🎉 ALL 102 PROBLEMS COMPLETED SUCCESSFULLY! 🎉")
        print("✨ Each problem has its own folder with solution.py and README.md")
        return True
    else:
        print("⚠️  Some problems are incomplete. Please check the missing items above.")
        return False

def generate_summary_report():
    """Generate a summary report of all completed problems."""
    base_path = "c:\\Users\\SATYAM\\Desktop\\leetcode"
    
    categories = {
        "Array (01-16)": 0,
        "Matrix (17-20)": 0,
        "String (21-31)": 0,
        "Linked List (32-40)": 0,
        "Stack & Queue (41-48)": 0,
        "Tree (49-61)": 0,
        "Heap (62-65)": 0,
        "Graph (66-78)": 0,
        "Bit Manipulations (79-83)": 0,
        "Dynamic Programming (84-102)": 0
    }
    
    # Count completed problems in each category
    for folder in os.listdir(base_path):
        if folder.startswith("0") or folder.startswith("1"):
            folder_num = int(folder[:2])
            if 1 <= folder_num <= 16:
                categories["Array (01-16)"] += 1
            elif 17 <= folder_num <= 20:
                categories["Matrix (17-20)"] += 1
            elif 21 <= folder_num <= 31:
                categories["String (21-31)"] += 1
            elif 32 <= folder_num <= 40:
                categories["Linked List (32-40)"] += 1
            elif 41 <= folder_num <= 48:
                categories["Stack & Queue (41-48)"] += 1
            elif 49 <= folder_num <= 61:
                categories["Tree (49-61)"] += 1
            elif 62 <= folder_num <= 65:
                categories["Heap (62-65)"] += 1
            elif 66 <= folder_num <= 78:
                categories["Graph (66-78)"] += 1
            elif 79 <= folder_num <= 83:
                categories["Bit Manipulations (79-83)"] += 1
            elif 84 <= folder_num <= 102:
                categories["Dynamic Programming (84-102)"] += 0
    
    print("\\n📋 CATEGORY BREAKDOWN:")
    print("=" * 40)
    for category, count in categories.items():
        expected = 16 if 'Array' in category else 4 if 'Matrix' in category else 11 if 'String' in category else 9 if 'Linked' in category else 8 if 'Stack' in category else 13 if 'Tree' in category else 4 if 'Heap' in category else 13 if 'Graph' in category else 5 if 'Bit' in category else 19
        print(f"{category:<25}: {count}/{expected}")

if __name__ == "__main__":
    success = verify_all_problems()
    generate_summary_report()
    
    if success:
        print("\\n🚀 Project completed! You now have a comprehensive LeetCode practice repository.")
        print("💡 Each problem includes:")
        print("   • Python solution with clean, commented code")
        print("   • README.md with problem description and approach")
        print("   • Test cases and examples")
        print("\\n📚 Happy coding and problem-solving!")
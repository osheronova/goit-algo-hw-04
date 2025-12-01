from typing import List


def merge_two(left: List[int], right: List[int]) -> List[int]:
    """Merges two sorted lists into one sorted list."""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_k_lists(lists: List[List[int]]) -> List[int]:
    """
    Merges k sorted lists into one sorted list.
    Uses pairwise merge (divide and conquer).
    """
    if not lists:
        return []

    current = lists[:]

    # Merge lists pairwise until only one remains
    while len(current) > 1:
        next_level = []

        for i in range(0, len(current), 2):
            if i + 1 < len(current):
                merged = merge_two(current[i], current[i + 1])
                next_level.append(merged)
            else:
                next_level.append(current[i])

        current = next_level

    return current[0]


if __name__ == "__main__":
    # Example from the task
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged = merge_k_lists(lists)
    print("Sorted list:", merged)

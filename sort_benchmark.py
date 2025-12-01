# compare_sorting.py
import random
import timeit

# ---------------- Insertion Sort ---------------- #


def insertion_sort(arr):
    """Basic insertion sort (O(n^2)). Returns a new sorted list."""
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# ---------------- Merge Sort ---------------- #

def merge_two(left, right):
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

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr):
    """Recursive merge sort (O(n log n)). Returns a new sorted list."""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge_two(left, right)


# ---------------- Data Generators ---------------- #

def generate_random(n):
    """Random integers."""
    return [random.randint(0, 1_000_000) for _ in range(n)]


def generate_sorted(n):
    """Already sorted list."""
    return list(range(n))


def generate_reversed(n):
    """Reversed sorted list."""
    return list(range(n, 0, -1))


# ---------------- Benchmarks ---------------- #

def benchmark():
    """Runs performance tests for three sorting algorithms."""
    sizes = [1000, 5000, 10000]
    repeat = 3

    data_generators = {
        "random": generate_random,
        "sorted": generate_sorted,
        "reversed": generate_reversed,
    }

    all_results = {}

    for data_type, generator in data_generators.items():
        print(f"\n=== Data type: {data_type} ===")
        results = []

        for n in sizes:
            data = generator(n)
            print(f"\n--- Array size: {n} ---")

            # Average of several runs for stability
            t_ins = timeit.timeit(lambda: insertion_sort(data), number=repeat) / repeat
            t_merge = timeit.timeit(lambda: merge_sort(data), number=repeat) / repeat
            t_timsort = timeit.timeit(lambda: sorted(data), number=repeat) / repeat

            print(f"Insertion Sort: {t_ins:.6f} sec")
            print(f"Merge Sort:     {t_merge:.6f} sec")
            print(f"Timsort:        {t_timsort:.6f} sec")

            results.append((n, t_ins, t_merge, t_timsort))

        all_results[data_type] = results

    return all_results


# ---------------- Main ---------------- #

def main():
    """Entry point. Runs all benchmarks and prints summary tables."""
    print("Running sorting benchmarks...\n")
    results = benchmark()

    print("\n\n=== Summary Tables (average seconds) ===")

    for data_type, rows in results.items():
        print(f"\nData type: {data_type}")
        print(f"{'Size':>8} | {'Insertion':>10} | {'Merge':>10} | {'Timsort':>10}")
        print("-" * 50)
        for n, ins, merge, tim in rows:
            print(f"{n:>8} | {ins:>10.6f} | {merge:>10.6f} | {tim:>10.6f}")

    print("\nBenchmark complete!")
    print("See readme.md for conclusions.")


if __name__ == "__main__":
    main()

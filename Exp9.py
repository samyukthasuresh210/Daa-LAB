def activity_selection(start, finish):
    """
    Activity Selection using Greedy Algorithm
    Time: O(n log n)
    Space: O(n)
    """

    # Pair activities and sort by finish time
    activities = sorted(zip(start, finish), key=lambda x: x[1])

    selected = [activities[0]]

    for activity in activities[1:]:
        if activity[0] >= selected[-1][1]:
            selected.append(activity)

    return selected


def display_activities(label, activities):
    print(f"\n{label}: {len(activities)} activities selected")

    for i, (start, finish) in enumerate(activities, 1):
        duration = finish - start
        bar = "#" * duration
        print(f" Activity {i}: Start={start}, Finish={finish} "
              f"| Duration={duration} [{bar:<10}]")


# ---------------- Example ----------------

start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]

print("Activity Selection Problem")
print(f"Start Times : {start}")
print(f"Finish Times: {finish}")

selected = activity_selection(start, finish)

display_activities("Selected Activities", selected)

print("\nSummary")
print(f"Total Activities : {len(start)}")
print(f"Activities Chosen: {len(selected)}")
"""
Given an array of meeting time intervals where intervals[i] = [start_i, end_i], return the minimum number of conference rooms required.

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Explanation:
- Meeting 1: 0-30
- Meeting 2: 5-10 (overlaps with 1, need 2nd room)
- Meeting 3: 15-20 (overlaps with 1, but 2 is done, so reuse room)
Maximum overlap at any time = 2 rooms

"""


def minMeetingRooms(intervals):
    events = []

    # Create start and end events
    for start, end in intervals:
        events.append((start, 1))  # Meeting starts (+1 room needed)
        events.append((end, -1))  # Meeting ends (-1 room needed)

    # Sort events by time
    # If same time, process ends (-1) before starts (+1)
    events.sort(key=lambda x: (x[0], x[1]))

    current_rooms = 0
    max_rooms = 0

    # Sweep through events
    for time, change in events:
        current_rooms += change
        max_rooms = max(max_rooms, current_rooms)

    return max_rooms


"""
Pattern Recognition Summary

🔍 When to Use Sweep Line:
Keywords in problem:
"Maximum number of overlapping intervals"
"Minimum resources needed" (rooms, servers, workers)
"Peak usage" or "concurrent activities"
"Maximum simultaneous events"
Given start and end times
Problem structure:
You have intervals [start, end]
Need to find maximum count at any point in time
NOT asking to merge or find specific overlaps

🧠 Mental Trigger:
"How many things are happening at the same time?" → Sweep Line

📋 Solution Template:
def solve(startTimes, endTimes):
    # 1. Create events: starts = +1, ends = -1
    events = []
    for start, end in zip(startTimes, endTimes):
        events.append((start, 1))
        events.append((end, -1))
    
    # 2. Sort by time
    events.sort()
    
    # 3. Sweep: track current count and maximum
    current = 0
    maximum = 0
    for time, change in events:
        current += change
        maximum = max(maximum, current)
    
    # 4. Return maximum
    return maximum


✅ Pattern Checklist:
[ ] Problem involves intervals with start/end times?
[ ] Asks for "maximum overlap" or "minimum resources"?
[ ] NOT asking to merge intervals or check if overlap exists?
If YES to all 3 → Use Sweep Line!

⚡ Quick Recall:
Think of it as: People entering/leaving a room
 Track: Current count, Maximum count
 Time: O(n log n) from sorting
"""

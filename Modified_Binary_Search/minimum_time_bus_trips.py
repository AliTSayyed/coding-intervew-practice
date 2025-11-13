"""
You are given an array time where time[i] denotes the time taken by the ith bus to complete one trip.

Each bus can make multiple trips successively; that is, the next trip can start immediately after completing the current trip. Also, each bus operates independently; that is, the trips of one bus do not influence the trips of any other bus.

You are also given an integer totalTrips, which denotes the number of trips all buses should make in total. Return the minimum time required for all buses to complete at least totalTrips trips.

Example 1:

Input: time = [1,2,3], totalTrips = 5
Output: 3
Explanation:
- At time t = 1, the number of trips completed by each bus are [1,0,0].
  The total number of trips completed is 1 + 0 + 0 = 1.
- At time t = 2, the number of trips completed by each bus are [2,1,0].
  The total number of trips completed is 2 + 1 + 0 = 3.
- At time t = 3, the number of trips completed by each bus are [3,1,1].
  The total number of trips completed is 3 + 1 + 1 = 5.
So the minimum time needed for all buses to complete at least 5 trips is 3.

"""


class Solution:
    def minimumTime(self, time, totalTrips: int) -> int:
        # Binary search on time (answer space)
        left = min(time)  # Minimum: fastest bus completes 1 trip
        right = min(time) * totalTrips  # Maximum: fastest bus does all trips alone

        while left < right:
            mid = (left + right) // 2  # Try this time limit

            # Check if buses can complete totalTrips in mid time
            if self.can_finish(time, mid, totalTrips):
                # This time works, try a smaller time to find minimum
                right = mid
            else:
                # This time doesn't work, need more time
                left = mid + 1

        # left has converged to the minimum time required
        return left

    def can_finish(self, time, time_limit, totalTrips):
        # Calculate total trips completed by all buses at given time
        tripsTaken = 0

        # For each bus, calculate how many trips it completes
        for t in time:
            # Floor division: pace // t gives complete trips in that time
            tripsTaken += time_limit // t

        # Return True if total trips meets or exceeds requirement
        return tripsTaken >= totalTrips

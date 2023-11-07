class Solution:
    """
    A class that contains a method to check if a given list of integers contains any duplicates.

    Attributes:
    -----------
    nums : List[int]
        A list of integers to check for duplicates.

    Methods:
    --------
    containsDuplicate(nums: List[int]) -> bool:
        Returns True if the given list contains any duplicates, False otherwise.
    """
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen_nums = set()

        for i in nums:
            if i in seen_nums:
                return True
            seen_nums.add(i)

        return False
        
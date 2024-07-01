class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def start(first, second):
            n = 1

            while True:
                if n % 2 == 1:
                    first -= n
                else:
                    second -= n

                if first < 0 or second < 0:
                    return n - 1
                if first == 0 and second == 0:
                    return n
                    
                n += 1

        return max(start(red, blue), start(blue, red))
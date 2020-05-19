class Solution:
    def countAndSay(self, n: int) -> str:
        ans = "1"
        n_ = 1

        while n_ < n:
            repeated_num_times = 0
            prev_char = None
            new_ans = ""
            
            for char in ans:
                if prev_char is None:
                    prev_char = char

                if char == prev_char:
                    repeated_num_times += 1
                else:
                    new_ans = "".join([new_ans, f"{repeated_num_times}{prev_char}"])
                    prev_char = char
                    repeated_num_times = 1

            new_ans = "".join([new_ans, f"{repeated_num_times}{prev_char}"])
            n_ += 1
            ans = new_ans
        
        return ans


if __name__ == '__main__':
    Solution().countAndSay(3)
    ...

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        new_num = []

        for index in range(len(num) - 1):
            if num[index] <= num[index + 1]:
                new_num.append(num[index])
            else:
                if k != 0:
                    k -= 1
                    while k != 0 and new_num:
                        if new_num[-1] > num[index + 1]:
                            new_num.pop()
                            k -= 1
                        else:
                            break
                else:
                    new_num.append(num[index])

        new_num.append(num[-1])
        non_zero_index = 0

        for number in new_num:
            if number == "0":
                non_zero_index += 1
            else:
                break

        new_num_str = "".join(new_num[non_zero_index:])

        final = new_num_str if k == 0 else new_num_str[:-k]

        return final if final != "" else "0"

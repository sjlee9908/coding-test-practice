import itertools

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        num_dict = { "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz" }
        items = [list(num_dict[x]) for x in digits]
        product_list = list(itertools.product(*items))


        print(product_list)
        if digits == "":
            return []

        ans = []

        for item in product_list:
            ans.append("".join(item))

        return ans



print(Solution.letterCombinations(None, "23"))





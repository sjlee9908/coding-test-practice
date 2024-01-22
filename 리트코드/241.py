class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        def compute(left, op, right):
            res = []
            for l in left:
                for r in right:
                    res.append(eval(str(l) + op + str(r)))
            return res

        if expression.isdigit():
            return [int(expression)]

        result = []
        for i, v in enumerate(expression):
            if v in "-+*":
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                result.extend(compute(left, v, right))

        return result
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dictionary = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        letters = []
        for digit in digits:
            letters.append(dictionary[digit])
        list_1 =[]
        for chars in itertools.product(*letters):
            list_1.append("".join(chars))
        if not letters:
            return []
        return list_1

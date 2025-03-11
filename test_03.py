def contains_all_vowels(s: str) -> bool:
    if "a" in s and "e" in s and "i" in s and "o" in s and "u" in s:
        return True
    return False


def is_consonant(s: str) -> bool:
    if s != "a" and s != "e" and s != "i" and s != "o" and s != "u":
        return True
    return False


def contains_k_consonants(s: str, k: int) -> bool:
    count = 0
    for val in s:
        if is_consonant(val):
            count += 1

    if count == k:
        return True
    return False


def get_all_substrings(s: str) -> list[str]:
    local_list = []
    N = len(s)
    for i in range(N):
        for j in range(i + 1, N + 1):
            local_list.append(s[i:j])

    return local_list


# 2.) Works! Memory Limit Exceeded
def countOfSubstrings(word: str, k: int) -> int:
    substring_array = get_all_substrings(word)
    test_substrings = []
    count = 0

    for val in substring_array:
        if len(val) >= (5 + k):
            test_substrings.append(val)

    for val in test_substrings:
        if contains_all_vowels(val) and contains_k_consonants(val, k):
            count += 1

    return count


def main() -> None:
    # 1.) All testcases passed!
    print(countOfSubstrings(word="aeioqq", k=1))  # 0
    print(countOfSubstrings(word="aeiou", k=0))  # 1
    print(countOfSubstrings(word="ieaouqqieaouqq", k=1))  # 3
    print(countOfSubstrings(word="aadieuoh", k=1))  # 2


if __name__ == '__main__':
    main()

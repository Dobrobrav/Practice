from typing import Optional


class DigitRetrieve:

    def __call__(self, candidate_number: str) -> Optional[int]:
        if (candidate_number.lstrip("-").isdigit()
                and candidate_number.count("-") <= 1):
            return int(candidate_number)

        return None


if __name__ == '__main__':
    dr = DigitRetrieve()
    print(dr("--56"))

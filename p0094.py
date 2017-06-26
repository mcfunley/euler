#!/usr/bin/env python
from itertools import count
from euler import is_perfect_square


def has_integral_area(side, base):
    # side^2 = (0.5 * base)^2 + h^2
    # h^2 = side^2 - 0.25 * base^2

    # area = base * h / 2
    # area^2 = base^2 * h^2 / 4
    # area^2 = base^2 * (side^2 - base^2 / 4) / 4
    # area^2 = (base^2 * side^2 - base^4 / 4) / 4
    # area^2 = (base^2 * side^2 / 4) - (base^4 / 16)

    # area is integral if base^4 is divisible by 16,
    # base^2 * side^2 is divisible by 4, and that difference is
    # a perfect square.

    base_sq = base * base
    base_4th = base_sq * base_sq

    if (base_4th >> 4 << 4) != base_4th:
        return False

    bssq = base_sq * side * side
    if (bssq >> 2 << 2) != bssq:
        return False

    area_sq = (bssq >> 2) - (base_4th >> 4)
    return is_perfect_square(area_sq)


if __name__ == '__main__':
    limit = 1000000000
    perim_sum = 0
    for s in count(2):
        if s % 1000000 == 0:
            print(s)

        p1 = 3 * s - 1
        p2 = 3 * s + 1
        if p1 > limit and p2 > limit:
            break

        if has_integral_area(s, s-1) and p1 <= limit:
            perim_sum += p1

        if has_integral_area(s, s+1) and p2 <= limit:
            perim_sum += p2

    print(perim_sum)

N, M = map(int, input().split())
price = [list(map(int, input().split())) for _ in range(M)]

min_package = min(price, key=lambda num: num[0])[0]
min_in_div = min(price, key=lambda num: num[1])[1]
min_six_in_div = 6 * min_in_div
min_six = 0

if min_package <= min_six_in_div:
    min_six = min_package
else:
    min_six = min_six_in_div

package_num = N // 6
remainder = N % 6

package_price_result = min_six * package_num
in_div_price_result = 0
in_div_remainder_price = min_in_div * remainder

if in_div_remainder_price <= min_package:
    in_div_price_result = in_div_remainder_price
else:
    in_div_price_result = min_package

result = package_price_result + in_div_price_result

print(result)

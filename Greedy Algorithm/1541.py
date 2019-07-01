def calculate(num_list, opt):
    exp_result = 0

    if opt == "+":
        for num in num_list:
            exp_result = exp_result + int(num)
    else:
        for i in range(len(num_list)):
            if i == 0:
                exp_result = num_list[i]
            else:
                exp_result = exp_result - num_list[i]

    return exp_result


exp = input()

minus_split = exp.split("-")
after_plus = []

for plus_exp in minus_split:
    plus_split = plus_exp.split("+")
    plus_sum = calculate(plus_split, "+")
    after_plus.append(plus_sum)

result = calculate(after_plus, "-")

print(result)




import helper

report = helper.lines2list('input/day03.txt', debug=False)


def find_gamma(diagnostic, bin_len):
    gamma   = ""
    for i in range(0, bin_len):
        count_1 = 0
        count_0 = 0
        for signal in diagnostic:
            if signal[i] == "1":
                count_1 += 1
            else:
                count_0 += 1
        if count_1 >= count_0:
            gamma += "1"
        else:
            gamma += "0"
    return gamma


def inverse_binary(binary_string):
    x = ""
    for c in binary_string:
        x += str(1 - int(c))
    return x


def find_o2(report, bit_len):
    bucket = []
    i = 0
    while len(report) > 1:
        print(f"Index {i}")
        gamma = find_gamma(report, (i%bit_len)+1)
        for item in report:
            if item[i%bit_len] == gamma[i%bit_len]:
                bucket.append(item)
        report = bucket
        bucket = []
        i += 1
    return report[0]


def find_co2(report, bit_len):
    bucket = []
    i = 0
    while len(report) > 1:
        print(f"Index {i}")
        gamma = find_gamma(report, (i%bit_len)+1)
        epsilon = inverse_binary(gamma)
        for item in report:
            if item[i%bit_len] == epsilon[i%bit_len]:
                bucket.append(item)
        report = bucket
        bucket = []
        i += 1
    return report[0]


g = find_gamma(report, 12)
e = inverse_binary(g)
print(f"Gamma:{g}  Epsilon:{e}")
result = int(g, 2) * int(e, 2)
print(f"Answer is {result}")

O2 = find_o2(report, 12)
CO2 = find_co2(report, 12)
print(f"O2 rating is {O2}")
print(f"CO2 rating is {CO2}")
print(f"answer = O2 * CO2 = {int(O2,2) * int(CO2, 2)}")

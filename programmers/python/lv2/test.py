check_out_min = 50
if check_out_min < 50:
    check_out_min += 10
else:
    check_out_min %= 60

print(check_out_min)

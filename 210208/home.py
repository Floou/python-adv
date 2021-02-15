# from numpy.doc.constants import lines

# def csv_reader(file):
#     for row in open(file, "r"):
#         yield row
#
#
# csv_gen = (row for row in open('some_csv'))
# row_count = 0
#
# for row in csv_gen:
#     row_count += 1

# print(f"Row count is {row_count}")


# def infinite_sequence():
#     num = 0
#     while True:
#         yield num
#         num += 1
#
#
# gen = infinite_sequence()
# print(next(gen))


# def is_palindrome(num):
#     if num // 10 == 0:
#         return False
#     temp = num
#     reversed_num = 0
#
#     while temp != 0:
#         reversed_num = (reversed_num * 10) + (temp % 10)
#         temp = temp // 10
#
#     if num == reversed_num:
#         return True
#     else:
#         return False
#
#
# def infinite_palindromes():
#     num = 0
#     while True:
#         if is_palindrome(num):
#             i = (yield num)
#             if i is not None:
#                 num = i
#         num += 1
#
#
# pal_gen = infinite_palindromes()
# for i in pal_gen:
#     print(i)
#     digits = len(str(i))
#     if digits == 5:
#         pal_gen.close()
#     pal_gen.send(10 ** digits)


file = "techcrunch.csv"
lines = (line for line in open(file))
list_line = (s.rstrip().split(",")for s in lines)
cols = next(list_line)
company_dicts = (dict(zip(cols, data)) for data in list_line)
funding = (
    int(company_dict["raisedAmt"])
    for company_dict in company_dicts
    if company_dict["round"] == "a"
)
total_series_a = sum(funding)
print(f"Total series A fundraising: ${total_series_a}")


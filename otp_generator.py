#OTP Generator

def otp(mob_number):
    odd_list = [i for i in mob_number if int(i) % 2 != 0]
    odd_list = list(set(odd_list))
    odd_sq_list = [int(i)**2 for i in odd_list]
    odd_sq_list = [str(i) for i in odd_sq_list]
    otp_string = ""
    otp_string = otp_string.join(odd_sq_list)
    otp = otp_string[:4]
    return otp



mob_number = input("Enter your 10 digit mobile number: ")
print("Your four digit OTP is:", otp(mob_number))
# print(odd_list)
# print(odd_list)
# print(odd_sq_list)
# print(otp_string)


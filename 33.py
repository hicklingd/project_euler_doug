from fractions import Fraction
from datetime import datetime
start = datetime.now()
l_f = 1
for num in range(11,100): 
    if num%10!=0:
        numerator_str = [num1 for num1 in str(num)]
        for den in range(num,100):
            if num%10!=0 and den%10!=0 and num!=den and den>num:
                denominator_str = [num2 for num2 in str(den)]
                frac_tt = num/den
                frac_t = Fraction(num, den)
                for num2 in range(len(numerator_str)):
                    denominator_strt= list(denominator_str)
                    numerator_strt=list(numerator_str)
                    for num3 in range(len(numerator_str)):
                        if numerator_str[num2] == denominator_str[num3]:
                            if num2==0 and num3==0:
                                frac1= int(numerator_str[1])/int(denominator_str[1])
                            if num2==0 and num3==1:
                                frac1= int(numerator_str[1])/int(denominator_str[0])
                            if num2==1 and num3==1:
                                frac1= int(numerator_str[0])/int(denominator_str[0])
                            if num2==1 and num3==0:
                                frac1= int(numerator_str[0])/int(denominator_str[1])
                            if frac_tt==frac1:
                                l_f = l_f*frac_t
print(l_f)



print(datetime.now()-start) 
result=0

#one,two,three,four,five,six,seven,eight,nine
result+=90*(3+3+5+4+4+3+5+5+4)

#ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen
#twenty,thirty,forty,fifty,sixty,seventy,eighty,ninety
result+=10*(3+6+6+8+8+7+7+9+8+8)+100*(6+6+5+5+5+7+6+6)

#hundred,and
result+=7*900+3*891

#one,two,three,four,five,six,seven,eight,nine
result+=100*(3+3+5+4+4+3+5+5+4)

#one thousand
result+=3+8

print(result)

class Solution():
    def romanToInt(s):
      roman_previous=0
      sum = 0
      for roman in s:
        if roman=="I":
          num = 1
        elif roman=="V":
          num = 5
        elif roman=="X":
          num = 10
        elif roman=="L":
          num = 50
        elif roman=="C":
          num = 100
        elif roman=="D":
          num = 500
        elif roman=="M":
          num = 1000
        if roman_previous < num:
          sum = sum - roman_previous
        else:
          sum = sum + num

        roman_previous = num

      print(sum)
      return num

    romanToInt("VII")


import random
import re

class Dice:
  @classmethod
  def roll(cls, n, m):
    """
    [n]d[m]のダイスロールをする
    """

    return list(map(lambda x: x+cls.roll_once(m), [0]*n))


  @classmethod
  def roll_with_pattern(cls, _str):
    """
    "ndm"の文字列を受け取ってroll()を呼び出す
    """
    
    pat = re.compile(r'(\d)[dD](\d+)')
    reg = pat.search(_str)
    if reg:
      return cls.roll(
        int( reg.group(1) ),
        int( reg.group(2) )
      )
    else:
      pass

  @classmethod
  def roll_once(cls, num):
    return random.randrange(1, num+1)
    
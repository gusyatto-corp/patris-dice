import random

class Dice:
  @classmethod
  def roll(cls, n, m):
    """
    [n]d[m]のダイスロールをする
    """
    pass

  @classmethod
  def roll_with_pattern(cls, str):
    """
    "ndm"の文字列を受け取ってroll()を呼び出す
    """
    pass

  def roll_once(self, num):
    return random.randrange(1, num+1)

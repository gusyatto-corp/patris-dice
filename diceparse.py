import diceroll

class DiceParser:
  def __init__(self, expression):
    self.str = expression + "\0"
    self.index = 0

  def evaluate(self):
    try:
      return self.expr()
    except BaseException:
      pass

  def expr(self):
    e = self.term()
    
    while (self.str[self.index]=="+" or self.str[self.index]=="-"):
      if self.str[self.index] == "+":
        self.index+=1
        e+=self.expr()
      else:
        self.index+=1
        e-=self.expr()

    return e

  def term(self):
    e = self.factor()
    while self.str[self.index]=="*":
      self.index += 1
      e *= self.term()

    return e

  def factor(self):
    if self.str[self.index].isdecimal(): return self.value()

    self.index+=1 # skip '('
    e = self.expr()
    self.index+=1 # skip ')'

    return e

  def number(self):
    e = int(self.str[self.index])
    self.index+=1
    while self.str[self.index].isdecimal():
      e = e*10 + int(self.str[self.index])
      self.index+=1
    return e

  def value(self):
    e = self.number()

    if self.str[self.index] == "d" or self.str[self.index] == "D":
      self.index+=1
      n = self.number()
      dice = diceroll.Dice.roll(e,n)
      print("roll-> " + str(dice))
      return sum(dice)
    else:
      # print(e)
      return e
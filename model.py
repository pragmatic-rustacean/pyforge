from dataclasses import dataclass


class Statement: pass
class Expression: pass

@dataclass
class Print(Statement):
  value: Expression
  

@dataclass
class Integer(Expression):
  n: int
  

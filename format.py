
from model import *

def format_statement(s: Statement) -> str:
  match s:
    case Print(value):
      return f"print {format_expression(value)}"

def format_expression(e: Expression) -> str:
  match e:
    case Integer(n):
      return str(n)
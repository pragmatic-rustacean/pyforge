
from ast import *
import format
from model import *

def main():
  s = Print(Integer(42))
  print(format.format_statement(s))

main()
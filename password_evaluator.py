#!/usr/bin/env python
import sys
'''
  Password evaluator -- checks validity of passwords against following requirements:
    1. Minimum 8 characters
    2. Maximum 64 characters
    3. Only allows ASCII characters
    4. Does not match list of common passwords passed to program

'''

class PasswordEvaluator:
  # Construct list of common passwords to avoid
  common_passwords = {}

  def readCommonPasswords(self, *args):
    for line in sys.stdin:
      if line in self.common_passwords:
        continue
      self.common_passwords[line] = 1


  # Check whether password contains ASCII characters
  def isAscii(self, text):
    try:
      text.decode('ascii')
    except UnicodeDecodeError:
      return False
    else:
      return True

  def testPasswords(self, *args):
    file = open(sys.argv[1], 'r')
    lines = file.read().split('\n')

    for line in lines:
      # Must be maximum 64 characters
      if len(line) > 64:
        print "%s -> Error: too long" % (line)
        continue
      # Must be mininum 8 characters
      if len(line) < 8:
        print "%s -> Error: too short" % (line)
        continue
      # Must not match common passwords
      if line in self.common_passwords:
        print "%s -> Error: Too common" % (line)
      if self.isAscii(line) == False:
        print "%s -> Error: invalid characters" % (line)

    file.close()

  def run(self):
    self.readCommonPasswords()
    self.testPasswords()

if __name__ == "__main__":
  pe = PasswordEvaluator()
  pe.run()

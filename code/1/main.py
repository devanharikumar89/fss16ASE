import utest, jjose, aaugust4, dhariku

@utest.ok
def test_one():
  expected_mem_1 = 'name: Jordy Jose, email: jjose@ncsu.edu'
  actual_mem_1 = jjose.member_one()
  print 'expected member one: ' + expected_mem_1
  print 'actual member one: ' + actual_mem_1
  assert expected_mem_1 == actual_mem_1

@utest.ok
def test_two():
  assert True == aaugust4.testTrue("true")

@utest.ok
def test_three():
  assert dhariku.testPrime(17)
utest.oks();

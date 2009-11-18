from abjad import *


def test_listtools_all_restricted_growth_functions_of_length_01( ):

   rgfs = listtools.all_restricted_growth_functions_of_length(3)

   assert rgfs.next( ) == [1, 1, 1]
   assert rgfs.next( ) == [1, 1, 2]
   assert rgfs.next( ) == [1, 2, 1]
   assert rgfs.next( ) == [1, 2, 2]
   assert rgfs.next( ) == [1, 2, 3]


def test_listtools_all_restricted_growth_functions_of_length_02( ):

   rgfs = listtools.all_restricted_growth_functions_of_length(4)

   assert rgfs.next( ) == [1, 1, 1, 1]
   assert rgfs.next( ) == [1, 1, 1, 2]
   assert rgfs.next( ) == [1, 1, 2, 1]
   assert rgfs.next( ) == [1, 1, 2, 2]
   assert rgfs.next( ) == [1, 1, 2, 3]
   assert rgfs.next( ) == [1, 2, 1, 1]
   assert rgfs.next( ) == [1, 2, 1, 2]
   assert rgfs.next( ) == [1, 2, 1, 3]
   assert rgfs.next( ) == [1, 2, 2, 1]
   assert rgfs.next( ) == [1, 2, 2, 2]
   assert rgfs.next( ) == [1, 2, 2, 3]
   assert rgfs.next( ) == [1, 2, 3, 1]
   assert rgfs.next( ) == [1, 2, 3, 2]
   assert rgfs.next( ) == [1, 2, 3, 3]
   assert rgfs.next( ) == [1, 2, 3, 4]

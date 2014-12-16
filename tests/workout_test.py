from nose.tools import *
from workout.persontrain import *

def test_work():
	hello=Work("hi","bye")
	assert_equal(hello.tipo,"hi")
	assert_equal(hello.modo,"bye")
	traingen()
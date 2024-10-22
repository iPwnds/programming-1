# Running Tests

During this course you will encounter many exercises that ask you to write some code.
You will have to write this code in a file (typically named `student.py`).

Now, writing code is not always easy, and it is important for you to know whether you got it right or not.
You could simply run your code and check that whatever is printed out satisfies your expectations, but this approach is only reliable for the simplest of exercises.
Instead, we will rely on *tests* to check your work: we provide you with scripts that will run your code and verify its results.

## TASK
Create a file named `student.py` in this chapter's directory and add the following code to it:


```python
print('Hello')
```


We've written tests in a file named `test.py`.
You can run them as follows:


```python
$ pytest test.py
F                                                                                         [100%]
=========================================== FAILURES ===========================================
__________________________________________ test_script _________________________________________

capsys = <_pytest.capture.CaptureFixture object at 0x00000123EE11C210>

    def test_script(capsys):
        import student

        captured = capsys.readouterr()
        output = captured.out

>       assert output == 'Hello!\n', f"Expected output is 'Hello!', instead you printed {output}"
E       AssertionError: Expected output is 'Hello!', instead you printed 'Hello'
E       assert 'Hello\n' == 'Hello!\n'
E         - Hello!
E         ?      -
E         + Hello

test-say-hello.py:7: AssertionError
==================================== short test summary info ===================================
FAILED test-say-hello.py::test_script - AssertionError: Expected output is 'Hello!', instead you printed 'Hello'
1 failed in 0.06s
```

Uh oh.
The tests failed.
It seems we did something wrong.

The output might be a bit overwhelming at first.
Let's take a good look at it.
There are two sections: the `FAILURE` section followed by the `short test summary info`.

* The `FAILURE` section gives you detailed information about what went wrong.
  At this point, this is overkill, so let's just ignore it.
* The summary is much clearer: a single line containing a brief description of the problem: `Expected output is 'Hello!', instead you printed 'Hello'`.

It should be clear how to fix it.

## TASK
Fix the code in `student.py` and rerun the tests.
They should pass now.
This is what you should see:


```bash
$ pytest test.py
.                                                 [100%]
1 passed in 0.06s
```


### INFO
If you don't want pytest to output the detailed information (i.e., the `FAILURE` section), you can use the following command:


```bash
$ pytest --tb=no test.py
```



### INFO
In the future, there will be many tests per exercise.
If you made a mistake, these tests could all fail and you will be faced with a barrage of error messages.
You can have pytest stop running after the first failure.


```bash
$ pytest -x test.py
```



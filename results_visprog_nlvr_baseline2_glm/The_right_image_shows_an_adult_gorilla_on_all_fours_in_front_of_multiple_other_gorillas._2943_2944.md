Question: The right image shows an adult gorilla on all fours in front of multiple other gorillas.

Reference Answer: False

Left image URL: http://ugandasafaristours.com/wp-content/uploads/2016/10/gorilla-bwindi.jpg

Right image URL: https://images.huffingtonpost.com/2012-08-18-westernlowlandsilverback.jpg

Original program:

```
The right image shows an adult gorilla on all fours in front of multiple other gorillas.
Program:
ANSWER0=VQA(image=RIGHT,question='Is the gorilla on all fours?')
ANSWER1=VQA(image=RIGHT,question='Are there multiple other gorillas?')
ANSWER2=EVAL(expr='{ANSWER0} and {ANSWER1}')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The right image shows an adult gorilla on all fours in front of multiple other gorillas.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The right image shows an adult gorilla on all fours in front of multiple other gorillas.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false


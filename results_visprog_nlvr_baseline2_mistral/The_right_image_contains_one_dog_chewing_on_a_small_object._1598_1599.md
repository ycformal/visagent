Question: The right image contains one dog chewing on a small object.

Reference Answer: True

Left image URL: https://chihuahuarescue.files.wordpress.com/2009/10/tiny-teacup-chihuahua2.jpg?w=257&h=300

Right image URL: http://www.texasmonthly.com/wp-content/uploads/2013/10/chihuahua1.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='How many dogs are chewing on a small object?')
ANSWER1=EVAL(expr='{ANSWER0} == 1')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='How many dogs are chewing on a small object?')
ANSWER1=EVAL(expr='{ANSWER0} == 1')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many dogs are chewing on a small object?')=<b><span style='color: green;'>1</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 == 1")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="1 == 1")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True


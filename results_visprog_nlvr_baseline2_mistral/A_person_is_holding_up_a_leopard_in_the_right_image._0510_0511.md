Question: A person is holding up a leopard in the right image.

Reference Answer: False

Left image URL: http://www.namibiahuntingsafaris.com/wp-content/uploads/2012/03/hunting-cheetah-033.jpg

Right image URL: http://africanhuntingsafaris.com/wp-content/uploads/2013/02/hunting-cheetah-025.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='Is a person holding up a leopard?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='Is a person holding up a leopard?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is a person holding up a leopard?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True


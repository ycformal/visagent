Question: In the image to the right, you will only see one dog.

Reference Answer: True

Left image URL: https://www.capitalfm.co.ke/radio/files/2014/06/pugs.jpg

Right image URL: https://i.ytimg.com/vi/YlPEDBPw-Dw/hqdefault.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='How many dogs are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} == 1')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='How many dogs are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} == 1')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many dogs are in the image?')=<b><span style='color: green;'>1</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 == 1")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="1 == 1")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True


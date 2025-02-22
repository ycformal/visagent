Question: The left image contains at least two chimpanzees.

Reference Answer: True

Left image URL: http://whozoo.org/Anlife99/sheclark/ThreeChimps083102_199C.jpg

Right image URL: https://i.ytimg.com/vi/ufBovI-Kuuo/maxresdefault.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='How many chimpanzees are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} >= 2')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='How many chimpanzees are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} >= 2')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many chimpanzees are in the image?')=<b><span style='color: green;'>3</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 >= 2")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="3 >= 2")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True


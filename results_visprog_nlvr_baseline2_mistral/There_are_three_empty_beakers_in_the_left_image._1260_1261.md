Question: There are three empty beakers in the left image.

Reference Answer: True

Left image URL: https://i.pinimg.com/originals/28/0e/3b/280e3bf1aceb988ec1fae71c5dedfaf1.jpg

Right image URL: https://static1.squarespace.com/static/587db7351b631be781c97189/588422463e00beae85d67a56/58842a18893fc0ce706797f6/1509410593602/?format=1000w

Original program:

```
ANSWER0=VQA(image=LEFT,question='How many empty beakers are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} == 3')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='How many empty beakers are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} == 3')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many empty beakers are in the image?')=<b><span style='color: green;'>1</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 == 3")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="1 == 3")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False


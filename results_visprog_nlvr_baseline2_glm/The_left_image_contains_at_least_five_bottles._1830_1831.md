Question: The left image contains at least five bottles.

Reference Answer: True

Left image URL: https://mollygjames.files.wordpress.com/2013/06/codd-neck_soda_bottles.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/df/e9/3d/dfe93da9f3651c352323206fde777c1b.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='How many bottles are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} >= 5')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='How many bottles are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} >= 5')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many bottles are in the image?')=<b><span style='color: green;'>30</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 >= 5")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="30 >= 5")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True


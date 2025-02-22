Question: The left image contains two dogs.

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/aa/dd/67/aadd67c3d7559caeff2492afe60d2d6e--afghans-afghan-hound.jpg

Right image URL: http://static2.bigstockphoto.com/thumbs/7/6/1/large1500/167236334.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='How many dogs are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} == 2')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='How many dogs are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} == 2')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many dogs are in the image?')=<b><span style='color: green;'>2</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 == 2")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="2 == 2")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True


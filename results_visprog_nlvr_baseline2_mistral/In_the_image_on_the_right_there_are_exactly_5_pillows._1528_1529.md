Question: In the image on the right there are exactly 5 pillows.

Reference Answer: False

Left image URL: https://s-media-cache-ak0.pinimg.com/236x/fd/69/44/fd6944a763c3faf55faa9970c35cd373.jpg

Right image URL: https://euimages.urbanoutfitters.com/is/image/UrbanOutfittersEU/5532436280030_000_b?$xlarge$&hei=900&fit=constrain

Original program:

```
ANSWER0=VQA(image=RIGHT,question='How many pillows are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} == 5')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='How many pillows are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} == 5')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many pillows are in the image?')=<b><span style='color: green;'>3</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 == 5")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="3 == 5")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False


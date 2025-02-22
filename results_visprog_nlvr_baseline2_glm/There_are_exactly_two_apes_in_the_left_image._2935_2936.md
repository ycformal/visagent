Question: There are exactly two apes in the left image.

Reference Answer: True

Left image URL: https://photos.smugmug.com/Travel/Mountain-Gorillas/i-v9zMBHc/0/143d6e0d/S/00495%20%2B%20Two%20gorillas%20facing%20the%20camera%2C%20Parc%20National%20des%20Volcans%2C%20Rwanda-S.jpg

Right image URL: http://photos.wildjunket.com/Africa/Uganda/Bwindi-Impenetrable-Forest/i-pS2JpQk/0/M/2013-10-11%20at%2016-37-22-M.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='How many apes are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} == 2')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='How many apes are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} == 2')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many apes are in the image?')=<b><span style='color: green;'>2</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 == 2")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="2 == 2")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True


Question: The main sails are white in the left image.

Reference Answer: False

Left image URL: https://www.coastandcountry.co.uk/wp-content/uploads/2013/08/Sailing-on-Salcombe-harbour-690.jpg

Right image URL: https://boxstuff-development-thumbnails.s3.amazonaws.com/521453_1024x400f.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='Are the main sails white?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='Are the main sails white?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Are the main sails white?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="False")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False


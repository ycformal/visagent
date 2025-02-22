Question: The right image contains no more than one seal.

Reference Answer: True

Left image URL: http://ecuadordolhansky.weebly.com/uploads/5/2/1/2/52128781/1071630_orig.jpg

Right image URL: https://i.pinimg.com/736x/3a/7f/05/3a7f05f403b50fc5cef40bde74c8fd78--slovenia-sea-lions.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='How many seals are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} <= 1')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='How many seals are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} <= 1')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many seals are in the image?')=<b><span style='color: green;'>1</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 <= 1")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="1 <= 1")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True


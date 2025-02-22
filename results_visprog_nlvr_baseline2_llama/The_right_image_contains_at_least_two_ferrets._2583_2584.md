Question: The right image contains at least two ferrets.

Reference Answer: True

Left image URL: http://cdn.dogwork.com/thumbnails/baby-ferrets-large.jpg

Right image URL: https://ferretworld1.files.wordpress.com/2010/12/first-photos-096.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='How many ferrets are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} >= 2')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='How many ferrets are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} >= 2')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many ferrets are in the image?')=<b><span style='color: green;'>2</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 >= 2")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="2 >= 2")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True


Question: The right image features one slope-front stainless steel sink mounted on the wall on the left.

Reference Answer: True

Left image URL: http://www.kavika.fi/wp-content/uploads/2015/10/Artikkelikuva7110b.jpg

Right image URL: http://www.hosser.ru/sites/default/files/mkdc_kazan_10.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='Does the image feature one slope-front stainless steel sink mounted on the wall on the left?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='Does the image feature one slope-front stainless steel sink mounted on the wall on the left?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Does the image feature one slope-front stainless steel sink mounted on the wall on the left?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True


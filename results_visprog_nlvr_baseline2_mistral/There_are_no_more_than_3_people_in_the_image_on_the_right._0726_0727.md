Question: There are no more than 3 people in the image on the right.

Reference Answer: False

Left image URL: https://media-cdn.tripadvisor.com/media/photo-s/09/62/0a/6a/foyles-bookshop.jpg

Right image URL: https://eddieolliffe.files.wordpress.com/2014/06/wp_20140611_008.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='How many people are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} <= 3')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='How many people are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} <= 3')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many people are in the image?')=<b><span style='color: green;'>10</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 <= 3")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="10 <= 3")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False


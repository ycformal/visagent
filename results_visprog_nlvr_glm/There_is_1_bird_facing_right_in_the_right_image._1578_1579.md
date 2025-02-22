Question: There is 1 bird facing right in the right image.

Reference Answer: False

Left image URL: https://gmenchaca821.files.wordpress.com/2014/03/american-pelican.jpg

Right image URL: http://i0.kym-cdn.com/photos/images/original/001/221/831/ba9.png

Program:

```
ANSWER0=VQA(image=RIGHT,question='How many birds are facing right?')
ANSWER1=EVAL(expr='{ANSWER0} == 1')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many birds are facing right?')=<b><span style='color: green;'>1</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 == 1")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="1 == 1")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True


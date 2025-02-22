Question: The right image contains no more than one dead water buffalo.

Reference Answer: True

Left image URL: https://t4.ftcdn.net/jpg/00/89/26/03/240_F_89260355_syk4xthMGLqbRBsckmBamylex0SPgD0P.jpg

Right image URL: http://news.bbcimg.co.uk/media/images/63144000/jpg/_63144802_c2f2fdc7-b417-46e8-907c-ebf579a45bd2.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='How many dead water buffaloes are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} <= 1')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='How many dead water buffaloes are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} <= 1')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many dead water buffaloes are in the image?')=<b><span style='color: green;'>1</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 <= 1")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="1 <= 1")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True


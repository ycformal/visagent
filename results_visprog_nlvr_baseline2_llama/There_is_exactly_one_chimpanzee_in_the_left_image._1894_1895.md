Question: There is exactly one chimpanzee in the left image.

Reference Answer: True

Left image URL: http://i.dailymail.co.uk/i/pix/2013/02/20/article-2281527-17EAE611000005DC-614_634x541.jpg

Right image URL: https://i.ytimg.com/vi/ZlVICsSIASc/maxresdefault.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='How many chimpanzees are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} == 1')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='How many chimpanzees are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} == 1')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many chimpanzees are in the image?')=<b><span style='color: green;'>1</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 == 1")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="1 == 1")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True


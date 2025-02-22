Question: In the image to the right, you can see the person's fingers.

Reference Answer: False

Left image URL: https://media-cdn.tripadvisor.com/media/photo-s/07/b5/7e/8e/seaworld-orlando.jpg

Right image URL: https://media-cdn.tripadvisor.com/media/photo-s/02/79/5e/89/filename-sea-world-1.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='Can you see the person's fingers?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='Can you see the person's fingers?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Can you see the person')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True


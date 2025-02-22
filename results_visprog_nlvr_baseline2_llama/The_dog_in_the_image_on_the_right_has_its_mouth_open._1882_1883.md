Question: The dog in the image on the right has its mouth open.

Reference Answer: True

Left image URL: https://s-media-cache-ak0.pinimg.com/736x/a6/61/84/a661840d19c2801e5b8ae780b7f1547b--old-dogs-black-wolves.jpg

Right image URL: https://howlingforjustice.files.wordpress.com/2012/04/black-wolf-pup1.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='Is the dog's mouth open?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='Is the dog's mouth open?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is the dog')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="False")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False


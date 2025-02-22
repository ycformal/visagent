Question: there is a human in the left side pic

Reference Answer: False

Left image URL: https://www.wikihow.com/images/d/de/Build-a-Plywood-Canoe-Intro.jpg

Right image URL: https://photos.smugmug.com/Boats/Home-Built-Canoes-and-Paddles/i-RKLgZzH/0/45378e8a/L/snowshoe12_spring2-L.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='Is there a human in the image?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='Is there a human in the image?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is there a human in the image?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="False")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False


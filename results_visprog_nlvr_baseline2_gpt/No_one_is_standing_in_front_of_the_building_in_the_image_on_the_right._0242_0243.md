Question: No one is standing in front of the building in the image on the right.

Reference Answer: False

Left image URL: https://i0.wp.com/www.onceinalifetimejourney.com/wp-content/uploads/2017/06/drepung-gomang-monastery-194760_1280.jpg?resize=1280%2C853&ssl=1

Right image URL: https://truthaboutshugden.files.wordpress.com/2010/01/screen-shot-2010-01-26-at-1-00-53-pm.png

Original program:

```
ANSWER0=VQA(image=RIGHT,question='Is anyone standing in front of the building?')
ANSWER1=EVAL(expr='not {ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='Is anyone standing in front of the building?')
ANSWER1=EVAL(expr='not {ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is anyone standing in front of the building?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="not ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="not True")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False


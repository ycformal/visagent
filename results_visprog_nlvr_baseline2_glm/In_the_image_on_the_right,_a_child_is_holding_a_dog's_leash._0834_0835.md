Question: In the image on the right, a child is holding a dog's leash.

Reference Answer: True

Left image URL: http://www.gentlegiantsrescue-great-pyrenees.com/Images2/Princess%20Leah%20and%20family%201%20cropped%20452%20arrow.jpg

Right image URL: http://img.photobucket.com/albums/v672/WJTH05/Great%20Pyrenees/HannahAndKeeper.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='Is a child holding a dog\'s leash?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='Is a child holding a dog\'s leash?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is a child holding a dog's leash?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True


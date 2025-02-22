Question: The sink in the image on the right is not mounted onto a counter.

Reference Answer: True

Left image URL: https://media-cdn.tripadvisor.com/media/photo-s/05/30/24/f0/piece-hostel-kyoto.jpg

Right image URL: https://media-cdn.tripadvisor.com/media/photo-s/01/5e/d7/ac/single-room-without-en.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='Is the sink mounted onto a counter?')
ANSWER1=EVAL(expr='not {ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='Is the sink mounted onto a counter?')
ANSWER1=EVAL(expr='not {ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is the sink mounted onto a counter?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="not ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="not False")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True


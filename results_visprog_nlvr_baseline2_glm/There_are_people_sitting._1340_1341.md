Question: There are people sitting.

Reference Answer: True

Left image URL: https://media-cdn.tripadvisor.com/media/photo-s/10/61/49/67/the-dutch-eating-place.jpg

Right image URL: http://media.nj.com/route_45/photo/reading-market-2jpg-a59e0839446db5c6.jpg

Original program:

```
Statement: There are people sitting.
Program:
ANSWER0=VQA(image=LEFT,question='Are there people sitting?')
ANSWER1=VQA(image=RIGHT,question='Are there people sitting?')
ANSWER2=EVAL(expr='{ANSWER0} or {ANSWER1}')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There are people sitting.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are people sitting.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true


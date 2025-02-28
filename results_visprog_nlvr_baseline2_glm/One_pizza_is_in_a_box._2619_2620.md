Question: One pizza is in a box.

Reference Answer: True

Left image URL: https://s3-media1.fl.yelpcdn.com/bphoto/PbS1RUQBuPzUo4BEMQSUIQ/348s.jpg

Right image URL: https://media-cdn.tripadvisor.com/media/photo-s/06/e5/fd/b5/margherita-pizza-with.jpg

Original program:

```
Statement: One pizza is in a box.
Program:
ANSWER0=VQA(image=LEFT,question='Is there a pizza in a box?')
ANSWER1=VQA(image=RIGHT,question='Is there a pizza in a box?')
ANSWER2=EVAL(expr='{ANSWER0} xor {ANSWER1}')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'One pizza is in a box.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One pizza is in a box.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true


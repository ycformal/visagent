Question: There is a warthog laying down.

Reference Answer: False

Left image URL: https://media-cdn.tripadvisor.com/media/photo-s/02/b4/fa/e5/haller-park.jpg

Right image URL: http://www.paesieimmagini.it/Kenya/Imm_Kenya/Kenya08-0049.jpg

Original program:

```
Statement: There is a warthog laying down.
Program:
ANSWER0=VQA(image=LEFT,question='How many warthogs are laying down?')
ANSWER1=VQA(image=RIGHT,question='How many warthogs are laying down?')
ANSWER2=EVAL(expr='{ANSWER0} + {ANSWER1} == 1')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There is a warthog laying down.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There is a warthog laying down.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false


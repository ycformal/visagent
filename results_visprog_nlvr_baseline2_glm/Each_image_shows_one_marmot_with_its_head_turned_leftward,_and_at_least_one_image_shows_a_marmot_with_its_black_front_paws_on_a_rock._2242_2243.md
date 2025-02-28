Question: Each image shows one marmot with its head turned leftward, and at least one image shows a marmot with its black front paws on a rock.

Reference Answer: False

Left image URL: https://i.ytimg.com/vi/oPlqlmGTuQ8/maxresdefault.jpg

Right image URL: http://www.nhptv.org/wild/images/hoarymarmotforestryalfredviola3.jpg

Original program:

```
Statement: An image shows one bare hand with the thumb on the right holding up a belly-first, head-up crab, with water in the background.
Program:
ANSWER0=VQA(image=LEFT,question='Does the image shows one bare hand with the thumb on the right holding a crab?')
ANSWER1=VQA(image=RIGHT,question='Does the image shows one bare hand with the thumb on the right holding a crab?')
ANSWER2=VQA(image=LEFT,question='Is the crab belly-first and head-ups?')
ANSWER3=VQA(image=RIGHT,question='Is the crab belly-first and head-ups?')
ANSWER4=VQA(image=LEFT,question='Is there water in the background?')
ANSWER5=VQA(image=RIGHT,question='Is there water in the background?')
ANSWER6=EVAL(expr='{ANSWER0} and {ANSWER2} and {ANSWER4}')
ANSWER7=EVAL(expr='{ANSWER1} and {ANSWER3} and {ANSWER5}')
ANSWER8=EVAL(expr='{ANSWER6} xor {ANSWER7}')
FINAL_ANSWER=RESULT(var=ANSWER8)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'Each image shows one marmot with its head turned leftward, and at least one image shows a marmot with its black front paws on a rock.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image shows one marmot with its head turned leftward, and at least one image shows a marmot with its black front paws on a rock.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True


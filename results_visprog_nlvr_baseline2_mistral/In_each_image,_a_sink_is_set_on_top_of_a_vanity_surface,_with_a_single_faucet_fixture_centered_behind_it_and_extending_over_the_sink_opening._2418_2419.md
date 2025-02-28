Question: In each image, a sink is set on top of a vanity surface, with a single faucet fixture centered behind it and extending over the sink opening.

Reference Answer: True

Left image URL: https://images-na.ssl-images-amazon.com/images/I/810dyS0VvIL._SX355_.jpg

Right image URL: http://buyspectra.com/uploads/category/relatedimages/stone_wash_basins_rp3.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='Is a sink set on top of a vanity surface?')
ANSWER1=VQA(image=RIGHT,question='Is a sink set on top of a vanity surface?')
ANSWER2=VQA(image=LEFT,question='Is a single faucet fixture centered behind the sink?')
ANSWER3=VQA(image=RIGHT,question='Is a single faucet fixture centered behind the sink?')
ANSWER4=VQA(image=LEFT,question='Does the faucet fixture extend over the sink opening?')
ANSWER5=VQA(image=RIGHT,question='Does the faucet fixture extend over the sink opening?')
ANSWER6=EVAL(expr='{ANSWER0} and {ANSWER2} and {ANSWER4}')
ANSWER7=EVAL(expr='{ANSWER1} and {ANSWER3} and {ANSWER5}')
ANSWER8=EVAL(expr='{ANSWER6} and {ANSWER7}')
FINAL_ANSWER=
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'In each image, a sink is set on top of a vanity surface, with a single faucet fixture centered behind it and extending over the sink opening.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In each image, a sink is set on top of a vanity surface, with a single faucet fixture centered behind it and extending over the sink opening.' true or false?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: False


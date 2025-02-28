Question: No image shows broccoli in a container, and the right image contains exactly two cut pieces of broccoli.

Reference Answer: True

Left image URL: https://st2.depositphotos.com/4366637/9571/i/450/depositphotos_95716846-stock-photo-some-green-brocolis-over-a.jpg

Right image URL: https://static.cuisineaz.com/680x357/i101506-le-brocoli.jpg

Original program:

```
Statement: No image shows broccoli in a container, and the right image contains exactly two cut pieces of broccoli.
Program:
ANSWER0=VQA(image=LEFT,question='Is the broccoli in a container?')
ANSWER1=VQA(image=RIGHT,question='Is the broccoli in a container?')
ANSWER2=VQA(image=LEFT,question='How many pieces of broccoli are there?')
ANSWER3=VQA(image=RIGHT,question='How many pieces of broccoli are there?')
ANSWER4=EVAL(expr='{ANSWER0} and {ANSWER1}')
ANSWER5=EVAL(expr='{ANSWER2} == 0 and {ANSWER3} == 2')
ANSWER6=EVAL(expr='{ANSWER4} and {ANSWER5}')
FINAL_ANSWER=RESULT(var=ANSWER6)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'No image shows broccoli in a container, and the right image contains exactly two cut pieces of broccoli.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'No image shows broccoli in a container, and the right image contains exactly two cut pieces of broccoli.' true or false?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: False


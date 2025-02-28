Question: One image features a forward-angled flat-front bus, the other features a forward angled bus with a non-flat front, and the buses in the left and right images appear to face each other.

Reference Answer: True

Left image URL: https://i.ytimg.com/vi/Br5RWNF_Trc/maxresdefault.jpg

Right image URL: https://i.ytimg.com/vi/5KucVQsawXE/hqdefault.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='Is the bus forward-angled and flat-front?')
ANSWER1=VQA(image=RIGHT,question='Is the bus forward-angled and flat-front?')
ANSWER2=EVAL(expr='{ANSWER0} xor {ANSWER1}')
ANSWER3=VQA(image=LEFT,question='Is the bus forward-angled and non-flat-front?')
ANSWER4=VQA(image=RIGHT,question='Is the bus forward-angled and non-flat-front?')
ANSWER5=EVAL(expr='{ANSWER3} xor {ANSWER4}')
ANSWER6=VQA(image=LEFT,question='Is the bus facing the other bus?')
ANSWER7=VQA(image=RIGHT,question='Is the bus facing the other bus?')
ANSWER8=EVAL(expr='{ANSWER6} and {ANSWER7}')
ANSWER9=EVAL(expr='{ANSWER2} and {ANSWER5} and {ANSWER8}')
FINAL_
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'One image features a forward-angled flat-front bus, the other features a forward angled bus with a non-flat front, and the buses in the left and right images appear to face each other.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image features a forward-angled flat-front bus, the other features a forward angled bus with a non-flat front, and the buses in the left and right images appear to face each other.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True


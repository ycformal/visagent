Question: One of the dogs has a red jacket

Reference Answer: True

Left image URL: https://i.ytimg.com/vi/509LT3ND6xY/hqdefault.jpg

Right image URL: http://www.schnauzers-rule.com/images/miniature-schnauzer-evie-21435699.jpg

Original program:

```
Statement: One of the dogs has a red jacket
Program:
ANSWER0=VQA(image=LEFT,question='Does the dog have a red jacket?')
ANSWER1=VQA(image=RIGHT,question='Does the dog have a red jacket?')
ANSWER2=EVAL(expr='{ANSWER0} xor {ANSWER1}')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True


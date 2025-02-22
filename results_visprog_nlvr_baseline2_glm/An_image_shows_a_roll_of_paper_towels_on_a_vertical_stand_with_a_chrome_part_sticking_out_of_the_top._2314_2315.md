Question: An image shows a roll of paper towels on a vertical stand with a chrome part sticking out of the top.

Reference Answer: False

Left image URL: https://i.pinimg.com/736x/ca/fc/d9/cafcd9dadf0ca3057444ec732ec7729f--paper-towels-toilet-paper.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/30/b7/38/30b738c6e4aba44a11531d7396c968e9.jpg

Original program:

```
Statement: An image shows a roll of paper towels on a vertical stand with a chrome part sticking out of the top.
Program:
ANSWER0=VQA(image=LEFT,question='Is there a roll of paper towels on a vertical stand?')
ANSWER1=VQA(image=RIGHT,question='Is there a roll of paper towels on a vertical stand?')
ANSWER2=VQA(image=LEFT,question='Is there a chrome part sticking out of the top?')
ANSWER3=VQA(image=RIGHT,question='Is there a chrome part sticking out of the top?')
ANSWER4=EVAL(expr='{ANSWER0} and {ANSWER2}')
ANSWER5=EVAL(expr='{ANSWER1} and {ANSWER3}')
ANSWER6=EVAL(expr='{ANSWER4} xor {ANSWER5}')
FINAL_ANSWER=RESULT(var=ANSWER6)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True


Question: A dog is laying on its back

Reference Answer: True

Left image URL: https://s-media-cache-ak0.pinimg.com/736x/04/98/c9/0498c9032023c048d69299e6d25831fc--vizsla-dog-weimaraner.jpg

Right image URL: https://i.pinimg.com/736x/0b/34/47/0b34475a37c77e25e60881e7e98b2a5c--blue-weimaraner-vizsla-dog.jpg

Original program:

```
Statement: A dog is laying on its back
Program:
ANSWER0=VQA(image=LEFT,question='Is the dog laying on its back?')
ANSWER1=VQA(image=RIGHT,question='Is the dog laying on its back?')
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


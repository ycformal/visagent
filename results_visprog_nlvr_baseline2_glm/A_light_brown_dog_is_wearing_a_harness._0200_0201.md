Question: A light brown dog is wearing a harness.

Reference Answer: True

Left image URL: https://www.fordogtrainers.com/images/large/Cocer-spaniel-dog-harness-american-spaniel_LRG.jpg

Right image URL: http://cdn.akc.org/CockerSpHist5.jpg

Original program:

```
Statement: A light brown dog is wearing a harness.
Program:
ANSWER0=VQA(image=LEFT,question='Is the dog light brown?')
ANSWER1=VQA(image=RIGHT,question='Is the dog light brown?')
ANSWER2=VQA(image=LEFT,question='Is the dog wearing a harness?')
ANSWER3=VQA(image=RIGHT,question='Is the dog wearing a harness?')
ANSWER4=EVAL(expr='{ANSWER0} and {ANSWER2}')
ANSWER5=EVAL(expr='{ANSWER1} and {ANSWER3}')
ANSWER6=EVAL(expr='{ANSWER4} xor {ANSWER5}')
FINAL_ANSWER=RESULT(var=ANSWER6)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'A light brown dog is wearing a harness.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'A light brown dog is wearing a harness.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true


Question: There are more than 4 monkeys in the forest.

Reference Answer: False

Left image URL: https://media2.wnyc.org/i/800/0/c/99/nprproxy/411748170

Right image URL: https://i.pinimg.com/736x/1b/2e/80/1b2e80176e496a9dba13ff1f108cb0a9--baby-chimpanzee-jane-goodall.jpg

Original program:

```
Statement: There are more than 4 monkeys in the forest.
Program:
ANSWER0=VQA(image=LEFT,question='How many monkeys are in the forest?')
ANSWER1=VQA(image=RIGHT,question='How many monkeys are in the forest?')
ANSWER2=EVAL(expr='{ANSWER0} + {ANSWER1} > 4')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There are more than 4 monkeys in the forest.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are more than 4 monkeys in the forest.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true


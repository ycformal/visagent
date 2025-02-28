Question: A large white dog is sleeping on the floor with his tongue hanging out.

Reference Answer: False

Left image URL: https://i.pinimg.com/736x/a1/08/91/a108911cbac9520704562a62cd4e1e68--baby-goats-dog-baby.jpg

Right image URL: https://iheartdogs.com/wp-content/uploads/2015/05/15-16382127582_40097da3a4_z.jpg

Original program:

```
Statement: A large white dog is sleeping on the floor with his tongue hanging out.
Program:
ANSWER0=VQA(image=LEFT,question='Is the dog large and white?')
ANSWER1=VQA(image=RIGHT,question='Is the dog large and white?')
ANSWER2=VQA(image=LEFT,question='Is the dog sleeping on the floor?')
ANSWER3=VQA(image=RIGHT,question='Is the dog sleeping on the floor?')
ANSWER4=VQA(image=LEFT,question='Is the dog\'s tongue hanging out?')
ANSWER5=VQA(image=RIGHT,question='Is the dog\'s tongue hanging out?')
ANSWER6=EVAL(expr='{ANSWER0} and {ANSWER2} and {ANSWER4}')
ANSWER7=EVAL(expr='{ANSWER1} and {ANSWER3} and {ANSWER5}')
ANSWER8=EVAL(expr='{ANSWER6} xor {ANSWER7}')
FINAL_ANSWER=RESULT(var=ANSWER8)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'A large white dog is sleeping on the floor with his tongue hanging out.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'A large white dog is sleeping on the floor with his tongue hanging out.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false


Question: There are both gray and white section of  fur on a single wolf whose body is facing right with their head tilted left forward.

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/8c/ab/bb/8cabbbcfffb34fd342baff85d96a288a--mexicans-wolf-life.jpg

Right image URL: http://www.tendua.org/IMG/jpg/tendua-dsc_0934-portrait_loup.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='How many wolves are in the image?')
ANSWER1=VQA(image=RIGHT,question='How many wolves are in the image?')
ANSWER2=VQA(image=LEFT,question='Are there both gray and white section of fur on the wolf?')
ANSWER3=VQA(image=RIGHT,question='Are there both gray and white section of fur on the wolf?')
ANSWER4=VQA(image=LEFT,question='Is the wolf's body facing right with their head tilted left forward?')
ANSWER5=VQA(image=RIGHT,question='Is the wolf's body facing right with their head tilted left forward?')
ANSWER6=EVAL(expr='{ANSWER0} == 1 and {ANSWER2} and {ANSWER4}')
ANSWER7=EVAL(expr='{ANSWER1} == 1 and {ANSWER3} and {ANSWER5}')
ANSWER8=EVAL(expr='{ANSWER6} xor {ANSWER7}')
FINAL_
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True


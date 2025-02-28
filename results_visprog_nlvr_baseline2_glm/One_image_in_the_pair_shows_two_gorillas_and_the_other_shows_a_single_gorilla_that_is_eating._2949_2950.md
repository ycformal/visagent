Question: One image in the pair shows two gorillas and the other shows a single gorilla that is eating.

Reference Answer: True

Left image URL: http://pbs.twimg.com/media/CIclVBsWgAAL0RT.jpg

Right image URL: http://i.dailymail.co.uk/i/pix/2016/04/19/12/326F4A1700000578-3547585-image-a-1_1461064440559.jpg

Original program:

```
Statement: One image in the pair shows two gorillas and the other shows a single gorilla that is eating.
Program:
ANSWER0=VQA(image=LEFT,question='How many gorillas are in the image?')
ANSWER1=VQA(image=RIGHT,question='How many gorillas are in the image?')
ANSWER2=VQA(image=LEFT,question='Is the gorilla eating?')
ANSWER3=VQA(image=RIGHT,question='Is the gorilla eating?')
ANSWER4=EVAL(expr='{ANSWER0} == 2 and {ANSWER2}')
ANSWER5=EVAL(expr='{ANSWER1} == 1 and {ANSWER3}')
ANSWER6=EVAL(expr='{ANSWER4} xor {ANSWER5}')
FINAL_ANSWER=RESULT(var=ANSWER6)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'One image in the pair shows two gorillas and the other shows a single gorilla that is eating.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image in the pair shows two gorillas and the other shows a single gorilla that is eating.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false


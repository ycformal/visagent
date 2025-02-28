Question: A cheetah is lying directly on some grass next to a human female.

Reference Answer: False

Left image URL: https://i.ytimg.com/vi/9HtAOJXZQ2I/maxresdefault.jpg

Right image URL: http://img.izismile.com/img/img8/20150407/640/the_girl_who_is_friends_with_a_cheetah_640_12.jpg

Original program:

```
Statement: A cheetah is lying directly on some grass next to a human female.
Program:
ANSWER0=VQA(image=LEFT,question='Is a cheetah lying directly on some grass?')
ANSWER1=VQA(image=RIGHT,question='Is a cheetah lying directly on some grass?')
ANSWER2=VQA(image=LEFT,question='Is the cheetah next to a human female?')
ANSWER3=VQA(image=RIGHT,question='Is the cheetah next to a human female?')
ANSWER4=EVAL(expr='{ANSWER0} and {ANSWER2}')
ANSWER5=EVAL(expr='{ANSWER1} and {ANSWER3}')
ANSWER6=EVAL(expr='{ANSWER4} xor {ANSWER5}')
FINAL_ANSWER=RESULT(var=ANSWER6)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'A cheetah is lying directly on some grass next to a human female.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'A cheetah is lying directly on some grass next to a human female.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false


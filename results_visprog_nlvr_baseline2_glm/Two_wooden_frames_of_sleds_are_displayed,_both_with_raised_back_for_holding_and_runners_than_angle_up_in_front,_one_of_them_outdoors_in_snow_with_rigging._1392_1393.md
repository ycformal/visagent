Question: Two wooden frames of sleds are displayed, both with raised back for holding and runners than angle up in front, one of them outdoors in snow with rigging.

Reference Answer: True

Left image URL: https://s-media-cache-ak0.pinimg.com/originals/17/0f/28/170f28141439f36cd91a3589ace42392.jpg

Right image URL: https://i.pinimg.com/736x/10/cc/f8/10ccf8de067a5515f2a5602a61a840e9--sled-shelters.jpg

Original program:

```
Statement: An image shows one bare hand with the thumb on the right holding up a belly-first, head-up crab, with water in the background.
Program:
ANSWER0=VQA(image=LEFT,question='Does the image shows one bare hand with the thumb on the right holding a crab?')
ANSWER1=VQA(image=RIGHT,question='Does the image shows one bare hand with the thumb on the right holding a crab?')
ANSWER2=VQA(image=LEFT,question='Is the crab belly-first and head-ups?')
ANSWER3=VQA(image=RIGHT,question='Is the crab belly-first and head-ups?')
ANSWER4=VQA(image=LEFT,question='Is there water in the background?')
ANSWER5=VQA(image=RIGHT,question='Is there water in the background?')
ANSWER6=EVAL(expr='{ANSWER0} and {ANSWER2} and {ANSWER4}')
ANSWER7=EVAL(expr='{ANSWER1} and {ANSWER3} and {ANSWER5}')
ANSWER8=EVAL(expr='{ANSWER6} xor {ANSWER7}')
FINAL_ANSWER=RESULT(var=ANSWER8)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'Two wooden frames of sleds are displayed, both with raised back for holding and runners than angle up in front, one of them outdoors in snow with rigging.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Two wooden frames of sleds are displayed, both with raised back for holding and runners than angle up in front, one of them outdoors in snow with rigging.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True


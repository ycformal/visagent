Question: An image shows part of a starfish alongside a jellyfish, and both are peachy-colored.

Reference Answer: False

Left image URL: https://s-media-cache-ak0.pinimg.com/originals/2e/c1/e9/2ec1e9a8984ae89792902dc50cae7db1.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/94/1c/58/941c58f5b227e4216c4ed26647137c5a.jpg

Original program:

```
Statement: An image shows part of a starfish alongside a jellyfish, and both are peachy-colored.
Program:
ANSWER0=VQA(image=LEFT,question='Is there a starfish in the image?')
ANSWER1=VQA(image=RIGHT,question='Is there a starfish in the image?')
ANSWER2=VQA(image=LEFT,question='Is there a jellyfish in the image?')
ANSWER3=VQA(image=RIGHT,question='Is there a jellyfish in the image?')
ANSWER4=VQA(image=LEFT,question='Is the starfish peachy-colored?')
ANSWER5=VQA(image=RIGHT,question='Is the starfish peachy-colored?')
ANSWER6=VQA(image=LEFT,question='Is the jellyfish peachy-colored?')
ANSWER7=VQA(image=RIGHT,question='Is the jellyfish peachy-colored?')
ANSWER8=EVAL(expr='{ANSWER0} and {ANSWER2} and {ANSWER4} and {ANSWER6}')
ANSWER9=EVAL(expr='{ANSWER1} and {ANSWER3} and {ANSWER5} and {ANSWER7}')
ANSWER
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'An image shows part of a starfish alongside a jellyfish, and both are peachy-colored.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'An image shows part of a starfish alongside a jellyfish, and both are peachy-colored.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false


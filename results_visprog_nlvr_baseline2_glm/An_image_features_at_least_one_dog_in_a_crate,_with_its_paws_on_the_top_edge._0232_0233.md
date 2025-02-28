Question: An image features at least one dog in a crate, with its paws on the top edge.

Reference Answer: False

Left image URL: http://www.milrocbeagles.com/sitebuilder/images/10988467_10206459325150490_6323999478497309567_n-288x251.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/79/a4/39/79a4393181e9e6b0d984dd378586ee65.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'An image features at least one dog in a crate, with its paws on the top edge.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'An image features at least one dog in a crate, with its paws on the top edge.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true


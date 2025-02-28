Question: One image depicts a single orange jellyfish with downward-trailing tentacles, and the other image includes at least two jellyfish with orange 'caps'.

Reference Answer: True

Left image URL: http://www.artofexcellencestudio.com/uploads/1/2/1/0/12107572/789044_orig.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/39/42/3e/39423e8e831004d8b0036d9dab18d730.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'One image depicts a single orange jellyfish with downward-trailing tentacles, and the other image includes at least two jellyfish with orange 'caps'.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image depicts a single orange jellyfish with downward-trailing tentacles, and the other image includes at least two jellyfish with orange 'caps'.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True


Question: One image contains no more than two short-haired guinea pigs posed on a blue surface, and the other image shows a single long-haired brown-and-white guinea pig.

Reference Answer: True

Left image URL: http://2.bp.blogspot.com/-9bDe9rtCO3w/TprVX83iakI/AAAAAAAAELw/vhFymbvMcTM/s1600/molly8weeks2.jpg

Right image URL: http://lunapigcavies.weebly.com/uploads/8/4/3/5/8435185/milo-and-fudge-posing_5104793.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'One image contains no more than two short-haired guinea pigs posed on a blue surface, and the other image shows a single long-haired brown-and-white guinea pig.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image contains no more than two short-haired guinea pigs posed on a blue surface, and the other image shows a single long-haired brown-and-white guinea pig.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True


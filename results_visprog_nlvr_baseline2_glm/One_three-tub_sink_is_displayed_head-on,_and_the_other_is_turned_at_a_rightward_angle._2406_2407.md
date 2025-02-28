Question: One three-tub sink is displayed head-on, and the other is turned at a rightward angle.

Reference Answer: False

Left image URL: https://3.imimg.com/data3/CS/LK/MY-3662038/3sink-work-table-500x500.jpg

Right image URL: https://5.imimg.com/data5/UD/AK/MY-2/three-sink-unit-500x500.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'One three-tub sink is displayed head-on, and the other is turned at a rightward angle.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One three-tub sink is displayed head-on, and the other is turned at a rightward angle.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true


Question: There are exactly four birds perched on a branch in the pair of images.

Reference Answer: False

Left image URL: http://3.bp.blogspot.com/-5AEI3yyIDJM/UOVyEnGzy2I/AAAAAAAAI24/5c_5FNE6OCE/s1600/Rainbow+Lorikeet+11.jpg

Right image URL: http://off.oatleypark.com/wordpress/wp-content/uploads/2013/08/01.-Rainbow-Lorikeet.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'There are exactly four birds perched on a branch in the pair of images.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are exactly four birds perched on a branch in the pair of images.' true or false?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: False


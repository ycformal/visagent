Question: a pair of warthogs are facing each other with noses touching

Reference Answer: False

Left image URL: http://d1bbnjcim4wtri.cloudfront.net/wp-content/uploads/2015/07/16125342/warthog20.jpg

Right image URL: http://s3-eu-west-1.amazonaws.com/rhinoafrica-blog/wp-content/uploads/2017/02/warthog-mating-rituals.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'a pair of warthogs are facing each other with noses touching' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'a pair of warthogs are facing each other with noses touching' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true


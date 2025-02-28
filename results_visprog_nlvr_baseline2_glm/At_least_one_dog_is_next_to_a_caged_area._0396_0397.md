Question: At least one dog is next to a caged area.

Reference Answer: True

Left image URL: http://www.leonbergerclubnw.com/img/gallery/leos/gallery1_013.jpg

Right image URL: http://4.bp.blogspot.com/_ntLbk00Wps0/SkItAl45BWI/AAAAAAAAAYE/sifBmpZw41c/s400/anyawaterpups5b.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'At least one dog is next to a caged area.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'At least one dog is next to a caged area.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true


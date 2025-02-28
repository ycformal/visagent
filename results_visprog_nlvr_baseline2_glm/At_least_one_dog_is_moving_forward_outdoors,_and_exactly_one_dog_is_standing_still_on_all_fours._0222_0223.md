Question: At least one dog is moving forward outdoors, and exactly one dog is standing still on all fours.

Reference Answer: False

Left image URL: http://static.ddmcdn.com/en-us/apl/breedselector/images/breed-selector/dogs/breeds/beagle_05_lg.jpg

Right image URL: http://twistedsifter.files.wordpress.com/2011/01/i-got-you-dog-winking.jpg?w=798&h=565

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
ANSWER0=VQA(image=IMAGE,question="Is 'At least one dog is moving forward outdoors, and exactly one dog is standing still on all fours.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'At least one dog is moving forward outdoors, and exactly one dog is standing still on all fours.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true


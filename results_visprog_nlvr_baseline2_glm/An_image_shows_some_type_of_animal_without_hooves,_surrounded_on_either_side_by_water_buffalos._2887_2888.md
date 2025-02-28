Question: An image shows some type of animal without hooves, surrounded on either side by water buffalos.

Reference Answer: True

Left image URL: http://i.dailymail.co.uk/i/pix/2013/05/03/article-2319004-199A2B2B000005DC-295_634x443.jpg

Right image URL: http://fscomps.fotosearch.com/compc/ULY/ULY162/u13049875.jpg

Original program:

```
Statement: An image shows some type of animal without hooves, surrounded on either side by water buffalos.
Program:
ANSWER0=VQA(image=LEFT,question='Is the animal in the image without hooves?')
ANSWER1=VQA(image=RIGHT,question='Is the animal in the image without hooves?')
ANSWER2=VQA(image=LEFT,question='Are there water buffalos surrounding the animal on either side?')
ANSWER3=VQA(image=RIGHT,question='Are there water buffalos surrounding the animal on either side?')
ANSWER4=EVAL(expr='{ANSWER0} and {ANSWER2}')
ANSWER5=EVAL(expr='{ANSWER1} and {ANSWER3}')
ANSWER6=EVAL(expr='{ANSWER4} xor {ANSWER5}')
FINAL_ANSWER=RESULT(var=ANSWER6)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'An image shows some type of animal without hooves, surrounded on either side by water buffalos.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'An image shows some type of animal without hooves, surrounded on either side by water buffalos.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false


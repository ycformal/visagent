Question: A bird is in flight and flying towards the right in one of the images.

Reference Answer: True

Left image URL: http://3.bp.blogspot.com/-JqG1KLm1tiQ/UWP7pHMYMlI/AAAAAAAAA78/3ATtsQ9Uydg/s1600/Birds+HD+Wallpaper-01.jpg

Right image URL: http://4.bp.blogspot.com/_FAO6PzqtEKc/TNBoIS7cUOI/AAAAAAAAAU0/84Cwp9zzz0w/s1600/arara+canind%C3%A9.jpg

Original program:

```
Statement: A bird is in flight and flying towards the right in one of the images.
Program:
ANSWER0=VQA(image=LEFT,question='Is the bird in flight?')
ANSWER1=VQA(image=RIGHT,question='Is the bird in flight?')
ANSWER2=VQA(image=LEFT,question='Is the bird flying towards the right?')
ANSWER3=VQA(image=RIGHT,question='Is the bird flying towards the right?')
ANSWER4=EVAL(expr='{ANSWER0} and {ANSWER2}')
ANSWER5=EVAL(expr='{ANSWER1} and {ANSWER3}')
ANSWER6=EVAL(expr='{ANSWER4} xor {ANSWER5}')
FINAL_ANSWER=RESULT(var=ANSWER6)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'A bird is in flight and flying towards the right in one of the images.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'A bird is in flight and flying towards the right in one of the images.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false


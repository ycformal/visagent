Question: A single dog in the image on the right is running toward the camera.

Reference Answer: False

Left image URL: http://static.ddmcdn.com/en-us/apl/breedselector/images/breed-selector/dogs/breeds/beagle_05_lg.jpg

Right image URL: http://twistedsifter.files.wordpress.com/2011/01/i-got-you-dog-winking.jpg?w=798&h=565

Original program:

```
ANSWER0=VQA(image=RIGHT,question='Is the dog running toward the camera?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='Is the dog running toward the camera?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is the dog running toward the camera?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="False")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False


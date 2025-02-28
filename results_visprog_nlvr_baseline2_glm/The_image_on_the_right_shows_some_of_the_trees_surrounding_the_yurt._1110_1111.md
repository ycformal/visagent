Question: The image on the right shows some of the trees surrounding the yurt.

Reference Answer: False

Left image URL: https://howardmeyerson.files.wordpress.com/2015/01/084-craig-lake-yurt-m.jpg

Right image URL: http://media.mlive.com/muskegonchronicle/photo/12514938-large.jpg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The image on the right shows some of the trees surrounding the yurt.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The image on the right shows some of the trees surrounding the yurt.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True


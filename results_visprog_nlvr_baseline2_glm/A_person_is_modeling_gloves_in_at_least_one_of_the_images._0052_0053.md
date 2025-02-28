Question: A person is modeling gloves in at least one of the images.

Reference Answer: False

Left image URL: https://s-media-cache-ak0.pinimg.com/originals/99/19/10/9919104db00b731621206009aa935018.jpg

Right image URL: http://www.makeit-loveit.com/wp-content/uploads/2010/01/110.jpg

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'A person is modeling gloves in at least one of the images.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'A person is modeling gloves in at least one of the images.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false


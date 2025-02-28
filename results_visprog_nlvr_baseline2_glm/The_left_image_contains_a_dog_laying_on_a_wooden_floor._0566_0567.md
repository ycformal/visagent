Question: The left image contains a dog laying on a wooden floor.

Reference Answer: False

Left image URL: https://www.thesun.co.uk/wp-content/uploads/2016/04/2606540.main_image.jpg?strip=all

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/08/7f/87/087f87ca537d81debb0cb143528afb57.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='Is there a dog laying on a wooden floor?')
FINAL_ANSWER=RESULT(var=ANSWER0)The statement is True.
```
Program:

```
ANSWER0=VQA(image=LEFT,question='Is there a dog laying on a wooden floor?')
FINAL_ANSWER=RESULT(var=ANSWER0)The statement is True.
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is there a dog laying on a wooden floor?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: False


Question: The right image shows a person to the right of a white dog, with a hand on the dog's fur.

Reference Answer: False

Left image URL: http://cdn.akc.org/content/hero/pyreneesheader.jpg

Right image URL: https://media2.fdncms.com/orlando/imager/u/slideshow/2481129/dogs.jpg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The right image shows a person to the right of a white dog, with a hand on the dog's fur.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The right image shows a person to the right of a white dog, with a hand on the dog's fur.' true or false?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: False


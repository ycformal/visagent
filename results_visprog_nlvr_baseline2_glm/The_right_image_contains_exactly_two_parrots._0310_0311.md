Question: The right image contains exactly two parrots.

Reference Answer: True

Left image URL: http://www.pawsthemoment.com.au/wp-content/uploads/2015/04/PomPom3-BEST.jpg

Right image URL: https://naturallysouthaustralia.files.wordpress.com/2015/04/p1030399.jpg?w=490

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The right image contains exactly two parrots.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The right image contains exactly two parrots.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true


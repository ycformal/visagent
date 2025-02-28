Question: There is a red octopus.

Reference Answer: True

Left image URL: https://lh4.googleusercontent.com/-DlOZp25SXr4/UW4SvphfisI/AAAAAAAABuQ/BQ4M28dtNmU/s668/DSCI0828.JPG

Right image URL: https://i.pinimg.com/originals/e8/90/db/e890db22746b3457f092c165def1eff8.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There is a red octopus.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There is a red octopus.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false


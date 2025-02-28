Question: One image in the pair shows two gorillas and the other shows a single gorilla that is eating.

Reference Answer: True

Left image URL: http://www.bwindiforestnationalpark.com/wp-content/uploads/gorilla-feeding.jpg

Right image URL: https://gorillatreks.files.wordpress.com/2011/07/baby-gorilla.jpeg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'One image in the pair shows two gorillas and the other shows a single gorilla that is eating.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image in the pair shows two gorillas and the other shows a single gorilla that is eating.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false


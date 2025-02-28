Question: There are three ferrets.

Reference Answer: False

Left image URL: http://blog.ferplast.com/wp-content/uploads/2016/01/ferret-character-ferrets-sociable-friendly-kiss-toilet.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/2c/1d/4c/2c1d4cca6ff7d977c9bf7f701e68b160.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There are three ferrets.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are three ferrets.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true


Question: There are at least 4 gorillas sitting in the greenery.

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/de/41/3f/de413f315e14dec627b2377772a23fbc--mountain-gorilla-baby.jpg

Right image URL: http://www.lbah.com/images/RwandaTanzania2011/Rwanda/Gorillas/Babyplaying1.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There are at least 4 gorillas sitting in the greenery.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are at least 4 gorillas sitting in the greenery.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true


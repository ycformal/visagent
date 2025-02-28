Question: Each image contains one bluish vase with a flaring scallop-edged top and a shape that tapers at the bottom.

Reference Answer: True

Left image URL: http://katrinagalleries.com.au/wp-content/uploads/2013/05/072p.jpg

Right image URL: https://i.pinimg.com/736x/4c/a1/86/4ca186316074a67aa5505ee88461dcc3--vintage-pottery-cobalt-blue.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'Each image contains one bluish vase with a flaring scallop-edged top and a shape that tapers at the bottom.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image contains one bluish vase with a flaring scallop-edged top and a shape that tapers at the bottom.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True


Question: An image contains exactly three bikini models, all standing, wearing sunglasses and facing forward.

Reference Answer: False

Left image URL: https://get.wallhere.com/photo/women-model-blonde-water-brunette-smiling-fashion-bikini-group-of-women-swimwear-clothing-supermodel-beauty-leg-photo-shoot-spring-break-309515.jpg

Right image URL: http://img.soy-chile.cl/Fotos/2015/01/12/file_20150112131300.jpg

Original program:

```
The program provided is a series of steps to determine if a given statement is true or false based on the content of an image. Each statement is evaluated step by step using a combination of image analysis and logical expressions. The final answer is determined by evaluating the logical expression for each statement and returning the result.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'An image contains exactly three bikini models, all standing, wearing sunglasses and facing forward.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'An image contains exactly three bikini models, all standing, wearing sunglasses and facing forward.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false


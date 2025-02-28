Question: The stairway railings are all dark colored.

Reference Answer: False

Left image URL: https://i.pinimg.com/736x/cd/10/90/cd109065896b6c1f03d2f60821b4eb09--metal-stair-railing-stair-spindles.jpg

Right image URL: https://www.jacksonwoodturners.co.uk/media/catalog/category/newel-posts-category-main-image-2.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The stairway railings are all dark colored.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The stairway railings are all dark colored.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true


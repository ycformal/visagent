Question: The robed people in the image on the left are standing outside.

Reference Answer: False

Left image URL: https://www.sgc.sa.edu.au/wp-content/uploads/2015/10/IMG_9053.jpeg

Right image URL: http://www.rocor.org.au/news10/wp-content/uploads/2014/09/bombala_1.jpg

Original program:

```
The program provided is a series of logical steps to determine if certain statements are true or false based on the content of images. Each statement is evaluated using a combination of image analysis and logical expressions. The program uses the VQA (Visual Question Answering) function to ask questions about the images and evaluate the answers. The final answer is determined by evaluating the logical expressions and returning the result.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The robed people in the image on the left are standing outside.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The robed people in the image on the left are standing outside.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true


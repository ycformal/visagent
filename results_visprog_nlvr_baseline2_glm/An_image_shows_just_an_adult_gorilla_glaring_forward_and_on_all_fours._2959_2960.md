Question: An image shows just an adult gorilla glaring forward and on all fours.

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/e1/da/28/e1da289cdf4e088e8e4521223346a025--silverback-gorilla-gorilla-gorilla.jpg

Right image URL: http://i.dailymail.co.uk/i/pix/2016/04/08/10/32F7019900000578-0-image-a-6_1460107813402.jpg

Original program:

```
The program provided is a series of logical steps to determine if a given statement is true or false based on the content of an image. Each statement is evaluated step by step using the VQA (Visual Question Answering) function, which takes an image and a question as input and returns a boolean answer. The results of each evaluation are combined using logical operators to determine the final answer.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'An image shows just an adult gorilla glaring forward and on all fours.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'An image shows just an adult gorilla glaring forward and on all fours.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false


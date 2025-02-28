Question: Two dogs are showing their tongues.

Reference Answer: False

Left image URL: https://www.petfinder.com/images/breeds/dog/1320.jpg

Right image URL: https://i2.wp.com/www.russiandog.net/wp-content/uploads/2012/04/irish-wolfhound_822875-e1426772532182.jpg?resize=740%2C494

Original program:

```
The program is asking if two dogs are showing their tongues in the image. The program uses the VQA function to ask questions about the image and then evaluates the answers to determine if the statement is true or false. The final answer is returned as a result.
####
The program is asking if two dogs are showing their tongues in the image. The program uses the VQA function to ask questions about the image and then evaluates the answers to determine if the statement is true or false. The final answer is returned as a result.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'Two dogs are showing their tongues.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Two dogs are showing their tongues.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true


Question: There is at least 1 monkey actively swimming left.

Reference Answer: False

Left image URL: https://media-cdn.tripadvisor.com/media/photo-s/0d/aa/ac/c4/baboon-having-a-drink.jpg

Right image URL: https://i.pinimg.com/736x/8f/b7/74/8fb774b1a8fd280764e76e4093095979--funny-animal-pics-animal-humor.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There is at least 1 monkey actively swimming left.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There is at least 1 monkey actively swimming left.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true


Question: The left and right image contains the same number soap dispensers facing right and forward.

Reference Answer: False

Left image URL: https://images.homedepot-static.com/productImages/e6f2e645-8054-4fc7-a5a4-3ed3f077ae7d/svn/satin-nickel-glacier-bay-soap-lotion-dispensers-36664-64_1000.jpg

Right image URL: https://images-na.ssl-images-amazon.com/images/I/71HX3Qd9H8L._SL1500_.jpg

Original program:

```
Statement: An image shows one bare hand with the thumb on the right holding up a belly-first, head-up crab, with water in the background.
Program:
ANSWER0=VQA(image=LEFT,question='Does the image shows one bare hand with the thumb on the right holding a crab?')
ANSWER1=VQA(image=RIGHT,question='Does the image shows one bare hand with the thumb on the right holding a crab?')
ANSWER2=VQA(image=LEFT,question='Is the crab belly-first and head-ups?')
ANSWER3=VQA(image=RIGHT,question='Is the crab belly-first and head-ups?')
ANSWER4=VQA(image=LEFT,question='Is there water in the background?')
ANSWER5=VQA(image=RIGHT,question='Is there water in the background?')
ANSWER6=EVAL(expr='{ANSWER0} and {ANSWER2} and {ANSWER4}')
ANSWER7=EVAL(expr='{ANSWER1} and {ANSWER3} and {ANSWER5}')
ANSWER8=EVAL(expr='{ANSWER6} xor {ANSWER7}')
FINAL_ANSWER=RESULT(var=ANSWER8)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The left and right image contains the same number soap dispensers facing right and forward.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAyAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD3+qd3eywyrBbWslxMw3YztRR6sx/kMn2q5RQBlyahqFqGe40svEASWtZg5H1DBf0zWXo3jW11nVGsY7WWMjy8OWBB3w+cP/Hf1roL6W3gsJ5buZIbdY2MkjsFCLjkknpXk3w8u9Pk8UzA3SBi0YiBYDcy2yxhR6nBfjvjPakxnsNFFFMQjMqKWYgKBkk9q5248YWkUzJFb3E6ocM8aEgfkD+tbl5are2klu7uiuMFkOCPpSWVnDYWkdtAoWOMYHv7mgCHTdXstVhElrMG9VPUVerEv/DNpdXBurZ3sronJkh4DH1K9Cffg1nX+l67bWM0n9sCVI0LFSjAsB1H3qQzYbxDpqtj7Rn3CnFaEE8VzCs0Lh426EV5HfX4bWNGt47ePyf3rTn+I8Hv2rvfBryyaUXkJ+bacehxzQncGrHR0UUUxBRRRQA2SNJY2SRFdGGCrDIIryb4YQQTeK9cZoIT5Dnyj5a5TkdOPrXqd4XFs2xyjZAyOvWud0XSodOv5Jbb920zjzNsarv5/iwOaTA6qiiimAUUUZoAKZKivC6McKykE+1PzVHVLOa+szDDOYWJyTjIYehoA8q1B47LXLVI4g6yG4TfnqFXP4V6f4fiSLSIgjhieWx2PpXMXXg3VJ5LILcWpSF2d3bjG4YOBt549TXRaPpNxp7bpbhSMY8uMHafc5qUimzZoozRVEhRRRQBDd827fUfzqlBGFuFI7tmrl3n7MxAJIwcD61RtZfNuVAB4OTx0pAatFFFMD5Q+MWu6vZ/FLWILXVb6CFfK2xxXDqo/dJ0AOK4T/hJ9f8A+g3qX/gXJ/jXV/Gz/krOtf8AbH/0Ulef0Aav/CT6/wD9BvUv/AuT/Gj/AISfX/8AoN6l/wCBcn+NZVFAGr/wk+v/APQb1L/wLk/xo/4SfX/+g3qX/gXJ/jWVRQBq/wDCT6//ANBvUv8AwLk/xorKooA+/wCiiigAoxiiigAooooA+QPjZ/yVnWv+2P8A6KSvP6KKACiiigAooooAKKKKAP/Z">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The left and right image contains the same number soap dispensers facing right and forward.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true


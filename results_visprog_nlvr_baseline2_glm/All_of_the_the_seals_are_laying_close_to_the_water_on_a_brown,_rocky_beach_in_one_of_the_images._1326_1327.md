Question: All of the the seals are laying close to the water on a brown, rocky beach in one of the images.

Reference Answer: True

Left image URL: https://media-cdn.tripadvisor.com/media/photo-s/01/14/bd/1d/sea-lions.jpg

Right image URL: http://annemckinnell.com/blog/wp-content/uploads/2012/11/newport_20121107__MG_6076-Edit_lg.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'All of the the seals are laying close to the water on a brown, rocky beach in one of the images.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAkAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDy8vLKT8q++3ilCP3z+ddd/wAIlNpq+bqNlhmU7Ip7tImz2yv3j9KhtNLhjti01mXkAYmNWyTjg8detDaW5Ci3scz5DEAs4wexqZdPcxmQ7BGOCzNgZ/Guxit7prqKZ9OZQuJFDKrlhjA6nJ/zxRqVpBAxyI4fKYySCWIltpPpkVk6y6I3VB9WZ+l6STZC5hsZVmfKpE5U78gYJBzgZz+VbtnZsnh5nlkWeWEZEcbFVGPbOfWo7aG5u7yGX7Fc5LB4rgkqH9vQD8e3NdglvFILyJgyyN+8lYbQJCeO3es6d5T1NKiUYOxw8bkjy0s1XbwA6lucE5FW4ow2XMSbSo58s9eO/wCddfDp8QYNufPQEnpS3mgxahbiBrieNQwYeUQDkfhXp8ljzbo5OFfs80hgLRnALRkHaSe/tmnXcs8QaR4zJHtzt2k7iBkjJ6ela7+DLiJSYNdvIwOfnUEfzFcdq2p3Gn3rWR1drswuA37pgoPqCeDWVR2jZmkE29DrZIdPbR9NuIkjW4IfzEaIHvx9OtZN3YWc4ZfIjjLDhljwVP4VXOt48OCT7cyXYkCoDkFk9do7c9aym8Qawi7tsgRcgvLHgZH55rjw0lTi43vq9/N3+5bI3qwk9bEsejKilJZbnepwTHFlT9M0VFP4s1WycRXEcYfaG+WJWGD75FFdSqRZi6cl0LKPZ6hbymG2ltrhmxmYNubpyGJz+fWq8ENwB9gguGupmPnMZPupjuCOoGPXk1cst1xLGLawkkuFVvNMZKBc/dRj/F7+nFb+laS1rbyPeIlq8mS0Mb+YWHpk9unFcKTZ3tpGPZeGppbxLu8uzErvhmhlKc9cbf4Qe1av9lyX19LFM4S0j/1AXDgEfdY5+8RjvnmtSztCjbjC8mzJUtHliT6k/wCfpWpa2bu25olSVeVQnIHpnHerUe5Dn2IbHTLO1lcS3U0s0oyTK5f278AewxU7adFbK8nlGORejKDtkHt2zV7HkOqFHVxgb1PB57+v0qtrRKaTd7rwIcKd65DHnPI6dAelawtzKxnO/KysqqzctIP91yKyNY12y0mWFPLuriSXcTtuCqoFOCSSfXjiuI1HxnmCSDT7mVg3yNNIccHjCjrn0Nc+JP7RgdjdTqIEwHd2chSccdB9etdFSrbY56dK+50es6/d6w0UStNbadcY2MspO0j+J2Pb2xVe3s0lvrmKS4DCJQokVtqvlciQNgjvwM1jrqMKzRyHzfs9ugi8wKrjPOcr2znmp0v7Wa2u51uXWSFh5btGCPLJGMqR257d65Jcz1Z1xcVsOtLuaezNqImIt3EscjwAKAGySw3Zx61YZ1iuY1KLNHd/u5URyu0/3sZxknoP51XuLyOCZpwrzQSswdElwi9MccdRwexpsutMZUfaGIUIuUz8noT7cYqXEamieLSpLuFJZbKG8O0ASfaPLIGOAVz1oqibZr0+ct/Jgkji3T196KfzFzIp2/xM1u1TbBa6agHTbbYx+tDfE/X3I3R2LLjGwwcfzoorWxncsR/FnxDDGUjt9OAPX9w2T9Tuqz/wujxSF2iPTh7i3Of/AEKiigBB8ZvFAiEflaaR3JtySf8Ax6rmhfETXfE3ivTbTUDbeSzsCsUW3+En1ooppe8vUmXws7K/8P6SYXk+wQhvvZC459azDoGmtbbfIIGAOHb/ABoorqnFdjni2Zlxo9nFbs6o24pgnd2ziq95axuGLbiygYYnkcY69aKK55JGibIbWCOVfKYEKS4OGPIxWgNKtNsYKMRjHLngH8aKKIJDbY2LSbBU4tk60UUVVkK7P//Z">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'All of the the seals are laying close to the water on a brown, rocky beach in one of the images.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True


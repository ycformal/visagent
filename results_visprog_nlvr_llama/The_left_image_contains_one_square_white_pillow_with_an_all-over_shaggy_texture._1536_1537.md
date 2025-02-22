Question: The left image contains one square white pillow with an all-over shaggy texture.

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/17/e9/00/17e900519e446ac4d398bf7b0d5219e0--fur-pillow-throw-pillows.jpg

Right image URL: https://i.pinimg.com/736x/92/e0/3e/92e03ef5c584195709586fe698c638e3--modern-throw-pillows-decorative-pillows.jpg

Program:

```
ANSWER0=VQA(image=LEFT,question='Is there a square white pillow with an all-over shaggy texture?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABkAEMDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD2JqjbqKmaoz61BoRgY4oI4p5pppARHOenFNIqQ4puAaBjMVGVz9amIpuKAIdtFTYooA0CBnpUbcVIxpoieTJUGmIhP1ppGT7VK0E2OEY/SoTHKP4H/KkAYxR9KaUk7o//AHyaQFgcbWz9KLjHECjaD1pVVz/A35Glxjg0CGbDRUnFFAE79auWxBgGO3BrOkkAJqzp8m7zFz6GgC2xCgngfWq3mgvgfN6kdKkuASuBye1V5js2pGvXv7U2JCi6DOR0A65o89lUYAyTnNVY1Acg8A8n1NSgAqcKRg4HtU3KH+Y+QWYknqBVWaTdKfarGcbnboBnFZaPu5J680NgkWdwoqLd70UAE8mHNWtJkD3LjnhP61mXj4Y1b8Pspeds8jAH0pLcOhuOCfpVOUtI2BwFqzI3HH4VAUCqRycnJq2SiJF2uc9OuKUvncoPHrSkhcEjHoKYThdoHSkMH4tZTj+A/wAqyUYYFbG3fE6H+JSK5+NwBjvUyKRb3UVW8z/aNFTcZWupZZ3PlbWBrZ0SL7LaYdw0jnc+Og9quppMEY+UU/7BD/dFWlrci5KZFJGCOOlRM/OAc0hsIsYxx9TTG02F2LEy5PpIR/WmAkjEsDnpTdwpv9j22fvT/wDf5qadHtuu6f8A7/N/jRqPQsI4BrltQW4s7x0SJpEJ3KR6E9K6T+y7cjDeYwHrI3+NSpZ264xH9M80nG4J2OMN1c5/49pf++aK7j7PD/cWip9n5lc5YLUm6oy9IXrQzJCfemlhmo93YU3cc0ATbhnrTSRzTCaNw9aBjg3alzxnNRluaTcR1oAl4oqPcPQUUAMYkUgY4HNFFACpzTmFFFACDrQaKKAIQxpSxoooATJooooA/9k=">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is there a square white pillow with an all-over shaggy texture?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True


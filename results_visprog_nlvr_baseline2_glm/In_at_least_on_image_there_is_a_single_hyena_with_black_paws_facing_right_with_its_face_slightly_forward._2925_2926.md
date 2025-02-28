Question: In at least on image there is a single hyena with black paws facing right with its face slightly forward.

Reference Answer: True

Left image URL: https://images-na.ssl-images-amazon.com/images/I/51qxHFeUfpL._SR600%2C315_PIWhiteStrip%2CBottomLeft%2C0%2C35_PIStarRatingFOURANDHALF%2CBottomLeft%2C360%2C-6_SR600%2C315_ZA(34%20Reviews)%2C445%2C286%2C400%2C400%2Carial%2C12%2C4%2C0%2C0%2C5_SCLZZZZZZZ_.jpg

Right image URL: https://images-na.ssl-images-amazon.com/images/I/51OAzjGRCvL._SR600%2C315_PIWhiteStrip%2CBottomLeft%2C0%2C35_PIAmznPrime%2CBottomLeft%2C0%2C-5_PIStarRatingFOURANDHALF%2CBottomLeft%2C360%2C-6_SR600%2C315_ZA(21%20Reviews)%2C445%2C286%2C400%2C400%2Carial%2C12%2C4%2C0%2C0%2C5_SCLZZZZZZZ_.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'In at least on image there is a single hyena with black paws facing right with its face slightly forward.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAaAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD3+iiigDP1LW9O0kD7bcrGzchcEsfwFc3/AMLM0fzyvkXfkDrNtXaBnGcZzjNcoPCuq+L/ABDqF5LfRWktnNJFJBJ+8yTygIUjACFec9enek0zwRDZ+LrXRtU1h/NFu1wgtf3XnZY/J3wBg+5xWb576Gi5banqmm6paavaC6spfMhJK7tpHI6jmrlZuhaHaeHtLTT7IMIUYsNxzyf5fhWlWhmFZXiLVX0TRZtRSNZfIKlkLY3KWAIB9ea1axPFegjxHoMtgJHjfcsiFZCg3KcjJAPHfGOwpPYa3PMtZ8W65qxlmF9Np1tkeVDakEMh4OX6lhjnGBiqaa1rttEI4te1AJg/eYNg/U5wOo+tdzf+FINE+H93bL/pF2o80zFed24dPbHbvVLQPCiazC9zM5hh+4RGo+dh97B7jjg1xVfa86ijspumoOTRT8NeLNatbq0jvp5b2C4kEZEm0smTgMCP5HOcdq9UryvxjbW/hSRZvOYWwQTRjcPMyjAsBxkjkfSvTrW4S7tIbiP7kqLIv0Iz/WtsO56xn0Mq/I7Sh1JqKKK6DnCiiigClBpNjbajc6hBbLHd3W0TSrnL7RgZqpq3hjTNZuYLq7if7Vb/AOpuI5CkkfOflI6citio5gDHggEZ70pOyuCV3YfkKvJ49SaAQehBqskEMnyvEjDOcMoNPhtoIX3RQxocYyqgUoy5lcbVnYWe5S327g7FjgBELH9KWCdLhSyBxg4IdSpz9DTL0A2j5AOOR7UtoqrbIVUDIycDqa0suW5lzPnt0Ob8cL4gubSy0/QoFZLufy7qc4Pkx8c4J/zj3rpLKzhsLKG0gXbFEgRR9KnpD901Flua3drHI614Et/EfiUajrVz9q0+GIJBYhSgU8FizA5bOOn+FdZGI0RUj2qqgBVXoB6VWWOM8FFwR6U/7JbLIHFvEGBBDBBnNTCfMrjkrFmiiirJP//Z">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In at least on image there is a single hyena with black paws facing right with its face slightly forward.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True


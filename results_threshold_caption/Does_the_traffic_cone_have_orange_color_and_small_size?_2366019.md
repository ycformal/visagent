Question: Does the traffic cone have orange color and small size?

Reference Answer: Yes, the traffic cone is orange and small.

Image path: ./sampled_GQA/2366019.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='traffic cone')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What color is the traffic cone?')
ANSWER1=VQA(image=IMAGE0,question='What size is the traffic cone?')
ANSWER2=EVAL(expr="'yes' if {ANSWER0} == 'orange' and {ANSWER1} == 'small' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='traffic cone')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAyABwDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDMWLdSeUN2Kt+XtFTWtqs91EmDycHFeZtqYRi5NRXUztiHinbIl4Yc10ut6TZWtqk1qjKwIDAnINYJjLcgURdzWvQnRnySLTR9g3WtTw/Zb7syE8IOKzNjAg966zQ7fybEO55c5/CobudGBp89ZPtqJr8CnSmIUgggniuVWH5eCa7bUx5ujy7ZN3HFcUqNtGSaLK5rmWtRS8iS3/0i4SJfvE4rtP8AUxrHvCkLgHFcPbh4LgMrBXFXf7YuUwxbf65HSi2osJiadGL5lqzq5g39msrKN2DwK4gqc8HNXjqd3MWUzHaw5HpUEaIU+9n607O5GLxEK1uVbERA3g45zTJOIsjjpRRSZxiLw7Y9aUc9aKKcRH//2Q=="></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAyABwDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDMWLdSeUN2Kt+XtFTWtqs91EmDycHFeZtqYRi5NRXUztiHinbIl4Yc10ut6TZWtqk1qjKwIDAnINYJjLcgURdzWvQnRnySLTR9g3WtTw/Zb7syE8IOKzNjAg966zQ7fybEO55c5/CobudGBp89ZPtqJr8CnSmIUgggniuVWH5eCa7bUx5ujy7ZN3HFcUqNtGSaLK5rmWtRS8iS3/0i4SJfvE4rtP8AUxrHvCkLgHFcPbh4LgMrBXFXf7YuUwxbf65HSi2osJiadGL5lqzq5g39msrKN2DwK4gqc8HNXjqd3MWUzHaw5HpUEaIU+9n607O5GLxEK1uVbERA3g45zTJOIsjjpRRSZxiLw7Y9aUc9aKKcRH//2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What color is the traffic cone?')=<b><span style='color: green;'>orange</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAyABwDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDMWLdSeUN2Kt+XtFTWtqs91EmDycHFeZtqYRi5NRXUztiHinbIl4Yc10ut6TZWtqk1qjKwIDAnINYJjLcgURdzWvQnRnySLTR9g3WtTw/Zb7syE8IOKzNjAg966zQ7fybEO55c5/CobudGBp89ZPtqJr8CnSmIUgggniuVWH5eCa7bUx5ujy7ZN3HFcUqNtGSaLK5rmWtRS8iS3/0i4SJfvE4rtP8AUxrHvCkLgHFcPbh4LgMrBXFXf7YuUwxbf65HSi2osJiadGL5lqzq5g39msrKN2DwK4gqc8HNXjqd3MWUzHaw5HpUEaIU+9n607O5GLxEK1uVbERA3g45zTJOIsjjpRRSZxiLw7Y9aUc9aKKcRH//2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What size is the traffic cone?')=<b><span style='color: green;'>small</span></b></div><hr><div><b><span style='color: blue;'>ANSWER2</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 == 'orange' and ANSWER1 == 'small' else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if 'orange' == 'orange' and 'small' == 'small' else 'no'")=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER2</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: Yes.

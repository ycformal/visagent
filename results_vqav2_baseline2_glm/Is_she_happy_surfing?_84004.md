Question: Is she happy surfing?

Reference Answer: yes

Image path: ./sampled_GQA/84004.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='Is she happy surfing?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='Is she happy surfing?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAA+AGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDvM0VhNKAQBHJ78GneYv8Acb8TiuowublGax9oPAA+pJpAud3Ix9TQO5tZFLmsdI8jgqT/AL+KjR9zEMVBJx1OKQrm5SZHtWS6oOFZH7ZDHA/SnJbO4OXiUYzhmxRoBqZozWe1lszvnhX+6NxO7/63vWTd6zplm5R7yKRlO0+USwz9Rxx39KTkluNJvZHTZHtRkeo/OqMdjG4DG+tVBGfvnNQzQQRsFW7jJPPQn9RmndCNTcP7w/Oiscps43RN7qWP9KKVxh5KltpOe4xml+zgqGG4Z4yKgTU5YlIEsKhuo8v/ABqxbzNdzAXGoHbj5QnH6Ci5N0TLZFlZuQcZwDyabDahpghYA+hPWtVNOhIUrMTtUj72TzU4t7aNg/ljf03YyTU8xfKZb6e6ElXDKD+Qqzp9nYSRlrhgG6ccCrDvEjM2GwB1AwKmWRBB5hQbfvdP1ouOyA6ZYMmYpWUE54ORUbadCeI7psAc8Z7+1VX163Zf9TK6dHIIwtXby+WyswYlSPoBjp64pXYXRS1Tw02owm3GpNbWjR8MqAvuyOOf4cdRXkWrLd2U89hcXIlW2dkTagAAz1A7Zr0W/wDEYkiYi6RfmKg7txz347fjXEa1ppu2XUIZUlinkAA6M5zzj1xzWtOKs+bqcWLdVuLo3Vux6H4UvdN13QEuby2EE9u/kSqMqMgDBx2yDW5Da6PE7sNkjZztJzt/AV5hAXsr2R1bMdyBvU9C46ZHfIrQmvpZlCtv2r02tWbd3obxnaKvqdtPd6DHKRLJErnkgE8flRXAsJXOSWUdhjtRSD2r7GrDDHvBkBxnB4/+vW1BZW/3lk6+44rNCOy5wR/vEUeS/UAg9iGplrQ6GACEfuwW98ZpymU7nChmx93I/lXPFbgjl2Pb73So1t5EfKzOH/2XwaRVzqLd5sEy7iMHgjvV4FCmCABj0rkYri/QYF8+335NPe6vuv2kt9VFIakW38ONHfNNBMqRN94A9ag1iC4ml2jYIoxnHmBf5momvdSGcSKPTK//AF653VjqDPIUcjdyWXg5oJfKkQxabpWmWgWdrUSDLOXYtz78UyIaSJmmt7xZULl4txJxnjgYGPSubu11JpX81pWJ5IbJzVjw/Kq3kcVxFux9wdAD701Iz50zpnXnHAUdhzTo4E2/MSfwwasxTCUgBFBPcnP9atFFJwQc+1MFEzGtkY5KyN7gA0VolFB+4aKA5UWAkhXAlAPsM01YpwwxcHHptqyLa43kiWIr2DIeP1pUhuGLEPFtzgAoe340GtiMK4GTIx/CnZYckE/QVZWMqgDkM2OSBxTgo6YFAWK4xj5qkC4T5ePwqUKo7UpK9CM0AVmTPXBPY7agmhLK2e47VeBUnhaUxgigDkb7TVkRlwd3JBx0rIt9Kkgu0kjDPsOcba76WziYfNnB7VSENuszKA4OM5GKCJQuQwBnIZonBHPIqztz/C38qmiCFf4iPc1NsUgYFBVinsP9zH1NFXfLHpRQFj//2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is she happy surfing?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: Yes


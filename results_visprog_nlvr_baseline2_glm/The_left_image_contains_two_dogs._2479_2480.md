Question: The left image contains two dogs.

Reference Answer: True

Left image URL: http://s3.amazonaws.com/medias.photodeck.com/20945f3d-ef98-4b7b-b029-9f99290b73ea/dwss-160_medium.jpg

Right image URL: https://i.pinimg.com/736x/90/76/85/90768587c680b66eaaec2d541fe19052--dog-videos-afghan-hound.jpg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The left image contains two dogs.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAApAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDwdIie1a2n2oY/MOtaF3oR0+6EEx3OSMeX05+td74K8F3M9rNcthAxTy5dmXUBssMH1HFQ3YtK5y9nZRKAWXAx6cmtKCxgmguI/OjiDL8oc89On9an1bSHTUbtUeFIDK5jQOR8uTgYA49KybLwtqrXSSeZbusshZQZDnBPIzj6daaWmon5GpHFBExSFWkkGQqR8Ak/yX3NQeKtBvR4fX7Q6CaeeNIkAwvTn379elbttomrI1w221B3K+wn5m+rYxjjH40/xaJDpdu77REt3AoQEMVb5gfm6ke3SqUFyuXUzlNqaieTy+FtRht5J3MOyMZOH/8ArVUh0e6muFgXZvY4GWr0G/2/2JdkKASnb6GuZ0yVpNUtywAPmDpWVOcpK5rUSjKyOaW1ld2VV3Mucgc9Opp8NhNPII0ALH3r0TwN4ct5Wu9dvX32sEkkH2Vesu4EEE9hg11up+AdENleavYRjS3023M0ke/fFMo5GCfut29M1LrJOwKm2rnicmk3Mdq9wxTYknlkbuc0tppFze3KQRbN7NtG5sCujES3WhSEnbvus+v8Oai0l4rHWYpWYtGjbiQM+taNu1yFa6Rlap4Z1LR7iOG6jUNJGJUKk4KkkZ6eoNFdR4wliub2wuArfvbNX+br99+v4YoqYzbV2XJK+h1K654eubqC1sl+0OzfPPOpLbR7npiuj8M63LboUgaWTzrkwoCeF6kD8hXlVj4h0iNHjljRGdcLIAfk/AV0ujeM/D+j2FtCLkSTw3PntLsPze2Meh61FRSk7mlOSSscprWq6jc6/rE8d7PHFBKxwX4+9gL/ADq94d1HVn1G3/0yR4hCWYO+MfT86i1Sbwpfapd3kVyyfaZDJ5bKSqMeTg8HGaz7Yaazr9q1K2MSjCqu4H8TitL6EW1PRPtuosNjzP5SnKiORR+HJrL8T3c/9j2yvPIyi6RmSR1Prjkelcvcp4b25iv+fRSx/pVGO2sry9trezud0ryBQDkDHPJpXdtQfkdFdSqukXStgZQYOevWufsZRBdwytyFYHit+88Puul+c9zBGOCQ4ct9OnWsMWBBBEucH/nmf8ailOKja4qsZSndI9S8C2XneE4NpXM07yMQOSxPA/AV1r6DI3hDXtHkybSS1aTzC5ypBJ4PUjIH5VwfwzkuV+0WhUBElWVTk4weCOfzr1DWrtrXwfrUkE26QRCJGzjGeOK43b2jdzp15ErHzbG2zSPlOGM2OvbaKits+ZvVXkcEfuwpIYe5FbUfh+a5iELTRwyNIWHyMQePWr2neB9RS78wzxKqHqwYZ98V2utFLc5PZSbWhl+JR8mjZHP9mx/+hPRVnxpa/Yr/AE+1LBvJsUTI74Z6KKbvFMuSszz2iiitzMKKKKACr2j6idJ1a2vxEJvIfdsLY3cetUaKTV1Zgdfe+PJ76bfLYxbR9xA5wo/Kq3/CXkdNOh/76/8ArVzNFZ+xh2L9pLudXB46urZy8FqkT/3kfH9K1bj4r6ldactlNYwNGHD7tx3Egd/WvP6KHQpvoP2s+5158ezkf8eEP/fZrTtPive28Ijk02GYD7pMpBA/LmvPaKHQpvoL2ku50fiDxa+vX6XTWawlYhHtEhbOCTnp70VzlFWoRSsiXJvU/9k=">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The left image contains two dogs.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true


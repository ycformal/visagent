Question: What room is this?

Reference Answer: bathroom

Image path: ./sampled_GQA/252857.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='What room is this?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='What room is this?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABkAEMDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDk/iVqd3pt1pZt2UebC5bKg9Grj4vGOqJ/Dbt9Yz/jXVfFxMXOie8En/oQrz1UFctKMfZq6N5t8zOnh8d36fftIG+jMKvx/EWYY36cMf7M3+IrjQgp4QUOEOwlOR3S/EiEKd1pcqfYqcfyqtN47t7sENLLEvoU/wAK49oQRVCaPa5AojSpvoDnI6Ww1P8AtTxPp25vk+1xBE9PnH619Zyw/MeO9fHfhNN/i/RV9b+Af+RFr7UkhyT9amvDaxVKXc86uFzcy/75/nRU8y/v5P8AfP8AOitVsYvc8j+MAAm0IkdYJf8A0IV5yh56V6T8YlG/QDn/AJZTf+hLXnKBPUfnU0v4aNKnxscDTw4owvr+tKFzTZI4uuOtUphGznMhH/AaveXkVQVxDdLI0Syqp+4+cH64qoAzoPA1rDL400bN0qst7AyKYzlz5i8D+f4V9nlMmvjHwPcxxeOtCnu5VREvond3ONoDD9K+xNP1jTNXWQ6df210I8b/ACZA+3PTOOnSlJXYvQ4WRcyuf9o/zop7Ll2+tFMRl63psN4LXzLS0m2K2PPj3beR04rNi0CxzzpGkkn/AKYj/wCJrorrkR/SoVGD3rguztsjMTw1pj4DaHpB/wC2f/2NK/hHRmI3eHtGbHH3P/sa2I2we9Sh6pSYrHMXXg/Qlj48PaYv+4SP6Vijwdom8t/YdqOD0kPpXc3RLJ3rMB2tiqjJ33JkkReGdJtNO1a0eDS7CJVcZCLzj/vmvTLJrNdf1WKC3Ec0UMPmuoADA7yv5YP51w+nAC8ib0df5iujttQtbbxf4kS4uoIXMdsqLJIFLfu26AnnrW1N63MpmWQM0UuKK1MipcHhKaB/nFNkbMcR9RTlPy//AF64kdjAcf8A6qcH/wA4qJjUEMkrTsrwlVA+9ng1F7FWJp3+WqGQXq3cH5KyppvJUvtZgvJC9atMhm5pMUkt9GseC2QcMcA4OevbpXTX2nW10z3d1ommyXAGfPfa7jA4IJTOR25rmfDtykt3HNF842tjHftXS/2l52ny7R5hOUbkDafb1x3xW1NN7GcrGSc5oprNhjRXXynLzGNNHcS29oYrgRrjLfJncMDj2+tXt8ap1bNY01xdf2ZaG2jZ22r90Z7UQzazjJtnx9RmvN67nea+5T/CxoVGzkIxz7Gs1tQvEwHeSNscqeCKj/tO7z/x8S/99U3S8xKZoz207qdkEh+imqkmi3F1FhrCV/YKRUf2+6PWaU/8CNEdzP1LSn6k00rA9TV0+2l0u6jSWBogEIUdvwqOK9mi1BbUxuYplLB/4UI6j8c1Rju2Wf5yc4PBP0qe2QyXpdj8uFxz0IJP+Fb0LmVTY1CeTRQBkUV3paHC3qc3DqUdrpNpIwyNqqRnFaVrqlvKqt0B9TXD38jv4dUKcFXTH51BZm8m0y4mgnxJGjMo25zgZrgjSi7tne5tWSOn8TeKtO024gjldt7IThVycZ9ulc5J48sOSiztz2TH9a86uL24vZzcXDtJKwBJNMDtggZ/Km4K1ied3PR7fxrDdzGCGCYyFWKAkDcwGQvXqe1UD47kcfu7Q9O7j/CuJV2UgqxDDkYOKQFieD196FBBzs6ibxxqBuoWSCNI1I8wfeLLnkDpg16bpF5HerBcQSExON445II6H868HY/KST0FegfC/W5rp7vT5DujgjDox6gE4xW1OKuZyZ6shG0UVW83GB7UV1nOeesvmaKFJOCw6fWgztpOj3MtuqllUkB+R0oorz4dTsfQ8x6ID3xT0ycHPJoopkjSSQOab1oopiFH3GrsvhaANS1RgMHyY/8A0I0UVpT3Jlsepux3UUUV2HOf/9k=">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What room is this?')=<b><span style='color: green;'>bathroom</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>bathroom</span></b></div><hr>

Answer: bathroom


Question: What is the pink piece of furniture called?

Reference Answer: The piece of furniture is a dresser.

Image path: ./sampled_GQA/2361734.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='pink furniture')
ANSWER0=VQA(image=IMAGE,question='What is the pink piece of furniture called?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='pink furniture')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD//gCgQ3JlYXRlZCB3aXRoIFZpZ25ldHRlIGZvciBBbmRyb2lkCkVmZmVjdDogTm9uZQpGcmFtZTogTm9uZQpXaGl0ZSBiYWxhbmNlOiBBdXRvClNlbnNpdGl2aXR5OiBBdXRvCkZvY3VzIGRpc3RhbmNlOiBBdXRvCk1ldGVyaW5nIG1vZGU6IENlbnRlcgpBbnRpLWJhbmRpbmc6IEF1dG//2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABLAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD0xzxVVzU8h4qq5rzrHVYYSaVTmmE0RtlqCkibFRyKcVOBQy8UylErLnFLQOCRQapDsJThTc05TVIlolXHpSkU0GlzTIDpRTC3NFUgLT9KqyVafpVSc4FYMpEBbBojb5qgmmVBliAKgF7DGy75o13HC7nAyaRrGN9jbQ5ArB8T+L7Hw3EqOrXF3IMpAn82PYVav9Xg0rTZb24J8uIZwOrHsB9a8Q1fU7nVdSuLlyN8j7j7eg/CnFXG9DqR8StXjuC01laOjHiMBgV9s5retviFatAs15ZSwKeMqwfn0A715FM0quGYknnIPerdtNdSTQES4WM5QDopHetOUm/Q92stSS9tVuBHLCrfdWUAMR64zxTv7StwSAzMQcHapPNZej6paavZiW2kVmUASJ/Eh9xWraxL84wPvZ/SpuNoUakD92CY/hinfbZ2+7aN/wACarKxgdqkEY9KdzJozmnvSeIIx9WNFX2QZ6UVaJLj9Ky7yYRjJOMVqSDiua14sts5HWsizOuNUBmyBlR0qC6t7XVrZlngRzj5D0IPse1Zlg8d1AjM3I4IHqK2FaGKPCcY7VooqxgqkoyvHRnn3iG/1GwtTo11I0tsriSF26kDOBn056dq5vzixyDzmug8dyTm6PmEmFCrxccDIwRmucSIPDujkOQM7SM/rTSVjvq8zkpO2qT0JRbPdTNGIkZmXILE1JZI1vchZF/dKTnbzxjmqxV1IczEY6Y61He6pPOFiEhGV2kgYLfU9TQk2ZtqOrRu6DbatdX6tpcc/nK3E0R2j8T0/CvZ9HGoLaJ/akCRXRUbvLYMrEdxjp9K8w0fWLrSFisrD93CI8tMAMlvfNdTpXiu61Gxvbe5SQXEYYwzfdYsnzDpwQeaHFvU7/qElDmT1/ryO7DDFPDD2rmdJ1VtUsxcbl5ZlOwkjINaa5Pc1NjzZ6No0S656j86KzyhzRVpGdzckHFc/rUe+Bx7V0ci8Vh6uMQmsTWx4/JqZ0nV54ZCVhdtwI/hJrXi1xCAVYN9DmsPxna7LhZQODwaxtBujBqMSNja7gDPrmtVsZSidT4jsbzUdIaRkYRrh9pHJHqP51wMMjxEqUyQMcccV7HqUq4iXdwV5HrXnLaDNdak6w2++FHKGRkOxe4yegNF0tzooRdSDS3X6mOI7i7dI4BuZiF+hzj8BXWw+GI9LgDefb3MhO2SSI5w3p9K6jw1o+jaRbu7MZblhhmKfKB6Ln3qPUCkS3JQRfZypMcYA3hvoO3HWspTb0R1U8NZc0tzmf7Guhk2U20Kc7W6fSrDy3WnWE5a3kWaWJow7EbBnhvxwTipodSuUkhWOyfy3yXZjyv4Ua3dXN1pYt4oGdmlUkccAdT/ACq4t9Ta9VQcUnb5k/w/1F49Sm09wSky71xyAy9fzH8hXp8S15L4bE2m6zb3csSomdsmWGQDwT1r1Ow1K0vWdbadZCgBYDPFUedOhVgryi0vQuMvPSilJB7UVdjA25lwK5rXphCgHrXVTVx3in7ormN7Hnl+q3k0gmUSLuOFYcVUSytY2BW3iUqcghBxVyT77fWo81SR9tRoU1FWivuHF2bBZmPbk0A4GMnHXFIKXuatI6lFLZDX6VA3WpmJxUDGqNL6CfhThj0puTindqZlJgDXQeErnydTlUnh4j+hFc/VjT5Gj1O0ZWIPnKPwPBoPMzCPNh5+h6V9qX1orzu/8Q6pBqFxFHchURyFHlpwPyorRQPieY//2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What is the pink piece of furniture called?')=<b><span style='color: green;'>box</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>box</span></b></div><hr>

Answer: box

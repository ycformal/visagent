Question: What color is the tall grass?

Reference Answer: The grass is brown.

Image path: ./sampled_GQA/n207893.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='tall grass')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What color is the tall grass?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='tall grass')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAyAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDlZNRupOGmI9l4p0Wo3ES7RIce/NPCQ5wIRn3BpWCbcGNQPbFafWkR9WZC9y07BpH3EdmPFOCxyD5VYnH8K04RwKMbmA68AH+lO8qBTkXUwH90jNJ4mI1h2hY2khG2OSVBnnggVPDe3gcE5kX0OBVfzdiqvmyOoPsMj0pGu0VlwJMjuX/+tS+teYfVvI0ftd6B/qomPsaY+pzqObfae5OTVaK7g3O32dyzdSXpxdm6KoHbrQsYDwiLMerhhh4Tn/ZNWI79ZD8sMn6VnRyBQDwTj0P+NJucjPlBjnOdvSn9cJ+qGkdQAGfs82OvQVAdYyMpbkj3aoFnlJG5Tntx0pUY8kIFJ5OMjn8Kf11B9TH/ANsv2gX/AL6oprDe24oMn2op/XYh9TfYrGHgkYJ9WGcfrQIhjIc/jzS7l46ZoDZGVHNeXdno2EMSH7zsfbFOECEZAJ+opA7qSMrnoKXzDnBbrSuFhfJBwAkY99vJ/WgQ4LAbOT1K9PpRnJ5xj60bweOMUXYWJdhxgP8AkKGVgOHOfemBuMDAHrS5ODhhSGAD5xvI/CnlGH8dN+UcHB980bTnjJHtRcLDmD7AFCE/3mJ4/AU4RrnqTTAGxknFA3EYDc+1NsLEgjXHeikw3dh+VFK4WMoSAD5Vxn+8acZOgH3h0yetQ7HAGTxjODUqycfPwOmcdKoQ5HmGd2M9ABTnAGM8k+/SmCQ7dw5GeoFKxQ4DMCx4ApAPCqQG+cjGMZ4NORhsA2YbPr0pNu0EiTdjgAHinIzheoJ74FAw356Lu7+lOBOzcBt9AajDfOSD9BSecWbac8e1ICUliuUBJzjkU4yybVJAA7mm7+ArEY7VGWABILUATLI2CV2k+tKryH5lAB+lQedzuywUc49af9p8wKVBC+tFguDs4br+Rooby3O4yYJ7UU7BcziTvk5P3alH+qX3YUUUxCR/w/59aVOZTnniiigC5tXMfyjn2qBQBEMADpRRQBDNxLxx8tN8x8N87ct60UUMCZOgPcjn86cCfKPJ/wAmiikAmT5zDPGOn50qkg4BwKKKaAqyM3mNyevrRRRQB//Z">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What color is the tall grass?')=<b><span style='color: green;'>brown</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>brown</span></b></div><hr>

Answer: golden

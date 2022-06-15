# 文件服务

使用 `curl` 命令上传文件  

```shell
curl -F "upfile=@./test.txt" -H "Content-Type: multipart/form-data" http://127.0.0.1:8000/
```
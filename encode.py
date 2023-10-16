shellcode = b""
str_=""
for i in shellcode:
    code=(i^1024)+1024
    str_+=str(code)
print(str_)
# tsmc hackerrank
def compressedString(message):
    if not message:
        return ""
    
    compressed = []
    count = 1

    for i in range(1, len(message)):
        if message[i] == message[i - 1]:
            count += 1
        else:
            compressed.append(message[i - 1])
            if count > 1:
                compressed.append(str(count))
            count = 1

    # 處理最後一個字元
    compressed.append(message[-1])
    if count > 1:
        compressed.append(str(count))
        
    return ''.join(compressed)

# testing cases
print(compressedString("abaasass"))  # Output: "aba2sas2"
print(compressedString("wwww"))  # Output: "w4"
print(compressedString("abc"))  # Output: "abc"
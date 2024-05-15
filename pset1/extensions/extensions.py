f = input('File Name: ')
f = f.lower().strip()

if '.gif' in f:
    print('image/gif')
elif '.jpg' in f:
    print('image/jpeg')
elif '.jpeg' in f:
    print('image/gif')
elif '.png' in f:
    print('image/gif')
elif '.pdf' in f:
    print('image/gif')
elif '.txt' in f:
    print('image/gif')
elif '.pdf' in f:
    print('image/gif')
else:
    print('application/octet-stream')
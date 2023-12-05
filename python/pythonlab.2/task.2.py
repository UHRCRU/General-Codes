diskSizeUsed = float(40)
fileSize= float(input("Enter the size of file"))
if diskSizeUsed < fileSize:
    print("The File you are downloading is too big")
    print("File size in gb:", fileSize)

else:
    print("File download completed successfully")

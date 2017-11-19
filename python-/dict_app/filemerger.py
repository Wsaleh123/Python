def filemerger():
    import glob2
    filenames = glob2.glob("data.json", "data.txt")

    with open("Data.json", 'a+') as file:
        for filename in filenames:
            with open(filename,"a+") as f:
                file.write(f.read()+"\n")

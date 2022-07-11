try:

    f = open("new.txt", "w")  # "a" appends
    print("File opened")

    try:

        print("Initializing Writer")
        f.write("Hello World")
        print("File written successfully")

    except Exception:

        print("Something went wrong when writing to the file")
        raise

    finally:

        f.close()
        print("File closed")

except Exception:

    print("Something went wrong when opening the file")
    raise

finally:

    print("End1")

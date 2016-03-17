import io


class SearchStream:
    @staticmethod
    def find_lines(keyword, stream):
        first = stream.read().split('\n')
        second= ''
        for s in first:
            if keyword in s:
                second += s.strip() + "\n"

        return second

#To see the output, uncomment the lines belows:
stream = io.StringIO("Hello, there!\nHow are you today?\nYes, you over there.")
print(SearchStream.find_lines('there', stream))
stream.close()
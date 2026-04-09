from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "#" + s
        
        return encoded_string


    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """

        decoded_string, i = [], 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
                length = int(s[i:j])

            decoded_string.append(s[j+1, j+length+1])
            i = j + length + 1

        return decoded_string
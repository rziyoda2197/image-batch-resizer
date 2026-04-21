class DiscordMessageFormatter:
    def __init__(self, message):
        self.message = message

    def format_message(self):
        formatted_message = ""
        for char in self.message:
            if char == "\n":
                formatted_message += "\\n"
            elif char == "\t":
                formatted_message += "\\t"
            elif char == "\\":
                formatted_message += "\\\\"
            elif char == "\"":
                formatted_message += "\\\""
            elif char == "\'":
                formatted_message += "\\\'"
            else:
                formatted_message += char
        return formatted_message

    def format_code(self, code):
        formatted_code = ""
        for char in code:
            if char == "\n":
                formatted_code += "\\n"
            elif char == "\t":
                formatted_code += "\\t"
            elif char == "\\":
                formatted_code += "\\\\"
            elif char == "\"":
                formatted_code += "\\\""
            elif char == "\'":
                formatted_code += "\\\'"
            else:
                formatted_code += char
        return f"```{formatted_code}```"

    def format_bold(self, text):
        return f"**{text}**"

    def format_italic(self, text):
        return f"*{text}*"

    def format_strike(self, text):
        return f"~~{text}~~"

    def format_underline(self, text):
        return f"<u>{text}</u>"

    def format_link(self, text, url):
        return f"[{text}]({url})"

    def format_image(self, text, url):
        return f"[{text}]({url})"

def main():
    message = "Hello, \nWorld!"
    formatter = DiscordMessageFormatter(message)
    print(formatter.format_message())

    code = "print('Hello, World!')"
    print(formatter.format_code(code))

    print(formatter.format_bold("Bold text"))
    print(formatter.format_italic("Italic text"))
    print(formatter.format_strike("Strike text"))
    print(formatter.format_underline("Underline text"))

    print(formatter.format_link("Link text", "https://www.example.com"))
    print(formatter.format_image("Image text", "https://www.example.com/image.jpg"))

if __name__ == "__main__":
    main()

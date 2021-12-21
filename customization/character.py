class Armor:
    def __init__(self, head="nothing", body="nothing", boot="nothing"):
        self.head = head
        self.body = body
        self.boot = boot
    def get_info(self):
        return """Head - light(for run), fully protected
body - light(for run), fully protected
boot - light(for run), fully protected"""

    def choice(self):
        return """Change Headset - 1
Change Bodyset - 2
Change Bootset - 3"""

    def your_armor(self):
        return f"Headset - {self.head}, Bodyset - {self.body}, Bootset - {self.boot}"

    def set_head(self, head):
        return f"Headset is {head}"

    def set_body(self, body):
        return f"Bodyset is {body}"

    def set_boot(self, boot):
        return f"Bootset is {boot}"




class MockSupportModel:
    def generate(self, last_user_message, attempted_fixes):
        if "browser" in last_user_message and "crash" in last_user_message:
            return (
                "Browser crashes can be caused by corrupted profiles or extensions. "
                "Have you already tried starting the browser in safe mode?"
            )

        if "wifi" in last_user_message and "disconnect" in last_user_message:
            return (
                "Since WiFi disconnects affect only one device, the issue may be with "
                "the network adapter. What device model are you using?"
            )

        if "already tried" in last_user_message:
            return (
                "Thanks for confirming. Since that didn’t work, let’s move to the next step "
                "instead of repeating it."
            )

        if "not technical" in last_user_message:
            return (
                "No worries — I’ll keep things simple and guide you step by step."
            )

        if "nothing works" in last_user_message:
            return (
                "Since standard troubleshooting didn’t resolve the issue, "
                "I recommend escalating this to human technical support."
            )

        return (
            "Thanks for the details. Let’s continue troubleshooting step by step."
        )

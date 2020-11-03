import os


def setup_code_server():
    def _get_code_server_cmd(port):
        return [
            "code-server",
            "--bind-addr",
            f"0.0.0.0:{port}",
            "--disable-telemetry",
            "--auth",
            "none",
        ]

    return {
        "command": _get_code_server_cmd,
        "launcher_entry": {
            "title": "VS Code",
            "icon_path": os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "icons", "vscode.svg"
            ),
        },
    }

import os
import logging

log = logging.getLogger(__name__)

def setup_code_server():
    def _get_code_server_cmd(port):
        ENV_VARS = os.environ

        launcher = ENV_VARS.get("VSCODE_PATH", "code-server")

        args = [
            launcher,
            "--bind-addr",
            f"0.0.0.0:{port}",
            "--disable-telemetry",
        ]
        auth = ENV_VARS.get("VSCODE_AUTH", "none")
        args.append("--auth")
        args.append(auth)

        cert = ENV_VARS.get("VSCODE_CERT")
        cert_key = ENV_VARS.get("VSCODE_CERT_KEY")
        if cert and cert_key:
            args.append("--cert")
            args.append(cert)
            args.append("--cert-key")
            args.append(cert_key)

        data_dir = ENV_VARS.get("VSCODE_DATA_DIR")
        if data_dir:
            args.append("--user-data-dir")
            args.append(data_dir)
        ext_dir = ENV_VARS.get("VSCODE_EXT_DIR")
        if ext_dir:
            args.append("--extensions-dir")
            args.append(ext_dir)
        log.info(' '.join(args))
        return args

    return {
        "command": _get_code_server_cmd,
        "launcher_entry": {
            "title": "VS Code",
            "icon_path": os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "icons", "vscode.svg"
            ),
        },
    }

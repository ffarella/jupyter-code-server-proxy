import os
import logging
import pathlib

log = logging.getLogger(__name__)


def to_existing_path(x: str, is_file: bool = True):
    try:
        filename = pathlib.Path(str(x)).absolute()
        if is_file:
            assert filename.is_file()
        else:
            assert filename.is_dir()
        return str(filename)
    except Exception as e:
        log.error(f"Path {x!r} is not valid ....")
        filename = None
    return filename


def setup_code_server():
    def _get_code_server_cmd(port):
        ENV_VARS = os.environ
        home = to_existing_path(ENV_VARS.get("HOME"), is_file=False)

        d_ext_path = d_data_path = d_start_path = None
        if home:
            d_start_path = str(pathlib.Path(home))
            d_ext_path = str(pathlib.Path(home) / ".vscode" / "extensions")
            d_data_path = str(pathlib.Path(home) / ".vscode" / "config")

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

        cert = to_existing_path(ENV_VARS.get("VSCODE_CERT"))
        cert_key = to_existing_path(ENV_VARS.get("VSCODE_CERT_KEY"))
        if cert and cert_key:
            args.append("--cert")
            args.append(cert)
            args.append("--cert-key")
            args.append(cert_key)

        data_dir = to_existing_path(
            ENV_VARS.get("VSCODE_DATA_DIR", d_data_path), is_file=False
        )
        if data_dir:
            args.append("--user-data-dir")
            args.append(data_dir)

        ext_dir = to_existing_path(
            ENV_VARS.get("VSCODE_EXT_DIR", d_ext_path), is_file=False
        )
        if ext_dir:
            args.append("--extensions-dir")
            args.append(ext_dir)

        start_path = to_existing_path(
            ENV_VARS.get("VSCODE_START_DIR", d_start_path), is_file=False
        )
        if start_path:
            args.append(start_path)
        else:
            args.append("~")

        log.warn(" ".join(args))
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

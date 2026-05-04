# IDM Patcher

A binary patching tool that applies specific byte pattern modifications to executable files.

## ⚠️ Disclaimer

**This tool is provided for educational purposes only.** The authors do not condone or encourage the use of this software for any illegal activities. Users are responsible for complying with all applicable laws and software licenses in their jurisdiction.

## 📋 Description

IDM Patcher is a Python-based tool that performs binary patching on executable files by searching for specific byte patterns and replacing them with modified sequences. The tool supports wildcard pattern matching and can operate in both dry-run and actual patching modes.

## 🚀 Usage

### Basic Syntax

```bash
python idmPatcher.py <file.exe> [OPTIONS]
```

### Parameters

| Parameter | Description |
|-----------|-------------|
| `<file.exe>` | **(Required)** Path to the executable file to patch |
| `--dry-run` | Run in simulation mode - shows what would be patched without modifying the file |
| `--overwrite` or `-o` | Overwrite the original file instead of creating a new `.xex` file |

### Examples

**Dry-run mode (preview changes):**
```bash
python idmPatcher.py IDMan.exe --dry-run
```

**Patch and create new file:**
```bash
python idmPatcher.py IDMan.exe
```
This creates `IDMan.xex` with the patches applied.

**Patch and overwrite original:**
```bash
python idmPatcher.py IDMan.exe --overwrite
```

## 🔨 Building an Executable

You can build a standalone executable using PyInstaller:

### Prerequisites

Install PyInstaller:
```bash
pip install pyinstaller
```

### Build Command

```bash
pyinstaller idmPatcher.spec
```

Or manually:
```bash
pyinstaller --onefile --console --name idmPatcher idmPatcher.py
```

The executable will be created in the `dist/` directory.

### Build Options

- `--onefile`: Creates a single executable file
- `--console`: Shows console window (recommended for this tool)
- `--name`: Specifies the output executable name

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 💬 Support

If you encounter any issues or have questions:

- Open an issue on GitHub
- Provide detailed information about the problem
- Include the error message and steps to reproduce

## 📄 License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

```
Copyright (C) 2024 IDM Patcher Contributors

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
```

---

**Note:** Always backup your files before patching. This tool modifies binary files and incorrect usage could result in corrupted executables.
